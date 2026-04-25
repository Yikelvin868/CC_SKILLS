---
name: weekly-magazine-builder
description: Design and build a beautiful, magazine-grade weekly electronic publication from scratch. Use this skill whenever the user wants to create, systematize, or refresh a digital weekly magazine, electronic journal, e-weekly (电子周刊 / 电子杂志 / 电子刊物), online magazine, recurring company publication, or any periodical with brand identity, multiple columns, and depth-first reading architecture. Triggers on phrases like "做一份周刊", "电子杂志", "magazine project", "weekly publication", "build me a digital magazine", "newsletter with depth", "出版物", or when the conversation involves designing a recurring content product. Strongly favor this skill whenever a user wants something more substantial than a blog post or social-media schedule — anything that should look like an editorial property.
---

# Weekly Magazine Builder

A playbook for designing and building a publication that feels like a magazine, not a blog. Distilled from building 《识界 · THE SPECTRUM》— HOMSH's iris recognition & AI weekly.

The job is bigger than "set up a website with articles." A magazine has a **point of view, a visual identity, an architecture, and a rhythm**. This skill walks through eight phases that together produce something a reader is willing to spend 30 minutes inside every week.

## Core principles

**Magazine, not blog.** The default content model on the web is reverse-chronological posts. A magazine is the opposite — issues, not posts; columns, not categories; depth, not feed scroll.

**Layered architecture.** Every issue exposes two layers: a magazine index page (10 columns, scannable, ~5 min) and individual depth pages (one per major story, 4500-6000 chars each). Readers self-select their depth.

**Visual identity is a system, not a logo.** A magazine needs a motif (a generative visual concept that appears across covers, dividers, page furniture), a typography stack (display serif + body serif + sans + mono), a color system, and animation principles.

**Editorial writing > marketing writing.** Even when the publisher is a company, the writing must read like a magazine — flowing prose, no bullet lists, no callout boxes, no marketing speak. MIT Technology Review is the reference standard.

**Image as illustration, not decoration.** One custom illustration per article, conceptually distinct, doing actual editorial work — not stock photos and not AI-slop fillers.

## The eight phases

Run them roughly in order, but iterate freely. Phase 1 is the most important — bad decisions here compound into wasted work later.

### Phase 1 — Brainstorming and decisions

Before writing a single line of code, run the user through a structured question funnel. This is not optional. The decisions made here shape every following phase. Use the question funnel in `references/question-funnel.md` — it covers audience, format, brand, length, language, columns, byline, frequency, and review process.

**Critical decisions to lock down:**
- **Magazine name + subtitle** (Chinese name + English subtitle is a strong default for Chinese publishers)
- **Visual direction** — Tech Brutalism / Editorial Magazine / Smart Digest, or hybrid (see `references/visual-directions.md`)
- **Visual motif** — the recurring generative concept that appears throughout (e.g., iris for HOMSH; could be a lens, a wave, a constellation for other brands)
- **Reading length target** (30 minutes is a strong default — long enough to be substantial, short enough to fit a Friday afternoon)
- **Column architecture** (10 columns is the proven structure, see Phase 3)
- **Hosting platform** — Tencent COS for China audiences, Cloudflare Pages / Vercel / Netlify for global

The user will rarely have all answers ready. Surface trade-offs, give recommendations, get explicit yes/no on each before moving on.

### Phase 2 — Design system construction

Build the CSS foundation first. Don't write any page HTML before tokens exist.

Three CSS files in this order:
1. `tokens.css` — design tokens (colors, fonts, spacing, animations, layout widths)
2. `main.css` — global components (masthead, buttons, cards, footer, typography)
3. `issue.css` — issue-page specific (cover, TOC, chapter openers, deep article reading mode)

The full token template with rationale is in `references/design-system.md`. Use it verbatim, change only the brand color and font choices for the project at hand.

Key principles to get right early:
- **Two themes coexisting** — `[data-theme="dark"]` for covers and section openers, `[data-theme="light"]` for long-form reading. The transition between them is part of the editorial rhythm.
- **Custom easing curves** — never use browser defaults. The "magazine feel" partly comes from confident, slightly-slow transitions.
- **Type stack with real fallbacks** — `Fraunces` / `Spectral` / `Inter` / `Noto Serif SC` / `JetBrains Mono` is a strong starting set. Load via `fonts.loli.net` for China-friendly delivery.

### Phase 3 — Content architecture: the ten columns

Every issue has the same ten columns. Stable structure → reader habit → magazine identity.

```
01 卷首语 / Editor's Note      — 编辑部本周视角
02 本期速览 / The Brief         — 5 条关键信号，扫一眼
03 公司动态 / Inside [Brand]    — 自家这一周
04 技术前沿 / Tech Radar         — 论文 / 新工程
05 深度一文 / Deep Dive          — 本期主打 4500-6000 字
06 行业观察 / Industry Watch     — 政策 / 市场 / 监管
07 AI 速递 / AI Pulse            — 短动态
08 数据一瞥 / By the Numbers     — 一组关键数字
09 识者之言 / Voices             — 一句话
10 下期预告 / Next Week          — 钩子 + 编辑部署名
```

Customization rules: the names can change to fit the brand voice, but the **functional slots** should not — each fills a different reader need. See `references/column-architecture.md` for the rationale of each slot, plus rules on what content belongs where.

### Phase 4 — Writing standards (MIT Technology Review style)

This is the single hardest part to get right. Most company writing defaults to marketing tone — which kills magazine credibility instantly.

The rules are absolute. They are listed in detail in `references/writing-style.md`, but the essentials:

- **No bullet lists, no numbered lists, no tables, no callout boxes inside article body.** Footer navigation is fine. Article body must be flowing prose.
- **Drop cap on the first paragraph** of every deep article.
- **Section headers should be thematic, not numbered.** "一堵墙" beats "二、市场困境".
- **Pull quotes are reserved for actual quotes** worth pulling — used 1-2 times max per article, not as decoration.
- **4500-6000 characters per deep article.** This is the magazine length; shorter feels like a blog post, longer loses readers.
- **Open with a specific scene or moment**, not with a thesis statement. MIT TR almost always starts with an observation, an event, a number — never with "In recent years, ..."
- **Data lives inside sentences**, not in tables. "From 2015 to 2024 the market grew from $500M to $4B" — not a chart.

### Phase 5 — Page templates

Three HTML templates form the backbone:

1. **Homepage** (`site/index.html`) — full-viewport hero with motif reveal animation, current-issue feature card, manifesto / about, subscribe CTA, footer
2. **Issue index** (`site/issues/XXX/index.html`) — cover, TOC, all 10 columns inline, footer
3. **Deep article** (`site/issues/XXX/articles/SLUG.html`) — light reading mode, breadcrumb, article header, body with one inline SVG figure, sibling articles navigation, footer

Reference scaffolds in `references/page-templates.md`. Each template is fully self-contained, uses absolute paths (everything from root `/`), and shares the same CSS and JS modules.

### Phase 6 — Visual identity component

The motif gets its own JavaScript module that generates the SVG programmatically. This way it can be sized, colored, animated, and varied per issue without re-drawing.

For 《识界》the motif is the iris (`iris.js`, ~240 lines). It exports:
- `buildIris(opts)` — full iris SVG with concentric rings, radial spokes, pupil, accent ring, optional label text
- `buildMiniIris(opts)` — small iris for masthead / mini logos
- `playIrisReveal(container, opts)` — cinematic animated reveal on page load
- `trackPupil(container, maxOffset)` — mouse-follow eye effect on cover

For other brands, write the equivalent component. See `references/motif-component.md` for the iris implementation as reference, and design principles for adapting to other motifs (waves, constellations, lenses, etc.).

### Phase 7 — Image strategy

Each deep article gets **one custom illustration**. Two acceptable types:

**SVG illustrations** (preferred for editorial graphics) — diagrams, timelines, comparison charts, conceptual figures. Drawn fresh per article, never reused. Each illustration should do a job that prose alone can't (visual comparison, temporal sequence, spatial relationship).

**AI-generated photographs** (for hero-level moody imagery) — use sparingly, max 3-5 per issue. Generate via GPT Image / Flux Pro / Midjourney with carefully written prompts. Always run through a unifying editorial filter (slight desaturation, contrast bump, optional duotone) so all images feel like they came from the same publication. Avoid AI-generated images of real people, named events, or politically/ethically sensitive scenes.

**Never use stock photos.** They instantly cheapen the magazine.

The image processing script (`tools/process_images.py`) takes raw PNGs and produces WebP + JPG fallbacks at 2x and 1x. See `references/image-strategy.md` for the full workflow including SVG concept patterns and the editorial filter.

### Phase 8 — Deployment

Choose hosting based on audience:
- **China audience**: Tencent COS bucket + custom domain + CDN. Static-website-hosting mode. HTML files need their `Content-Type: text/html; charset=utf-8` and `Content-Disposition: inline` headers set explicitly after upload, otherwise COS serves them as downloads.
- **Global audience**: Cloudflare Pages or Vercel — connect Git, push to deploy.

The deploy script template is in `references/deployment.md`. It handles credentials (loaded from `.secrets/.env`), proxy environment cleanup (a recurring trap on macOS with VPN tools), recursive upload, and per-HTML header fixing.

After every deploy: **flush the CDN cache**. Otherwise users see the old version for up to 30 minutes.

### Phase 9 (companion) — Launch communication

Every issue (especially the inaugural one) deserves a companion launch post on the brand's existing channels — typically a WeChat 公众号 article. The launch post is **not** a copy of the magazine content; it is a piece of editorial writing about the magazine itself, in the voice of the host channel.

For 《识界》创刊号, the launch post on 虹识微刊 framed the magazine as a "longer-form sister to the technical paper reviews" microreaders are used to. It included three custom-designed images (cover, TOC visual, CTA), pointed to specific deep articles by name, and made an explicit promise about what would and wouldn't change for existing readers.

The full template for launch posts is in `references/launch-communication.md`.

## How to use this skill in practice

When this skill triggers, don't dump the whole playbook on the user at once. Walk them through it in order:

1. Open with **Phase 1 brainstorming questions** — this is where most users haven't thought through their answers, and where the most leverage exists.
2. Once decisions are locked, **execute Phase 2 (design system) before any HTML**. Don't let the user push you into building a homepage on day one without tokens — you'll regret it.
3. Build **Homepage first**, then **Issue 001 index**, then **first deep article** as the proof-of-quality. Show the user. Iterate the visual until they agree it's "stunning" (their word will vary; the standard is "would I screenshot this and share it?").
4. Once one deep article proves the writing standard, **batch-write the rest** for that issue.
5. **Deploy to a preview path** (or directly to root if user agrees existing site is replaceable).
6. **Write the launch communication** as a final companion deliverable.

A first-issue project takes 4-8 sessions of meaningful collaboration with the user, depending on iteration count on visual direction. Subsequent issues are faster because the templates and patterns carry over.

## When NOT to use this skill

- User wants a single article or essay → use a regular writing skill
- User wants a blog with reverse-chronological posts → that's a different content model
- User wants a marketing landing page → different goals (conversion > engagement)
- User wants a daily newsletter → different rhythm (short, frequent, less designed)
- User wants a content management system → this skill produces handcrafted static HTML, not a CMS

## Reference files

Read these as the project progresses, not all at once.

- `references/question-funnel.md` — Phase 1 interview questions
- `references/visual-directions.md` — three default visual styles + how to choose
- `references/design-system.md` — full CSS tokens template
- `references/column-architecture.md` — 10-column rationale + content rules
- `references/writing-style.md` — MIT Tech Review writing rules in detail
- `references/page-templates.md` — HTML scaffolds for all three page types
- `references/motif-component.md` — generative SVG component design
- `references/image-strategy.md` — SVG concepts + AI prompts + editorial filter
- `references/deployment.md` — Tencent COS + generic static host
- `references/launch-communication.md` — companion WeChat / blog post template
