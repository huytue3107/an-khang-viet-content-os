#!/usr/bin/env python3
"""Generate the current AKV visual batch with UTF-8 prompts."""

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate-infographic.py"
REFERENCE = ROOT / "reference" / "infographic-ref-1.jpeg"

JOBS = [
    {
        "label": "Bài 002",
        "output": ROOT / "posts" / "002-30-ngay-truoc-khi-xay-nha" / "image.png",
        "prompt": (
            "Tạo infographic tiếng Việt: 30 NGÀY TRƯỚC KHI XÂY NHÀ - ĐỪNG TÌM MẪU, "
            "HÃY CHỐT 3 CON SỐ NÀY. 1. Ngân sách & khoản dự phòng. "
            "2. Thời gian sinh hoạt thực tế tại nhà. "
            "3. Mã vật tư hoàn thiện trong báo giá. Dưới cùng: AN KHANG VIỆT."
        ),
    },
    {
        "label": "Bài 003",
        "output": ROOT / "posts" / "003-anh-cu-yen-tam-khong-phai-hop-dong" / "image.png",
        "prompt": (
            "Tạo infographic cảnh báo tiếng Việt: 'ANH CỨ YÊN TÂM' KHÔNG PHẢI LÀ "
            "ĐIỀU KHOẢN HỢP ĐỒNG. 3 điểm phải có giấy trắng mực đen: "
            "1. Bảng mã vật tư chi tiết. 2. Điều khoản phát sinh/bán thầu. "
            "3. Tiến độ nghiệm thu từng phần. Dưới cùng: AN KHANG VIỆT."
        ),
    },
    {
        "label": "Bài 004",
        "output": ROOT / "posts" / "004-sua-nha-pho-dung-voi-son-moi" / "image.png",
        "prompt": (
            "Tạo infographic tiếng Việt theo phong cách sổ khám bệnh công trình: "
            "3 BỆNH NỀN NHÀ CŨ PHẢI XỬ LÝ TRƯỚC KHI DECOR. "
            "1. Bệnh thấm: xử lý tận gốc tường giáp ranh, nhà vệ sinh. "
            "2. Bệnh mạch máu: nâng cấp dây điện, thông ống nước. "
            "3. Bệnh khó thở: cải tạo thông gió, lấy sáng tự nhiên. "
            "Dưới cùng: AN KHANG VIỆT."
        ),
    },
    {
        "label": "Bài 005",
        "output": ROOT / "posts" / "005-ban-ve-tien-ty-bi-binh-dan-hoa" / "image.png",
        "prompt": (
            "Tạo infographic tiếng Việt: BẢN VẼ TIỀN TỶ CŨNG CÓ THỂ BỊ 'BÌNH DÂN HÓA'. "
            "Nhà sang nằm ở độ hoàn thiện chi tiết: đường ron gạch thẳng tắp, "
            "mí đá líp cạnh sắc nét, phào chỉ khít rịt, hệ thống giấu dây thông minh, "
            "giám sát khắt khe từng milimet. Dưới cùng: AN KHANG VIỆT."
        ),
    },
    {
        "label": "Bài 006",
        "output": ROOT / "posts" / "006-lap-smarthome-quen-tinh-duong-dien" / "image.png",
        "prompt": (
            "Tạo infographic tiếng Việt: 3 BỰC MÌNH KHI LẮP SMARTHOME THEO CẢM HỨNG. "
            "1. Đèn chớp nháy vì thiếu dây N (nguội). "
            "2. Kịch bản công nghệ cản trở thói quen sống thật. "
            "3. Mất mạng là nhà thành 'stupid-home'. "
            "Phải tính đường điện ngay từ bản vẽ. Dưới cùng: AN KHANG VIỆT."
        ),
    },
]


def run_job(job):
    print(f"Đang tạo ảnh cho {job['label']}...", flush=True)
    cmd = [
        sys.executable,
        str(GENERATOR),
        "--reference",
        str(REFERENCE),
        "--output",
        str(job["output"]),
        "--prompt",
        job["prompt"],
    ]
    return subprocess.run(cmd, cwd=ROOT)


def main():
    parser = argparse.ArgumentParser(description="Generate all current AKV post visuals")
    parser.add_argument("--dry-run", action="store_true", help="Print planned outputs without calling OpenRouter")
    args = parser.parse_args()

    if args.dry_run:
        for job in JOBS:
            print(f"{job['label']}: {job['output']}")
        return 0

    failed = []
    for job in JOBS:
        result = run_job(job)
        if result.returncode != 0:
            failed.append(job["label"])
            print("Dừng batch vì mục trên bị lỗi. Sửa lỗi rồi chạy lại.", file=sys.stderr)
            return 1

    print("Đang cập nhật Dashboard...", flush=True)
    dashboard = subprocess.run([sys.executable, str(ROOT / "scripts" / "build-dashboard.py")], cwd=ROOT)
    if dashboard.returncode != 0:
        failed.append("Dashboard")

    if failed:
        print("Không hoàn tất các mục: " + ", ".join(failed), file=sys.stderr)
        return 1

    print("Hoàn tất. Mở file outputs/dashboard.html để xem kết quả.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
