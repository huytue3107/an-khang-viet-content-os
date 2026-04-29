# Tạo Batch 10 Nội Dung — An Khang Việt

Tạo 10 nội dung sẵn sàng biên tập/xuất bản theo văn phong **Chuyên Gia Xây Nhà**.

## Bắt Buộc Đọc Trước

1. `AKV-content.md`
2. `CLAUDE.md`
3. `context/strategy.md`
4. `context/icp.md`
5. `context/voice-analysis.md`
6. 5 bài gần nhất trong `posts/` nếu có

## Tệp Khách Hàng Cần Luân Phiên

Khi tạo batch, không viết cả 10 bài cho cùng một nhóm. Ưu tiên phủ ít nhất 5 trong 8 tệp:

1. Gia đình trẻ xây căn nhà đầu tiên.
2. Người đang tìm thiết kế và thi công trọn gói.
3. Chủ biệt thự/nhà phố cao cấp.
4. Chủ nhà cải tạo nhà cũ.
5. Nhà đầu tư bất động sản/cho thuê/homestay.
6. Khách smarthome/nhà xanh.
7. Gia đình nhiều thế hệ.
8. Người nâng cấp phong cách sống.

## Cơ Cấu Batch

### Theo Trụ Cột

| Trụ cột | Số lượng | Mục tiêu |
| --- | ---: | --- |
| Kinh nghiệm xây nhà | 4 | Giáo dục thị trường, tăng lưu bài |
| Cảnh báo rủi ro | 2-3 | Chạm nỗi đau, tạo tranh luận |
| Case study/công trình thực tế | 1-2 | Chứng minh năng lực, chỉ dùng khi có dữ kiện thật |
| Quy trình/thương hiệu AKV | 1 | Xây niềm tin, chuyển đổi inbox |
| Bán hàng mềm | 1 | Mời tư vấn nhẹ, không quảng cáo lố |

Nếu không có case thật, thay phần case bằng “bài học/thực tế công trình thường gặp” và ghi rõ không nêu tên/chi phí/địa điểm.

### Theo Định Dạng

Phân bổ linh hoạt, tránh 3 bài liền cùng format:

- Bài tư vấn Facebook/Zalo.
- Checklist lưu bài.
- Script video 45-60 giây.
- Bài tranh luận nhẹ.
- Bài bán hàng mềm.
- Carousel/checklist.
- Infographic idea.

## Giai Đoạn 1: Lên Ý Tưởng

1. Lấy chủ đề từ 5 trụ cột AKV.
2. Tránh lặp chủ đề hẹp với các bài gần nhất.
3. Với mỗi ý tưởng, ghi:
   - Tiêu đề làm việc.
   - Trụ cột AKV.
   - Đối tượng chủ nhà.
   - Tệp khách hàng cụ thể.
   - Nỗi đau.
   - Format.
   - Hook dự kiến.
   - CTA mềm.
4. Lưu plan vào `outputs/YYYY-MM-DD-akv-batch-content-plan.md`.

## Giai Đoạn 2: Viết Text

Với từng bài:

1. Xác định số post tiếp theo trong `posts/`.
2. Tạo thư mục `posts/NNN-slug/`.
3. Viết `post.md` theo chuẩn:

```markdown
# Bài NNN: Tiêu Đề

**Ngày tạo:** YYYY-MM-DD
**Nền tảng:** Facebook / TikTok-Reels / Zalo / Website / Email-Inbox
**Định dạng:** Bài post / Caption ngắn / Script video / Checklist / Carousel / Bài bán hàng mềm
**Trụ cột AKV:** Kinh nghiệm xây nhà / Cảnh báo rủi ro / Tư duy thiết kế / Quy trình AKV / Case study
**Tệp khách hàng:** [Một trong 8 tệp AKV]
**Mục tiêu:** Tạo niềm tin / Tăng inbox / Tăng lưu bài / Giáo dục thị trường / Tạo tranh luận
**Visual:** Ảnh công trình / AI Infographic / Carousel / Không dùng
**Trạng thái:** Draft

---

## Post Text

[Nội dung copy-paste ready]

---

## Voice Check

- Hook:
- Tệp khách hàng:
- Nỗi đau:
- Lời khuyên cụ thể:
- CTA mềm:
- Đã tránh:

---

## Image Notes

[Mô tả visual hoặc prompt]
```

## Giai Đoạn 2.5: Duyệt Trước Visual

Không generate visual tốn API trước khi text đã đủ chắc hoặc user đã xác nhận.

Báo user danh sách 10 bài gồm:

- Tiêu đề.
- Trụ cột.
- Tệp khách hàng.
- Format.
- Hook.
- CTA.
- Visual đề xuất.

## Giai Đoạn 3: Tạo Visual Nếu Được Duyệt

### Infographic

```powershell
python scripts/generate-infographic.py --reference reference/infographic-ref-1.jpeg --output posts/NNN-slug/image.png --prompt "<prompt tiếng Việt có dấu>"
```

### Carousel

```powershell
python scripts/generate-carousel.py --json posts/NNN-slug/content.json --output posts/NNN-slug/carousel.pdf
```

## Giai Đoạn 4: Hoàn Thiện

1. Chạy `python scripts/build-dashboard.py`.
2. Kiểm tra `Voice Check` từng bài.
3. Kiểm tra không có dữ kiện bị bịa.
4. Báo cáo danh sách 10 bài, file đã tạo, visual còn chờ duyệt nếu có.

## Quality Bar

- Hook phải thẳng, không chung chung.
- Nội dung phải có ích, không chỉ nêu vấn đề.
- Mỗi bài nên có một câu chốt nhớ lâu.
- CTA phải tự nhiên.
- Không viết như bảng báo giá.
- Không hứa điều An Khang Việt chưa cung cấp dữ kiện.
