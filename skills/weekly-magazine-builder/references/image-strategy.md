# Image strategy — SVG illustrations + AI hero photographs

A magazine without good imagery looks like a blog. A magazine with bad imagery (stock photos, generic AI slop) looks worse than no imagery. Every image must be doing real editorial work.

## Two acceptable image types

### Type 1 — SVG editorial illustrations (preferred)

One per deep article. Drawn fresh per article. Conceptually distinct.

**SVG illustrations are best for:**
- Timelines (years on x-axis, milestones as dots/labels)
- Comparison diagrams (before/after, A vs B)
- Technical schemas (architecture, data flow, system layout)
- Data visualizations (charts, plots, geographic data)
- Conceptual abstractions (multimodal converging, taxonomy, hierarchy)

**SVG concept patterns (use as starting points):**

```
1. Horizontal milestone timeline
   - axis line at y=center
   - 4-7 milestone circles
   - one milestone styled differently (red filled) as visual climax
   - labels above circles, dates below

2. Before / after split panel
   - vertical divider line, dashed
   - left panel = "BEFORE", right = "AFTER"
   - same visual element rendered two ways

3. Layered architecture stack
   - 4-6 horizontal strips, stacked vertically
   - each strip = one architectural layer
   - bottom strip = brand color (foundation), top strip = lightest
   - right-side annotations describing each layer

4. Concentric pyramid of specialization
   - widest base at bottom (most generic)
   - narrowing toward top (most specific)
   - each level labeled with example (CPU → GPU → NPU → ASIC)

5. Side-by-side flow comparison
   - top row: traditional flow with multiple steps
   - bottom row: new flow compressed into fewer steps
   - both aligned to same time axis

6. Constellation / network
   - several nodes at varying positions
   - edges drawn between meaningful pairs
   - one focal node highlighted

7. Sector breakdown (4-quadrant or radial)
   - 4 industries / categories / segments
   - each with size proportional to weight
```

**SVG style consistency rules across the magazine:**

- viewBox typically `960×280` to `960×420` (16:9 to 12:5 aspect)
- Background: transparent (rendered on `paper-1` or `paper-0` in light reading mode)
- Stroke widths: 0.5px for hairlines, 0.75px for emphasis, 1.5px max
- Colors: use design tokens — `#1F1F2B` (ink), `#6B6B76` (gray), `#E60012` (accent)
- Typography in SVG: `Fraunces` for serif numbers/titles, `JetBrains Mono` for axis labels, `Inter` for sans labels
- Always include `<title>` and `<desc>` for accessibility
- One red highlight per illustration — the visual climax
- Always end with credit text: `制图 · [Magazine] 编辑部 · YYYY.MM.DD`

### Type 2 — AI-generated hero photographs

Used sparingly. Maximum 2-3 per issue total. For:
- The deep article's hero image (full-bleed photographic moment)
- Section 5 in the deep article (an in-text editorial photograph)
- Cover background atmosphere (low opacity, behind the motif)

**Generation tools (in order of quality for editorial use):**
1. GPT Image / DALL-E with the right prompt
2. Flux Pro 1.1 (excellent texture, photographic feel)
3. Midjourney (most artistic, harder to control consistency)

**Prompt template for editorial photography:**

```
Editorial magazine photography of [SUBJECT].
[Specific composition direction: extreme close-up / cinematic wide /
 architectural mid-shot]. 
[Lighting: dramatic side-light / moody dim / natural diffused]. 
[Mood: contemplative, clinical, beautiful / industrial, somber / 
 hopeful, soft].
Editorial magazine photography, [grain texture / 8K sharpness / 
 soft focus]. 
[Aspect ratio: 21:9 cinematic / 16:9 / 4:3 portrait]. 
Minimal negative space on [LEFT/RIGHT] for text overlay. 
No text, no logos, no people's faces visible.
```

**Critical exclusions in every AI prompt:**
- "No text" (AI text generation is unreliable)
- "No people's faces" if the article touches on real-world identity-sensitive scenarios (refugees, crime victims, political figures)
- "No logos" (avoid trademark issues)

**Subjects that are appropriate for AI generation:**
- Abstract concepts (light, particles, networks)
- Product / object close-ups (devices, instruments, tools — without specific brand identification)
- Scenic atmosphere (architecture, landscapes, natural phenomena)
- Generic technology contexts (server rooms, lab benches, industrial scenes)

**Subjects that require care or avoidance:**
- Real people (especially recognizable figures — never)
- Specific cultural or political scenes (refugees, war zones, protests — be very thoughtful; consider abstract substitution instead)
- Anything that could pass as "real journalism photography" of a real event (creates misinformation risk)

When in doubt, pick a metaphorical / abstract substitute. For an article on refugee biometrics, an iris scanner device close-up is editorially honest; an AI-generated refugee portrait is editorial dishonesty.

### What NEVER to use

- **Stock photos**. Even good ones cheapen the magazine instantly. Readers' eyes recognize the look.
- **Same hero image repeated across issues**. Each issue gets fresh imagery.
- **Decorative emoji or icons inline**. Editorial body is text + custom illustrations only.
- **Generic AI illustrations** ("vector style abstract concept") without specific editorial intent.

## Image processing pipeline

The file `tools/process_images.py` (~140 lines, Python + Pillow) handles raw PNG → web-optimized.

Workflow:
1. User generates raw images at 1500×800+ resolution, drops into `site/assets/img/ISSUE/`
2. Run `python3 tools/process_images.py ISSUE`
3. Script applies editorial filter (slight desaturation -15%, contrast +8%, brightness -3%) for unified magazine feel
4. Outputs: `slug-2x.webp` (1920w), `slug-2x.jpg` (1920w fallback), `slug-1x.webp` (960w mobile)
5. Originals moved to `_raw/` for archive; deploy script excludes `_raw/`

Typical compression results: 4.5MB raw PNG → 350KB optimized WebP, equivalent visual quality.

## Editorial filter — why every image gets the same treatment

A magazine has visual unity. If image A is from Midjourney with high saturation, image B is from Flux Pro with cool tones, and image C is a stock photograph, the issue feels disjointed. The filter ensures all three look like they came from the same publication.

Default filter parameters (the `editorial_treatment()` function):
- Color saturation × 0.85 (-15%)
- Contrast × 1.08 (+8%)
- Brightness × 0.97 (-3%)

These values are mild — viewer doesn't notice the filter, but the resulting unity is felt. For a more dramatic look, push saturation to 0.7 (more grayscale). For warmer feel, add a slight color balance shift toward warm tones.

## When the user says "I want a photo of X"

Walk them through the decision:

1. Is X actually photographable in real life by someone you'd hire?
   - Yes → consider commissioning real photography (best quality if budget allows)
   - No → AI generation candidate
2. If AI generation: write the prompt yourself (don't let user prompt directly — they'll under-specify), generate 3-4 variants, pick the best, run through editorial filter
3. If the article doesn't actually need a photo (it could be served by an SVG illustration), default to SVG. SVGs are infinitely cheaper and stay relevant longer.

The default ratio to aim for: **80% SVG illustrations, 20% AI hero photography**. An issue heavy on SVG looks more editorial; one heavy on photography looks more lifestyle. Most B2B / technical magazines should stay closer to 80/20.
