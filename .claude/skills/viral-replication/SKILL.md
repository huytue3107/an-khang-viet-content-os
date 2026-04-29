---
name: viral-replication
description: Adapt proven content packaging into An Khang Việt Content while replacing the substance with owner-focused house building, renovation, quotation, design, contractor, and construction-risk insights. Use when asked to replicate a post, copy a format, adapt a viral structure, or borrow packaging.
---

# Viral Packaging Adaptation — An Khang Việt

This skill keeps the useful part of a proven post: packaging, hook mechanics, structure, visual hierarchy, CTA rhythm. It does **not** copy the original substance or voice.

The final output must follow `AKV-content.md` and sound like **Chuyên Gia Xây Nhà**.

## Required Context

Read:

1. `AKV-content.md`
2. `context/brand-dna.md`
3. `context/voice-analysis.md`
4. `context/icp.md`
5. `context/strategy.md`

## What To Borrow

- Hook pattern, not exact unrelated wording.
- Body flow: warning, list, framework, story arc, comparison, checklist.
- Visual structure: central headline, numbered list, before/after, radial checklist, flow.
- CTA mechanic: save, comment, inbox, share, but rewritten softly for AKV.

## What To Replace

- Topic becomes AKV domain: xây nhà, sửa nhà, báo giá, hợp đồng, vật tư, công năng, nhà thầu, nghiệm thu.
- Voice becomes Chuyên Gia Xây Nhà: thẳng, thật, mộc mạc, có nghề, có tâm.
- Examples become owner-safe and non-fabricated.
- CTA becomes soft: lưu bài, inbox tư vấn bước đầu, gửi báo giá/bản vẽ để xem điểm cần kiểm tra.

## Step 1: Analyze Packaging

Document:

```markdown
## Packaging Analysis

- Original hook pattern:
- Body structure:
- Visual structure:
- CTA mechanic:
- Why it worked:
- AKV-safe adaptation:
```

## Step 2: Choose AKV Angle

Pick one:

- Kinh nghiệm xây nhà.
- Cảnh báo rủi ro.
- Tư duy thiết kế nhà đáng sống.
- Quy trình An Khang Việt.
- Case/bài học thực tế, only if data exists.

Define:

- Target owner group.
- Specific AKV customer segment from the 8-segment matrix.
- Specific fear/pain.
- Practical payload.
- Boundary: what data must not be invented.

## Step 3: Write Post Text

Use the AKV formula:

```text
Hook thẳng
Nỗi đau thật
Bóc bản chất vấn đề
Ví dụ đời thường hoặc tình huống không định danh
Lời khuyên/cách kiểm tra cụ thể
Câu chốt nhớ lâu
CTA mềm
```

Requirements:

- Keep the post useful without needing the reader to comment or inbox.
- Make the hook fit the chosen customer segment. A high-end villa owner, a first-time young family, and a rental investor do not buy the same thing.
- If asking for inbox, make it a natural next step for a personal case.
- No fake numbers, fake projects, fake quotes, fake policies.
- No corporate slogans.

## Step 4: Visual Adaptation

If adapting a visual, keep the information architecture but use AKV style:

- Light neutral background.
- Đỏ An Khang, Cam Phát Triển, Nâu Mái Nhà, Vàng Ánh Sáng used with restraint.
- Construction and brand cues: A roof shape, 3 slanted orange-red lines, window square, grid, blueprint line, ruler, material blocks, checklist marks.
- Vietnamese text with exact diacritics.
- Bottom or corner brand mark: “AN KHANG VIỆT”.

For infographic:

```powershell
python scripts/generate-infographic.py --reference reference/infographic-ref-1.jpeg --output posts/NNN-slug/image.png --prompt "<prompt AKV tiếng Việt có dấu>"
```

This uses OpenRouter with default model `google/gemini-3.1-flash-image-preview`. Do not use older image providers.

For carousel:

```powershell
python scripts/generate-carousel.py --json posts/NNN-slug/content.json --output posts/NNN-slug/carousel.pdf
```

## Step 5: Save Output

Use:

```text
posts/NNN-slug/
  post.md
  image.png or carousel.pdf
  content.json if carousel
  original.md if source text is available
  original-image.jpg if source image is available
```

`post.md` must include `Voice Check`.

## Anti-Patterns

- Copying a creator’s personal story and pretending it is AKV’s.
- Keeping a voice that sounds unrelated to construction.
- Adding fake project details to make the post feel “real”.
- Making the hook clever but not useful.
- Using visual text without Vietnamese diacritics.
- Turning an educational post into a hard sales pitch.
