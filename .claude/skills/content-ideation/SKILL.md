---
name: content-ideation
description: Generate content ideas for An Khang Việt Content using the AKV master style guide, five content pillars, owner pain points, and soft conversion goals. Use when asked to brainstorm topics, create content ideas, plan a series, or find post angles for house building, renovation, contractor selection, design, quotation, contracts, or construction risks.
---

# Content Ideation — An Khang Việt

Generate ideas that fit `AKV-content.md` and the voice **Chuyên Gia Xây Nhà**.

## Required Context

Read before ideating:

1. `AKV-content.md`
2. `context/icp.md`
3. `context/strategy.md`
4. `context/voice-analysis.md`
5. Recent files in `posts/` if any

## Core Rule

An idea is only useful if it can become content a chủ nhà would save, send to family, comment on, or inbox about. Avoid generic topic labels like “thiết kế nhà đẹp”; turn them into concrete tensions, mistakes, checklists, or decisions.

## Customer Segment Rule

Every idea must name one of the 8 AKV customer segments:

1. Gia đình trẻ Gen Y/Gen Z xây căn nhà đầu tiên.
2. Người đang tìm thiết kế và thi công trọn gói.
3. Chủ biệt thự/nhà phố cao cấp.
4. Chủ nhà cải tạo nhà cũ.
5. Nhà đầu tư bất động sản/cho thuê/homestay.
6. Khách smarthome/nhà xanh.
7. Gia đình nhiều thế hệ.
8. Người nâng cấp phong cách sống.

If the user does not specify a segment, infer it from topic and goal. Record the assumption in the idea output.

## Idea Sources

### 1. Kinh Nghiệm Xây Nhà

Use when the goal is education and saves.

Angles:

- What to prepare before building.
- How to read a quotation.
- What to ask before signing.
- Costs and items owners often forget.
- Mistakes first-time builders make.

Output idea as:

```text
### [Title]
- Trụ cột: Kinh nghiệm xây nhà
- Tệp khách hàng: [one of 8 AKV segments]
- Nỗi đau: "[their words]"
- Hook: "[first 1-2 lines]"
- Format: [post/checklist/script/carousel]
- Advice payload: [what useful checklist/framework the post gives]
- CTA: [soft CTA]
```

### 2. Cảnh Báo Rủi Ro

Use when the goal is comments, shares, and inbox from worried owners.

Angles:

- Cheap but vague quotes.
- Swapped materials.
- Scope not written clearly.
- Unclear variation costs.
- No site supervision.
- Weak warranty responsibility.
- “Anh cứ yên tâm” without written terms.

Output idea as:

```text
### [Title]
- Trụ cột: Cảnh báo rủi ro
- Tệp khách hàng: [one of 8 AKV segments]
- Risk: [specific risk]
- Hook: "[direct warning]"
- Why it matters: [practical consequence]
- Check method: [what owner should ask/check]
- Format: [post/script/checklist]
- CTA: [save/inbox/check quotation]
```

### 3. Tư Duy Thiết Kế Nhà Đáng Sống

Use when the goal is upgrading perception from “pretty house” to “livable house”.

Angles:

- Function over decor.
- Light and ventilation.
- Storage.
- Kitchen workflow.
- Hot bedrooms.
- Smell-prone bathrooms.
- Multi-generation homes.

Output idea as:

```text
### [Title]
- Trụ cột: Tư duy thiết kế nhà đáng sống
- Tệp khách hàng: [one of 8 AKV segments]
- Misbelief: [what owners often think]
- Better frame: [what AKV wants them to understand]
- Hook: "[contrarian/livable-house hook]"
- Practical takeaway: [what they can check at home/design stage]
- Format: [post/carousel/script]
- CTA: [soft CTA]
```

### 4. Quy Trình An Khang Việt

Use when the goal is trust and conversion.

Only use verified process details if provided. If no detailed process exists, stay at principle level: consult clearly, design clearly, quote clearly, build and inspect clearly.

Output idea as:

```text
### [Title]
- Trụ cột: Quy trình An Khang Việt
- Tệp khách hàng: [one of 8 AKV segments]
- Trust point: [clarity/transparency/supervision/warranty]
- Hook: "[process-oriented hook]"
- What to explain: [specific process or principle]
- Boundary: [what must not be claimed without data]
- Format: [soft sales post/script/inbox follow-up]
- CTA: [book consultation/inbox first review]
```

### 5. Case Study / Công Trình Thực Tế

Use only when the user provides real case details. Without real case details, convert to “bài học thường gặp” and avoid names, locations, prices, or exact outcomes.

Output idea as:

```text
### [Title]
- Trụ cột: Case study/công trình thực tế
- Tệp khách hàng: [one of 8 AKV segments]
- Case data available: [yes/no]
- Owner problem: [given or generic]
- Lesson: [what readers learn]
- Hook: "[situation hook]"
- Format: [case post/carousel/script]
- CTA: [ask about similar case]
```

## Batch Split

For N ideas, default split:

- 40% Kinh nghiệm xây nhà.
- 25% Cảnh báo rủi ro.
- 15% Case/bài học thực tế.
- 10% Quy trình/thương hiệu.
- 10% Bán hàng mềm.

If no case data is available, replace case ideas with “bài học thực tế thường gặp” and mark them clearly.

For a batch of 10 ideas, cover at least 5 customer segments unless the user asks for a narrow campaign.

## Goal-To-Segment Defaults

- **Tạo tin tưởng:** first-time builders, design-build shoppers, renovation owners.
- **Tạo lưu bài:** first-time builders, renovation owners, multi-generation families, smarthome/green-home customers.
- **Muốn inbox:** quote-comparing owners, first-time builders, high-end homeowners, property investors.
- **Tạo tranh luận:** young design-minded owners, design-build shoppers, rental investors, smarthome fans.

## Hook Requirements

Rotate hook types:

- Direct warning: “Đừng…”
- Misbelief correction: “Nhiều chủ nhà nghĩ…, nhưng…”
- Saveable checklist: “Trước khi…, kiểm tra…”
- Debate: “Chủ nhà càng…, công trình càng…”
- Livable-house insight: “Nhà đẹp mà… thì…”

## Output File

Save idea sets to:

```text
outputs/YYYY-MM-DD-akv-content-ideas.md
```

Use this structure:

```markdown
# Ý Tưởng Nội Dung AKV — YYYY-MM-DD

**Tổng số:** N
**Nguồn:** AKV-content.md

## Kinh Nghiệm Xây Nhà

[ideas]

## Cảnh Báo Rủi Ro

[ideas]

## Tư Duy Thiết Kế Nhà Đáng Sống

[ideas]

## Quy Trình An Khang Việt

[ideas]

## Case/Bài Học Thực Tế

[ideas]

## Top Ưu Tiên

[ranked top ideas and why]
```

## Quality Filter

Reject ideas that:

- Require fake price, fake case, fake warranty, or fake project details.
- Are only a broad topic with no owner pain.
- Do not name a specific customer segment.
- Sound like a sales brochure.
- Do not offer a check, lesson, or practical action.
- Repeat a recent narrow topic.
