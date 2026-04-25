# Phase 1 — Brainstorming question funnel

The single most important phase. Decisions made here ripple through everything else. Run the user through them in order; do not skip.

Each question below has its own purpose — surfaced in the sub-bullets. Don't read them as a checklist, read them as a conversation; it's a Socratic dialogue, not a survey.

## 1 · Audience

**Who reads this magazine?** Push the user past "everyone" — get a specific portrait.

- Internal employees → "internal voice", informal, more people-focused
- Customers / partners → semi-formal, brand voice consistent with sales materials
- Industry / public → most editorial, must read like a real magazine
- Investors → analytical, with framing for company narrative

The audience determines tone, language register, and column priorities.

## 2 · Distribution medium

**Where will readers actually read it?**

- HTML web magazine (recommended; broadest reach, best design control)
- PDF (for archive / email; less interactive)
- WeChat 公众号 article (max 微信 reach, severely constrained design)
- WeChat H5 page (richer than 公众号, less wide reach)
- Long image (朋友圈 native, lowest effort, no interactivity)

Best practice: HTML primary + WeChat 公众号 companion + 长图 derivative.

## 3 · Hosting platform

**Where does the HTML actually live?** Determines deploy workflow and access pattern.

| Option | China audience | Global | Deploy ease |
|---|---|---|---|
| Tencent COS + 自定义域名 + CDN | ✓ best | – | medium |
| Aliyun OSS + CDN | ✓ best | – | medium |
| Cloudflare Pages | △ unstable | ✓ best | easy |
| Vercel / Netlify | ✗ blocked often | ✓ best | easy |
| Self-hosted on company website /weekly | ✓ if HQ in China | ✓ if not | reuses existing infra |
| GitHub Pages / Gitee Pages | △ slow / limited | △ small projects | easy |

For a Chinese publisher, default to Tencent COS + CDN + custom subdomain. Requires ICP filing for the domain.

## 4 · Brand identity

**Does the publisher already have a strong visual identity?**

- Yes → adopt their palette, fonts, logo. Magazine becomes a brand expression.
- No → invent one. Strong opportunity to set tone.

Always extract:
- Primary brand color (hex)
- Logo (vector if possible)
- Existing typography preferences
- Tone-of-voice guidelines if any

## 5 · Visual direction

Three defaults; user picks one or a hybrid (see `visual-directions.md` for full details).

- **Tech Brutalism** — black background, brand color accent, large empty space, geometric, severe
- **Editorial Magazine** — paper-cream background, classic serif typography, warm
- **Smart Digest** — bright, info-dense, friendly, color-coded sections

For technical brands and B2B publishers, default to Tech Brutalism × Editorial Magazine hybrid (dark covers + light reading mode).

## 6 · Visual motif

**The recurring generative concept.** Every magazine needs one — it's what makes the cover instantly recognizable as belonging to this publication, not another.

Examples:
- Iris (HOMSH biometrics weekly)
- Wave / spectrum (signal-processing publishers)
- Constellation / network graph (community publishers)
- Lens / aperture (photography or vision publishers)
- Bookmark / page (reading communities)
- Compass / cardinal (navigation / strategy)

The motif must be:
- Programmatically generatable (so it can vary per issue)
- Recognizable at multiple scales (3px favicon → full-screen cover)
- Symbolically tied to the publisher's domain
- Aesthetically able to absorb the brand color as accent

Skip motifs that are clichés (lightbulbs, brain icons, gears, world maps).

## 7 · Reading length

How long should reading the full issue take?

| Length | Use case |
|---|---|
| 5 minutes | Daily digest, headline-only |
| 15 minutes | Weekly highlights, fewer columns |
| **30 minutes** | **Full magazine, 10 columns, default recommendation** |
| 45-60 minutes | Bi-weekly or monthly thick magazine |

30 min is the sweet spot for a Friday afternoon publication. Long enough to feel substantial, short enough to fit one sitting.

## 8 · Language

- Chinese only — simplest
- English only — for international audiences
- **Bilingual** — Chinese primary + English subtitle, key terms parenthetical English. **Strong default for technical Chinese brands** because it signals seriousness and globalness.

For bilingual: never machine-translate the body. Title and section headers can be bilingual; body should be one language with key technical terms parenthetically annotated.

## 9 · Columns / sections

Default to 10-column structure (see `column-architecture.md`). The user may want to adjust, but the functional slots should remain. Common adjustments:
- Drop "AI 速递" if not in tech industry
- Add a "讲者 / Voices" interview column if you have access to interesting people
- Add a regular feature column (e.g., book review, classics revisit)

Resist user pressure to do "more columns" — 10 is the sweet spot. More feels cluttered.

## 10 · Frequency and timing

| Frequency | Best for |
|---|---|
| Daily | News-paced industries, very short content |
| Weekly | **Default — most magazines** |
| Bi-weekly | Slow-news industries, deeper articles |
| Monthly | Long-form, low-pressure publications |

For weekly, time of week matters:
- **Friday afternoon (recommended)** — readers are winding down, attention available
- Monday morning — start-of-week briefing, but competes with email triage
- Sunday evening — long-form personal time, but feels intrusive on weekend
- Tuesday/Wednesday — neutral, no strong rhythm

## 11 · Editorial process

- **Editor-in-chief** — who has final say on each issue?
- **Review process** — solo / 2-eyes / 4-eyes / committee?
- **Byline** — published as personal author? "[Brand] editorial board"? Anonymous?
- **Author voice** — first person ("we"), third person ("the editorial team"), or invisible omniscient?

For company-published magazines, the strongest default is "[Brand] editorial board" with first-person plural in the editor's note ("we") and third-person elsewhere ("the company / the industry"). This signals collective authorship without dropping the editorial voice into corporate marketing tone.

## 12 · Subscription mechanism

How does a reader subscribe / get notified of new issues?

- Email digest (requires mailing list infrastructure)
- WeChat 公众号 push (requires existing 公众号)
- RSS feed (small but motivated audience)
- "No subscription, just visit weekly.brand.com" (zero infra, weakest retention)

For inaugural launch, "visit + bookmark" is acceptable. Plan to add email subscription within first 3 months if the magazine sticks.

---

## After the funnel: write the design brief

Before moving to Phase 2, summarize all decisions in a **one-page design brief**. Format:

```markdown
# [Magazine name] · Design Brief v0.1

## Basics
- Name: ...
- Subtitle: ...
- Publisher: ...
- Editor: ...
- Frequency: ...
- Length target: ...

## Visual
- Direction: ...
- Motif: ...
- Brand color: #...
- Typography: ...

## Content
- Audience: ...
- Tone: ...
- Columns: ...
- Voice / byline: ...

## Distribution
- Primary: ...
- Companion: ...
- Hosting: ...
```

Have the user explicitly approve this brief before writing any code. It is the contract for everything that follows.
