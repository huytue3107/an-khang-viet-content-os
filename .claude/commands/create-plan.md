# Lập Kế Hoạch — An Khang Việt Content OS

Tạo kế hoạch triển khai chi tiết cho campaign, series, batch nội dung, template hoặc thay đổi workflow trong workspace AKV.

## Biến Đầu Vào

`request: $ARGUMENTS`

## Nguyên Tắc

- Đây là bước lập kế hoạch, không phải triển khai.
- Luôn đọc `AKV-content.md`, `CLAUDE.md` và các file `context/` trước khi lập kế hoạch.
- Kế hoạch phải bám 5 trụ cột AKV: kinh nghiệm xây nhà, cảnh báo rủi ro, tư duy thiết kế nhà đáng sống, quy trình An Khang Việt, case/công trình thực tế.
- Kế hoạch phải chọn rõ tệp khách hàng theo mục 3.2-3.7 của `AKV-content.md`, nhất là 8 tệp mở rộng.
- Không đưa vào kế hoạch các bài cần case, giá, vật tư, chính sách hoặc số liệu nếu chưa có dữ kiện thật.
- Nếu thiếu thông tin quan trọng, ghi rõ trong “Câu hỏi mở” thay vì tự quyết.

## Nghiên Cứu Trước Khi Viết

1. Đọc:
   - `AKV-content.md`
   - `CLAUDE.md`
   - `context/strategy.md`
   - `context/icp.md`
   - `context/voice-analysis.md`
2. Nếu lập campaign, kiểm tra `posts/` và `outputs/` để tránh lặp chủ đề gần đây.
3. Nếu có visual/carousel, kiểm tra `reference/` và script tương ứng.

## File Kế Hoạch

Tạo file trong `plans/`:

```text
YYYY-MM-DD-{ten-mo-ta}.md
```

## Mẫu Kế Hoạch

```markdown
# Kế Hoạch: <tiêu đề>

**Tạo lúc:** <YYYY-MM-DD>
**Trạng thái:** Draft
**Yêu cầu:** <tóm tắt một dòng>

---

## Tổng Quan

<Kết quả cuối cùng, vì sao quan trọng với An Khang Việt Content.>

## Trụ Cột Và Mục Tiêu

| Trụ cột AKV | Vai trò trong kế hoạch | Mục tiêu |
| --- | --- | --- |
| <trụ cột> | <nội dung sẽ làm> | <tạo niềm tin/tăng inbox/tăng lưu bài/...> |

## Đối Tượng Và Insight

- **Đối tượng chính:** <nhóm chủ nhà>
- **Tệp khách hàng:** <một trong 8 tệp AKV>
- **Nỗi đau cần đánh vào:** <nỗi đau cụ thể>
- **Hành động mong muốn:** <lưu bài/inbox/gửi báo giá/hỏi tư vấn/...>

## Thay Đổi Hoặc Nội Dung Đề Xuất

### Nội dung/workflow cần tạo

| Hạng mục | Định dạng | Nền tảng | Ghi chú |
| --- | --- | --- | --- |
| <tên> | <post/script/checklist/carousel/...> | <Facebook/Zalo/...> | <ghi chú> |

### File mới cần tạo

| Đường dẫn | Mục đích |
| --- | --- |
| `path/to/file.md` | <mục đích> |

### File cần chỉnh sửa

| Đường dẫn | Nội dung thay đổi |
| --- | --- |
| `path/to/file.md` | <mô tả> |

## Quyết Định Nội Dung

- **Voice:** Chuyên Gia Xây Nhà, thẳng, thật, dễ hiểu.
- **Tệp khách hàng và góc viết:** <vì sao chọn tệp này>
- **CTA:** <CTA mềm dự kiến>
- **Điều không được bịa:** <giá/case/chính sách/vật tư/...>
- **Visual:** <ảnh công trình/infographic/carousel/không dùng>

## Các Bước Thực Hiện

1. <bước cụ thể>
2. <bước cụ thể>
3. <bước cụ thể>

## Checklist Kiểm Tra

- [ ] Đã đối chiếu `AKV-content.md`.
- [ ] Đã chọn tệp khách hàng cụ thể, không viết chung chung.
- [ ] Không có dữ kiện bị bịa.
- [ ] Mỗi bài có hook, nỗi đau, lời khuyên cụ thể, CTA mềm.
- [ ] Format lưu trữ đúng chuẩn `posts/README.md`.
- [ ] Dashboard build được nếu có post mới.

## Tiêu Chí Thành Công

1. <tiêu chí đo được>
2. <tiêu chí đo được>
3. <tiêu chí đo được>

## Câu Hỏi Mở

<Nếu không có, ghi “Không có”.>
```

## Báo Cáo Sau Khi Tạo Plan

Nêu ngắn gọn:

- Kế hoạch đã bao gồm gì.
- Câu hỏi mở còn lại.
- Full path tới file plan.
- Lệnh `/implement plans/YYYY-MM-DD-{name}.md` để thực thi khi sẵn sàng.
