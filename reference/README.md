# Reference — An Khang Việt Content

Thư mục này chứa visual reference, ví dụ packaging và tài liệu phụ cho workflow nội dung.

Nguồn sự thật về voice vẫn là `AKV-content.md`. Tài liệu trong `reference/` chỉ hỗ trợ đóng gói ý tưởng hoặc visual, không được thay thế style guide AKV.

## Ảnh Tham Chiếu Infographic

Ba ảnh sau được dùng làm ảnh tham chiếu khi tạo infographic qua OpenRouter:

- `infographic-ref-1.jpeg` — layout radial hoặc checklist trung tâm.
- `infographic-ref-2.jpeg` — layout headline lớn, các ý xung quanh.
- `infographic-ref-3.jpeg` — layout flow dọc, từng bước rõ ràng.

Style AKV chính thức lấy từ `context/brand-dna.md`:

- Đỏ An Khang `#E52620`, Cam Phát Triển `#F36B21`, Nâu Mái Nhà `#A77A4D`, Vàng Ánh Sáng `#FFD500`.
- Nền trắng hoặc Ghi Nền Móng `#F4F1ED`.
- Chữ Đen Chữ Chính `#1F1F1F`, rõ và dễ đọc trên mobile.
- Có tín hiệu logo/ngành: chữ A mái nhà, 3 đường xiên cam đỏ, ô cửa vàng, bản vẽ, grid, thước, checklist, khối nhà, vật liệu.
- Tinh thần: chắc như nền móng, ấm như mái nhà, rõ như một cam kết.

## Carousel Reference

`carousel-ref/` chứa slide tham chiếu và phân tích style. Carousel AKV nên ưu tiên:

- Hook lưu bài.
- 5-9 điểm kiểm tra.
- Mỗi slide một ý.
- CTA mềm ở cuối.
- Tiếng Việt có dấu, không quá tải chữ.
- Bố cục rõ, có mảng mái nâu hoặc pattern 3 đường xiên dùng tiết chế.
- Mỗi slide carousel dùng watermark `logo AKV.png` ở chính giữa, rộng 50% canvas, opacity 20%.
- Ảnh đơn/infographic dùng `logo AKV.png` ở góc trái trên.

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

Script dùng `OPENROUTER_API_KEY` và model mặc định `google/gemini-3.1-flash-image-preview`.
