#!/usr/bin/env python3
"""
Generate an An Khang Viet infographic with Kie.ai using a style reference image.

Usage:
    python3 scripts/generate-infographic.py \
      --reference reference/infographic-ref-1.jpeg \
      --output posts/002-example/image.png \
      --prompt "Vietnamese prompt here"
"""

import argparse
import base64
import io
import json
import os
import sys
import time
from pathlib import Path

import requests
from PIL import Image


API_URL = "https://api.kie.ai/api/v1/jobs/createTask"
STATUS_URL = "https://api.kie.ai/api/v1/jobs/recordInfo"

AKV_STYLE_PREFIX = """
An Khang Việt Content infographic style. Create a practical Vietnamese construction/house-building education graphic for homeowners. Use a warm light neutral background (#F7F4EC), deep charcoal green text (#1F2520), construction green accent (#2F6B4F), subtle earth-gold accent (#D7A84F), clean high-contrast typography, simple blueprint grid lines, ruler/checklist/house-outline construction cues, and a small brand mark reading "AN KHANG VIET". The design should feel clear, trustworthy, grounded, and practical, not luxury real-estate glossy, not neon, not dark. Keep layout mobile-readable at 1080x1350.
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
    key = os.environ.get("KIE_AI_API_KEY")
    if key:
        return key
    env = load_env(Path(".env"))
    return env.get("KIE_AI_API_KEY")


def encode_reference_image(path):
    with Image.open(path) as img:
        img = img.convert("RGB")
        img.thumbnail((512, 512), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=70)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


def create_task(api_key, prompt, reference_image):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "nano-banana-pro",
        "input": {
            "prompt": prompt,
            "width": 1080,
            "height": 1350,
            "image_num": 1,
            "reference_image": reference_image,
        },
    }
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") not in (200, 0):
        raise RuntimeError(f"Kie.ai createTask failed: {data.get('msg', data)}")
    task_id = data.get("data", {}).get("taskId")
    if not task_id:
        raise RuntimeError(f"Could not create task: {data}")
    return task_id


def poll_result(api_key, task_id, interval=5, timeout=300):
    headers = {"Authorization": f"Bearer {api_key}"}
    started = time.time()
    while True:
        if time.time() - started > timeout:
            raise TimeoutError(f"Timed out waiting for task {task_id}")
        time.sleep(interval)
        resp = requests.get(f"{STATUS_URL}?taskId={task_id}", headers=headers, timeout=60)
        resp.raise_for_status()
        payload = resp.json()
        if payload.get("code") not in (200, 0):
            raise RuntimeError(f"Kie.ai recordInfo failed: {payload.get('msg', payload)}")
        data = payload.get("data", {})
        state = data.get("state")
        if state == "success":
            result = json.loads(data["resultJson"])
            return result["resultUrls"][0]
        if state == "failed":
            raise RuntimeError(f"Kie.ai task failed: {data}")


def download_image(url, output_path):
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(resp.content)


def build_prompt(user_prompt, no_style_prefix=False):
    if no_style_prefix:
        return f"{user_prompt.strip()}\n\n{AKV_TEXT_RULE.strip()}"
    return f"{AKV_STYLE_PREFIX.strip()}\n\nCONTENT TO RENDER:\n{user_prompt.strip()}\n\n{AKV_TEXT_RULE.strip()}"


def main():
    parser = argparse.ArgumentParser(description="Generate An Khang Viet infographic with Kie.ai")
    parser.add_argument("--reference", required=True, help="Path to style reference image")
    parser.add_argument("--output", required=True, help="Output image path")
    parser.add_argument("--prompt", required=True, help="Prompt text")
    parser.add_argument("--no-style-prefix", action="store_true", help="Send only the provided prompt plus Vietnamese text safety rule")
    args = parser.parse_args()

    api_key = read_api_key()
    if not api_key or api_key == "YOUR_KEY":
        raise RuntimeError("Missing KIE_AI_API_KEY in environment or .env")

    reference_image = encode_reference_image(Path(args.reference))
    prompt = build_prompt(args.prompt, args.no_style_prefix)
    task_id = create_task(api_key, prompt, reference_image)
    print(f"Created task: {task_id}")
    result_url = poll_result(api_key, task_id)
    download_image(result_url, Path(args.output))
    print(f"Saved image: {args.output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
