#!/usr/bin/env python3
"""
Generate an An Khang Viet infographic through OpenRouter.

Default model:
    google/gemini-3.1-flash-image-preview

Usage:
    python scripts/generate-infographic.py \
      --reference reference/infographic-ref-1.jpeg \
      --output posts/002-example/image.png \
      --prompt "Vietnamese prompt here"

The generated single image is post-processed with logo AKV.png in the top-left corner.
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
from pathlib import Path

import requests
from PIL import Image


API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3.1-flash-image-preview"
DEFAULT_LOGO_PATH = Path(__file__).resolve().parents[1] / "logo AKV.png"

AKV_STYLE_PREFIX = """
AN KHANG VIỆT brand infographic style. Create a practical Vietnamese construction/house-building education graphic for homeowners. Use the official brand DNA: roof/home, warmth, solid foundation, trust, Vietnamese living, sustainable value. Palette: Đỏ An Khang #E52620 as the main accent for headline/CTA, Cam Phát Triển #F36B21 for slanted lines and icons, Nâu Mái Nhà #A77A4D for roof/foundation shapes, Vàng Ánh Sáng #FFD500 as a small warm window/highlight only, Ghi Nền Móng #F4F1ED or white as background, Đen Chữ Chính #1F1F1F for text. Use clean bold sans-serif typography, clear hierarchy, roof/A-shape geometry, three restrained slanted orange-red lines, square window motif, blueprint/ruler/checklist cues. The design should feel solid like a foundation, warm like a home, and clear like a commitment. Avoid neon, glossy real-estate hype, clutter, weak curvy fonts, fake stock-photo feeling, and "sale đất nền chợ búa" styling. Keep layout mobile-readable at 4:5.
"""

AKV_TEXT_RULE = """
CRITICAL: render Vietnamese diacritics exactly as provided. Do not remove accents. Do not invent prices, numbers, project names, warranty policies, or technical claims not included in the prompt.
"""


def load_env(path):
    env = {}
    if not path.exists():
        return env
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip()
    return env


def read_api_key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key
    env = load_env(Path(".env"))
    return env.get("OPENROUTER_API_KEY")


def encode_image_data_url(path):
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def build_prompt(user_prompt, no_style_prefix=False):
    if no_style_prefix:
        return f"{user_prompt.strip()}\n\n{AKV_TEXT_RULE.strip()}"
    return f"{AKV_STYLE_PREFIX.strip()}\n\nCONTENT TO RENDER:\n{user_prompt.strip()}\n\n{AKV_TEXT_RULE.strip()}"


def build_message_content(prompt, reference_path=None):
    content = [{"type": "text", "text": prompt}]
    if reference_path:
        content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": encode_image_data_url(reference_path),
                },
            }
        )
    return content


def request_image(api_key, model, prompt, reference_path=None, aspect_ratio="4:5", image_size="1K"):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/huytue3107/an-khang-viet-content-os",
        "X-Title": "An Khang Viet Content OS",
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": build_message_content(prompt, reference_path),
            }
        ],
        "modalities": ["image", "text"],
        "image_config": {
            "aspect_ratio": aspect_ratio,
            "image_size": image_size,
        },
        "stream": False,
    }
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=300)
    if not resp.ok:
        raise RuntimeError(f"OpenRouter request failed ({resp.status_code}): {resp.text}")
    return resp.json()


def extract_image_data_url(result):
    choices = result.get("choices") or []
    for choice in choices:
        message = choice.get("message") or {}
        for image in message.get("images") or []:
            image_url = image.get("image_url") or image.get("imageUrl") or {}
            url = image_url.get("url") if isinstance(image_url, dict) else None
            if url:
                return url
    raise RuntimeError(f"OpenRouter response did not include generated image data: {json.dumps(result)[:1000]}")


def save_data_url(data_url, output_path):
    if not data_url.startswith("data:") or "," not in data_url:
        raise RuntimeError("Expected OpenRouter image output as a base64 data URL")
    _, b64_data = data_url.split(",", 1)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(base64.b64decode(b64_data))


def add_top_left_logo(image_path, logo_path=DEFAULT_LOGO_PATH, max_width=190, margin=34):
    """Post-process a single generated image with the official AKV logo."""
    if not logo_path.exists():
        return

    img = Image.open(image_path).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")
    scale = min(max_width / logo.width, 1.0)
    logo = logo.resize((int(logo.width * scale), int(logo.height * scale)), Image.LANCZOS)

    plate_pad = 14
    plate = Image.new(
        "RGBA",
        (logo.width + plate_pad * 2, logo.height + plate_pad * 2),
        (255, 255, 255, 225),
    )
    plate.alpha_composite(logo, (plate_pad, plate_pad))
    img.alpha_composite(plate, (margin, margin))
    img.convert("RGB").save(image_path, "PNG", quality=95)


def main():
    parser = argparse.ArgumentParser(description="Generate An Khang Viet infographic with OpenRouter")
    parser.add_argument("--reference", help="Optional local style reference image path")
    parser.add_argument("--output", required=True, help="Output image path")
    parser.add_argument("--prompt", required=True, help="Prompt text")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"OpenRouter model (default: {DEFAULT_MODEL})")
    parser.add_argument("--aspect-ratio", default="4:5", help="Image aspect ratio (default: 4:5)")
    parser.add_argument("--image-size", default="1K", help="Image size: 0.5K, 1K, 2K, 4K (default: 1K)")
    parser.add_argument("--no-style-prefix", action="store_true", help="Send only the provided prompt plus Vietnamese text safety rule")
    args = parser.parse_args()

    api_key = read_api_key()
    if not api_key or api_key == "your_openrouter_api_key_here":
        raise RuntimeError("Missing OPENROUTER_API_KEY in environment or .env")

    reference_path = Path(args.reference) if args.reference else None
    if reference_path and not reference_path.exists():
        raise RuntimeError(f"Reference image not found: {reference_path}")

    prompt = build_prompt(args.prompt, args.no_style_prefix)
    result = request_image(
        api_key=api_key,
        model=args.model,
        prompt=prompt,
        reference_path=reference_path,
        aspect_ratio=args.aspect_ratio,
        image_size=args.image_size,
    )
    data_url = extract_image_data_url(result)
    output_path = Path(args.output)
    save_data_url(data_url, output_path)
    add_top_left_logo(output_path)
    print(f"Saved image: {args.output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
