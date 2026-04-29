# Reference — An Khang Việt Content

Thư mục này chứa visual reference, ví dụ packaging và tài liệu phụ cho workflow nội dung.

Nguồn sự thật về voice vẫn là `AKV-content.md`. Tài liệu trong `reference/` chỉ hỗ trợ đóng gói ý tưởng hoặc visual, không được thay thế style guide AKV.

## Ảnh Tham Chiếu Infographic

Ba ảnh sau được dùng làm `reference_image` khi tạo infographic bằng Kie.ai:

- `infographic-ref-1.jpeg` — layout radial hoặc checklist trung tâm.
- `infographic-ref-2.jpeg` — layout headline lớn, các ý xung quanh.
- `infographic-ref-3.jpeg` — layout flow dọc, từng bước rõ ràng.

Khi có brand guideline thật, thay ba ảnh này bằng style AKV chính thức:

- Nền sáng trung tính.
- Accent xanh xây dựng hoặc vàng đất nhẹ.
- Chữ rõ, dễ đọc trên mobile.
- Có tín hiệu ngành xây nhà: bản vẽ, grid, thước, checklist, khối nhà, vật liệu.

## Carousel Reference

`carousel-ref/` chứa slide tham chiếu và phân tích style. Carousel AKV nên ưu tiên:

- Hook lưu bài.
- 5-9 điểm kiểm tra.
- Mỗi slide một ý.
- CTA mềm ở cuối.
- Tiếng Việt có dấu, không quá tải chữ.

## Tư Liệu Phụ

Các file ví dụ copywriting hoặc packaging cũ có thể giữ lại để học cấu trúc hook/bố cục, nhưng không còn là chuẩn giọng viết mặc định.

Khi dùng tài liệu phụ:

- Chỉ mượn cấu trúc đóng gói.
- Thay substance bằng chủ đề xây nhà/sửa nhà/thiết kế/nhà thầu.
- Viết lại hoàn toàn theo `AKV-content.md`.
- Không đưa giọng cá nhân của tác giả khác vào nội dung AKV.

## Lệnh Tạo Infographic

```powershell
python scripts/generate-infographic.py `
  --reference reference/infographic-ref-1.jpeg `
  --output posts/NNN-slug/image.png `
  --prompt "Checklist 5 điều chủ nhà cần kiểm tra trước khi ký hợp đồng xây nhà..."
```
