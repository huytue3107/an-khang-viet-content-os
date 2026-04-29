# Init Context — An Khang Việt Content OS

Cập nhật context thương hiệu từ thông tin user cung cấp, nhưng không thay thế `AKV-content.md`.

## Biến Đầu Vào

`input: $ARGUMENTS`

Input có thể là:

- Thông tin dịch vụ, quy trình, chính sách thật.
- Link website/kênh social cần tham khảo.
- Dữ liệu case study/công trình thật.
- Brand guideline visual.
- Chân dung khách hàng hoặc ghi chú sales.

## Quy Tắc

- `AKV-content.md` luôn là master style guide. Không sửa file này trừ khi user yêu cầu rõ.
- Nếu dữ liệu mới mâu thuẫn với `AKV-content.md`, ghi nhận và hỏi user trước khi đổi định hướng.
- Chỉ cập nhật context bằng dữ kiện có nguồn từ user hoặc tài liệu thật.
- Không tự tạo giá, chính sách, số năm kinh nghiệm, số công trình, tên khách, địa điểm.

## File Có Thể Cập Nhật

| File | Khi nào cập nhật |
| --- | --- |
| `context/profile.md` | Có thay đổi định vị, kênh, cách xưng hô, hình ảnh thương hiệu |
| `context/business.md` | Có dịch vụ, quy trình, chính sách, thông tin liên hệ thật |
| `context/icp.md` | Có chân dung khách hàng mới hoặc insight sales |
| `context/strategy.md` | Có mục tiêu/campaign/trụ cột ưu tiên mới |
| `context/voice-analysis.md` | Có ví dụ bài viết thật hoặc điều chỉnh voice |
| `context/metrics.md` | Có số liệu vận hành thật |
| `reference/README.md` | Có visual reference hoặc brand guideline mới |

## Quy Trình

1. Đọc `AKV-content.md`, `CLAUDE.md`, `context/`.
2. Phân loại input thành: brand, dịch vụ, ICP, voice, visual, metrics, case.
3. Cập nhật file context phù hợp.
4. Nếu có case thật, lưu tóm tắt dữ kiện vào `context/data/` hoặc plan/post liên quan.
5. Chạy rà soát để đảm bảo không có placeholder hoặc dữ kiện bị suy diễn.

## Báo Cáo Sau Khi Cập Nhật

- File đã cập nhật.
- Dữ kiện mới đã thêm.
- Dữ kiện còn thiếu cần user bổ sung.
- Bất kỳ điểm nào chưa rõ hoặc có rủi ro nếu dùng trong content.
