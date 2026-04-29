---
name: carousel-creation
description: Create An Khang Việt carousel/checklist content for house building, renovation, design, quotations, contracts, contractor selection, and construction risk education. Use when the user asks for carousel, slides, swipe post, checklist PDF, or multi-slide content.
---

# Carousel Creation — An Khang Việt

Create carousels that homeowners can save and re-read before building, renovating, signing a contract, or comparing quotes.

## Required Context

Read:

1. `AKV-content.md`
2. `context/voice-analysis.md`
3. `context/strategy.md`

## Best Carousel Topics

- 5-9 điều cần kiểm tra trước khi ký hợp đồng.
- Cách đọc một báo giá xây nhà.
- Dấu hiệu báo giá mập mờ.
- Những lỗi xây nhà lần đầu.
- Nhà đẹp chưa chắc đã đáng sống.
- Câu hỏi phải hỏi nhà thầu.
- Các bước làm rõ nhu cầu trước khi thiết kế.
- Checklist cải tạo nhà cũ trước khi đập sửa.
- Smarthome vừa đủ: những điểm nên tính từ lúc thiết kế.
- Nhà nhiều thế hệ: an toàn, chung riêng, thói quen sống.
- Nội thất cho thuê: đẹp phải đi cùng độ bền và hoàn vốn.

## Segment Fit

Before writing slides, pick one customer segment:

- First-time young family: simplify, guide, focus on budget and avoiding mistakes.
- Design-build shopper: compare responsibility, quote clarity, contract, supervision.
- High-end homeowner: speak about hidden quality, execution detail, privacy, long-term value.
- Renovation owner: diagnose old-house problems before making it pretty.
- Property investor: connect design decisions to operation, maintenance, and cash flow.
- Smarthome/green-home customer: technology after real habits, energy savings from design first.
- Multi-generation family: safety, harmony, shared/private space.
- Lifestyle upgrader: personal taste with function and restraint.

## Slide Structure

Recommended 7-11 slides:

1. Cover: hook mạnh, saveable.
2. Context slide: vì sao chủ nhà dễ sai.
3. Point slides: one check/lesson per slide.
4. Warning slide: lỗi hay gặp hoặc hậu quả.
5. CTA slide: lưu bài/inbox tư vấn bước đầu.

Each content slide should include:

- Heading: ngắn, rõ.
- Subtitle: giải thích bằng ngôn ngữ đời thường.
- Takeaway: câu chốt đáng nhớ.

## JSON Schema

Use UTF-8 and keep Vietnamese diacritics:

```json
{
  "title": "7 điều cần kiểm tra trước khi ký hợp đồng xây nhà",
  "title_emphasis": "7 điều",
  "slides": [
    {
      "number": 1,
      "heading": "Phạm vi công việc",
      "subtitle": "Hợp đồng phải ghi rõ bên thi công làm những hạng mục nào và không làm hạng mục nào.",
      "takeaway": "Cái gì không ghi rõ hôm nay, rất dễ thành phát sinh ngày mai."
    }
  ],
  "cta_text": "Lưu lại trước khi làm việc với nhà thầu.",
  "cta_subtitle": "Nếu đang có báo giá hoặc bản vẽ còn lăn tăn, inbox An Khang Việt để được gợi ý điểm cần kiểm tra."
}
```

## Generate

```powershell
python scripts/generate-carousel.py --json posts/NNN-slug/content.json --output posts/NNN-slug/carousel.pdf
```

The script also saves slide PNGs for dashboard preview.

## Post Caption

Caption should not duplicate every slide word-for-word. It should:

- Open with the same pain.
- Preview 3-5 key checks.
- Add one practical warning.
- End with soft CTA.

## Visual Style

Default AKV style:

- Light neutral background.
- Dark green and earth-gold accents.
- Clean typography, high contrast.
- Minimal construction-inspired geometry: grids, dots, ruler lines, blueprint cues.
- No neon, no luxury cliché, no overdecorated real estate look.

## Quality Checklist

- Cover slide is clear enough to save.
- Each slide teaches one thing only.
- No fake data.
- Segment is explicit and the slide examples fit that segment.
- No hard sales language.
- CTA is soft and useful.
- Text is legible and fits.
- Vietnamese diacritics render correctly.
