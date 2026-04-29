#!/usr/bin/env python3
"""
Add scroll-stopping text overlay to An Khang Viet photos.

Adds a semi-transparent dark gradient + bold hook text to a photo,
matching the practical An Khang Viet Content visual style.
Adds logo AKV.png to the top-left corner.

Usage:
    python3 scripts/add-photo-overlay.py \
        --photo context/images/photo.jpg \
        --text "Đừng ký hợp đồng xây nhà khi còn 5 điểm mơ hồ" \
        --output posts/017-example/image.png

    # With highlighted (Do An Khang red) words:
    python3 scripts/add-photo-overlay.py \
        --photo context/images/photo.jpg \
        --text "7 ĐIỀU chủ nhà nên kiểm tra trước khi ký" \
        --highlight "7" "ĐIỀU" \
        --output posts/017-example/image.png

    # Position: bottom (default) | center | top
    python3 scripts/add-photo-overlay.py \
        --photo context/images/photo.jpg \
        --text "Nhà đẹp mà ở bất tiện thì chỉ đẹp cho người ngoài xem" \
        --position center \
        --output posts/017-example/image.png
"""

import argparse
import os
import sys
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ─────────────────────────────────────────────
# BRAND CONFIG
# ─────────────────────────────────────────────
BRAND_NAME   = "AN KHANG VIET"
LOGO_PATH    = Path(__file__).resolve().parents[1] / "logo AKV.png"
ACCENT_COLOR = (229, 38, 32)         # Do An Khang #E52620
SECONDARY_COLOR = (243, 107, 33)     # Cam Phat Trien #F36B21
WHITE        = (255, 255, 255)
BLACK        = (0, 0, 0)
DARK_OVERLAY = (0, 0, 0, 180)        # Semi-transparent black

# Output canvas
W, H = 1080, 1350

# Font paths
FONT_BOLD   = "C:/Windows/Fonts/arialbd.ttf"
FONT_NORMAL = "C:/Windows/Fonts/arial.ttf"


def add_top_left_logo(img, logo_path=LOGO_PATH, max_width=190, margin=34):
    """Add the official AKV logo to the top-left corner of a single image."""
    if not logo_path.exists():
        return img

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
    return img


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = " ".join(current + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_text_with_highlights(draw, lines, x_center, y_start, font, highlight_words,
                               line_spacing=14):
    """Draw text lines with optional lime-green highlighted words."""
    font_size = font.size if hasattr(font, 'size') else 56
    for line in lines:
        # Measure full line width for centering
        bbox = draw.textbbox((0, 0), line, font=font)
        line_w = bbox[2] - bbox[0]
        line_h = bbox[3] - bbox[1]

        if not highlight_words:
            # Drop shadow
            draw.text((x_center - line_w // 2 + 3, y_start + 3), line,
                      font=font, fill=(0, 0, 0, 160))
            draw.text((x_center - line_w // 2, y_start), line,
                      font=font, fill=WHITE)
        else:
            # Word-by-word coloring
            words = line.split(" ")
            x = x_center - line_w // 2
            for i, word in enumerate(words):
                color = ACCENT_COLOR if word in highlight_words else WHITE
                # Shadow
                draw.text((x + 3, y_start + 3), word, font=font, fill=(0, 0, 0, 160))
                draw.text((x, y_start), word, font=font, fill=color)
                word_bbox = draw.textbbox((0, 0), word + (" " if i < len(words)-1 else ""), font=font)
                x += word_bbox[2] - word_bbox[0]

        y_start += line_h + line_spacing
    return y_start


def add_overlay(photo_path, hook_text, output_path,
                highlight_words=None, position="bottom"):
    """Main function: add gradient + text overlay to photo."""

    # ── Load & resize photo (cover crop — keep aspect ratio) ─
    img = Image.open(photo_path).convert("RGBA")
    orig_w, orig_h = img.size
    scale = max(W / orig_w, H / orig_h)
    new_w = int(orig_w * scale)
    new_h = int(orig_h * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - W) // 2
    top  = (new_h - H) // 2
    img  = img.crop((left, top, left + W, top + H))

    # ── Dark gradient overlay ────────────────────────────────
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_ov = ImageDraw.Draw(overlay)

    if position == "bottom":
        # Gradient from transparent at 40% to dark at bottom
        gradient_start = int(H * 0.42)
        for y in range(gradient_start, H):
            t = (y - gradient_start) / (H - gradient_start)
            alpha = int(200 * min(t * 1.4, 1.0))
            draw_ov.line([(0, y), (W, y)], fill=(0, 0, 0, alpha))
    elif position == "top":
        gradient_end = int(H * 0.45)
        for y in range(0, gradient_end):
            t = 1 - (y / gradient_end)
            alpha = int(190 * min(t * 1.4, 1.0))
            draw_ov.line([(0, y), (W, y)], fill=(0, 0, 0, alpha))
    else:  # center
        # Dark band in the middle
        band_y1 = int(H * 0.30)
        band_y2 = int(H * 0.72)
        for y in range(band_y1, band_y2):
            dist_from_center = abs(y - (band_y1 + band_y2) // 2)
            max_dist = (band_y2 - band_y1) // 2
            t = 1 - (dist_from_center / max_dist)
            alpha = int(180 * t)
            draw_ov.line([(0, y), (W, y)], fill=(0, 0, 0, alpha))

    img = Image.alpha_composite(img, overlay)
    img = add_top_left_logo(img)

    # ── Text ─────────────────────────────────────────────────
    draw = ImageDraw.Draw(img)

    # Try large font first, shrink if text too long
    max_text_w = W - 80
    for font_size in [50, 45, 39, 34, 29, 25]:
        font = load_font(FONT_BOLD, font_size)
        lines = wrap_text(hook_text, font, max_text_w, draw)
        if len(lines) <= 4:
            break

    line_h = font_size + 14
    total_text_h = len(lines) * line_h

    # Position text block
    if position == "bottom":
        text_y = H - total_text_h - 120
    elif position == "top":
        text_y = 80
    else:
        text_y = (H - total_text_h) // 2 - 20

    highlight_set = set(highlight_words) if highlight_words else set()
    draw_text_with_highlights(draw, lines, W // 2, text_y, font,
                               highlight_set, line_spacing=16)

    # ── Brand mark ───────────────────────────────────────────
    brand_font = load_font(FONT_BOLD, 28)
    brand_bbox = draw.textbbox((0, 0), BRAND_NAME, font=brand_font)
    brand_w = brand_bbox[2] - brand_bbox[0]
    # Brand pill background
    pad = 14
    pill_x1 = W - brand_w - pad * 2 - 30
    pill_y1 = H - 60
    pill_x2 = W - 30
    pill_y2 = H - 28
    draw.rounded_rectangle([pill_x1, pill_y1, pill_x2, pill_y2],
                            radius=10, fill=ACCENT_COLOR)
    draw.line([(pill_x1 + 12, pill_y2 + 5), (pill_x1 + 58, pill_y1 - 5)],
              fill=SECONDARY_COLOR, width=5)
    draw.text((pill_x1 + pad, pill_y1 + 4), BRAND_NAME,
              font=brand_font, fill=BLACK)

    # ── Save ─────────────────────────────────────────────────
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    img.convert("RGB").save(output_path, "PNG", quality=95)
    print(f"Saved: {output_path} ({os.path.getsize(output_path):,} bytes)")


def main():
    parser = argparse.ArgumentParser(
        description="Add scroll-stopping text overlay to personal photos"
    )
    parser.add_argument("--photo",   required=True, help="Input photo path")
    parser.add_argument("--text",    required=True, help="Hook text to overlay")
    parser.add_argument("--output",  required=True, help="Output image path")
    parser.add_argument("--highlight", nargs="*", default=[],
                        help="Words to highlight in brand red")
    parser.add_argument("--position", choices=["bottom", "top", "center"],
                        default="bottom", help="Text position (default: bottom)")
    args = parser.parse_args()

    if not os.path.exists(args.photo):
        print(f"ERROR: photo not found: {args.photo}", file=sys.stderr)
        sys.exit(1)

    add_overlay(
        photo_path=args.photo,
        hook_text=args.text,
        output_path=args.output,
        highlight_words=args.highlight or [],
        position=args.position,
    )


if __name__ == "__main__":
    main()
