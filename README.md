# An Khang Việt Content OS

Workspace này dùng để lập kế hoạch, viết, lưu trữ và kiểm tra nội dung cho **An Khang Việt Content**. Nguồn sự thật chính là `AKV-content.md`, bộ style guide định nghĩa văn phong **Chuyên Gia Xây Nhà**.

Mục tiêu của hệ thống không phải viết bài cho có. Mỗi nội dung phải giúp chủ nhà hiểu rõ hơn trước khi xây, sửa, thiết kế hoặc chọn nhà thầu: rõ chi phí, rõ vật tư, rõ quy trình, đỡ mệt về sau.

## Nguyên Tắc Lõi

- Luôn đọc `AKV-content.md` trước khi viết nội dung mới hoặc tạo campaign.
- Viết như một chuyên gia tư vấn thiết kế và xây nhà trọn gói: thẳng, thật, có nghề, có tâm, dễ hiểu.
- Không bịa báo giá, số liệu, chính sách, cam kết, case study hoặc chi tiết kỹ thuật nếu brief không cung cấp.
- Ưu tiên giá trị thực tế: checklist, câu hỏi cần hỏi nhà thầu, cách kiểm tra báo giá, rủi ro cần tránh, lời khuyên áp dụng được.
- CTA phải mềm: lưu bài, inbox tư vấn bước đầu, gửi bản vẽ/báo giá để được xem các điểm cần kiểm tra.

## Quick Start

```powershell
# Nạp bối cảnh workspace trong một session mới
/prime

# Lập kế hoạch campaign hoặc workflow nội dung
/create-plan chuỗi 14 bài về lỗi xây nhà lần đầu

# Tạo batch 10 nội dung theo chuẩn AKV
/create-10-posts
```

Nếu tạo visual bằng Kie.ai, cần cấu hình:

```powershell
Copy-Item .env.example .env
# Điền KIE_AI_API_KEY vào .env
```

## Workspace Structure

```text
.
├── AKV-content.md          # Master style guide, không rút gọn hoặc ghi đè
├── CLAUDE.md               # Hướng dẫn vận hành cốt lõi cho AI trong repo
├── .claude/
│   ├── commands/           # Workflow: prime, create-plan, implement, create-10-posts
│   └── skills/             # Ideation, viral packaging, carousel theo chuẩn AKV
├── context/                # Bối cảnh thương hiệu, ICP, chiến lược, voice, metrics
├── posts/                  # Nội dung cuối cùng, mỗi bài một thư mục NNN-slug
├── outputs/                # Dashboard, draft, idea bank, batch plan
├── reference/              # Visual refs, tư liệu phụ, ví dụ tham khảo
├── scripts/                # Dashboard, carousel, infographic, photo overlay
└── plans/                  # Kế hoạch triển khai campaign/workflow
```

## Content Pillars

1. **Kinh nghiệm xây nhà** — checklist, chuẩn bị ngân sách, đọc báo giá, chọn nhà thầu.
2. **Cảnh báo rủi ro** — báo giá mập mờ, phát sinh, tráo vật tư, bán thầu, hợp đồng sơ sài.
3. **Tư duy thiết kế nhà đáng sống** — công năng, ánh sáng, thông gió, lưu trữ, thói quen sinh hoạt.
4. **Quy trình An Khang Việt** — tư vấn, thiết kế, báo giá, thi công, nghiệm thu, bảo hành.
5. **Case study/công trình thực tế** — bài toán của chủ nhà, giải pháp, điểm khó, bài học rút ra. Chỉ dùng khi có dữ kiện thật.

## Customer Scenario Matrix

Bản `AKV-content.md` mới mở rộng hệ khách hàng thành 8 tệp. Khi viết hoặc lập kế hoạch, phải chọn tệp cụ thể thay vì viết chung chung cho “chủ nhà”:

1. Gia đình trẻ Gen Y/Gen Z xây căn nhà đầu tiên.
2. Người đang tìm đơn vị thiết kế và thi công trọn gói.
3. Chủ nhà trung lưu/thượng lưu sở hữu biệt thự, nhà phố cao cấp.
4. Chủ nhà sửa chữa, cải tạo nhà cũ trong đô thị.
5. Nhà đầu tư bất động sản, căn hộ cho thuê, homestay, nhà phố khai thác dòng tiền.
6. Khách quan tâm smarthome, nhà xanh, tiết kiệm năng lượng.
7. Gia đình nhiều thế hệ xây nhà để ở lâu dài.
8. Người nâng cấp phong cách sống, thích nhà đẹp, có gu, muốn cá nhân hóa.

Mỗi tệp có nỗi đau, thứ họ thật sự muốn mua, tuyến nội dung và CTA riêng. Nếu brief không nói rõ tệp, AI phải suy luận theo chủ đề/mục tiêu và ghi lại giả định trong `Voice Check`.

## Post Format

Mỗi bài nằm trong `posts/NNN-slug/post.md`:

```markdown
# Bài NNN: Tiêu Đề

**Ngày tạo:** YYYY-MM-DD
**Nền tảng:** Facebook / TikTok-Reels / Zalo / Website / Email-Inbox
**Định dạng:** Bài post / Caption ngắn / Script video / Checklist / Carousel / Bài bán hàng mềm
**Trụ cột AKV:** Kinh nghiệm xây nhà / Cảnh báo rủi ro / Tư duy thiết kế / Quy trình AKV / Case study
**Tệp khách hàng:** [Một trong 8 tệp ở Customer Scenario Matrix]
**Mục tiêu:** Tạo niềm tin / Tăng inbox / Tăng lưu bài / Giáo dục thị trường / Tạo tranh luận
**Visual:** Ảnh công trình / AI Infographic / Carousel / Không dùng
**Trạng thái:** Draft / Ready to publish

---

## Post Text

[Nội dung plain text, copy-paste ready]

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

[Mô tả visual hoặc prompt tạo ảnh]
```

## Visual Workflow

- Infographic dùng `scripts/generate-infographic.py`, prompt tiếng Việt có dấu và style AKV.
- Carousel dùng `scripts/generate-carousel.py`, schema `content.json` gồm `title`, `title_emphasis`, `slides`, `cta_text`, `cta_subtitle`.
- Dashboard dùng `scripts/build-dashboard.py`, output tại `outputs/dashboard.html`.
- Không generate ảnh tốn API trước khi nội dung text đã đủ chắc.

## Quality Bar

Trước khi coi một bài là xong, kiểm tra:

- Hook có chạm đúng nỗi lo chủ nhà không?
- Nội dung có nói rõ bản chất vấn đề không?
- Có checklist, câu hỏi kiểm tra hoặc lời khuyên cụ thể không?
- Có câu nào sáo rỗng kiểu “uy tín hàng đầu”, “chất lượng số 1”, “giá tốt nhất” không?
- Có bịa báo giá, case, cam kết hoặc chính sách không?
- CTA có tự nhiên, không ép inbox không?
