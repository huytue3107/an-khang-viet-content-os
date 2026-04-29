# Triển Khai — An Khang Việt Content OS

Thực thi một kế hoạch đã tạo bởi `/create-plan`.

## Biến Đầu Vào

`plan_path: $ARGUMENTS`

## Giai Đoạn 1: Hiểu Kế Hoạch

1. Đọc toàn bộ file plan.
2. Kiểm tra trạng thái plan phải là `Draft` hoặc `Ready`.
3. Đọc `AKV-content.md`, `CLAUDE.md` và context liên quan.
4. Kiểm tra “Câu hỏi mở”. Nếu còn câu hỏi làm thay đổi nội dung hoặc dữ kiện, dừng lại và hỏi user.
5. Xác định file sẽ tạo/sửa/xóa, tránh chạm file ngoài scope.

## Giai Đoạn 2: Thực Thi

Làm đúng thứ tự trong plan. Với mỗi hạng mục:

- Nếu tạo post, dùng chuẩn `posts/README.md`.
- Nếu tạo carousel, tạo `content.json` đúng schema và dùng tiếng Việt có dấu.
- Nếu tạo visual tốn API, chỉ làm khi kế hoạch hoặc user đã duyệt text.
- Nếu thiếu dữ kiện thật về giá/case/vật tư/chính sách, ghi placeholder cần user bổ sung hoặc viết ở mức nguyên tắc, không tự bịa.
- Nếu chỉnh workflow, cập nhật `CLAUDE.md` hoặc README liên quan nếu cấu trúc thay đổi.

## Giai Đoạn 3: Kiểm Tra Voice

Mỗi nội dung hoàn chỉnh phải qua checklist:

- Hook có rõ và chạm nỗi đau không?
- Có đúng nhóm chủ nhà mục tiêu không?
- Có phân tích bản chất vấn đề không?
- Có checklist/câu hỏi/lời khuyên cụ thể không?
- CTA có mềm, không ép inbox không?
- Có câu nào quảng cáo lố hoặc cam kết vô căn cứ không?
- Có dữ kiện nào bị bịa không?

## Giai Đoạn 4: Kiểm Tra Kỹ Thuật

- Chạy `python scripts/build-dashboard.py` nếu có post mới hoặc cập nhật post.
- Với carousel, chạy `python scripts/generate-carousel.py --json <content.json> --output <carousel.pdf>`.
- Kiểm tra tiếng Việt có dấu trong file output.
- Rà lại file đã thay đổi bằng `git diff`.

## Giai Đoạn 5: Cập Nhật Plan

Sau khi hoàn tất, cập nhật file plan:

```markdown
**Trạng thái:** Implemented

---

## Implementation Notes

**Implemented:** <YYYY-MM-DD>

### Summary

<Tóm tắt ngắn>

### Deviations from Plan

<Liệt kê hoặc “Không có”>

### Issues Encountered

<Liệt kê hoặc “Không có”>
```

## Báo Cáo Cuối

Báo cáo:

1. Tóm tắt phần đã làm.
2. File đã tạo/sửa/xóa.
3. Kết quả kiểm tra.
4. Điểm lệch so với plan.
5. Việc cần user bổ sung nếu có dữ kiện còn thiếu.
