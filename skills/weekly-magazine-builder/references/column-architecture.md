# Content architecture — the ten columns

The proven structure for a 30-minute weekly magazine. Adapt names but preserve **functional slots** — each fills a different reader need at a different moment in the read.

| # | Default name | English | Time | Function |
|---|---|---|---|---|
| 01 | 卷首语 | Editor's Note | 3 min | Voice the editorial perspective; tell the reader why this issue matters |
| 02 | 本期速览 | The Brief | 1 min | 5 punchy bullet-equivalents (in prose) — for readers who only have a minute |
| 03 | 公司动态 | Inside [Brand] | 3 min | What the publisher itself did this week |
| 04 | 技术前沿 | Tech Radar | 5 min | New papers / new engineering / new techniques |
| 05 | 深度一文 | Deep Dive | 12 min | The cover story — 4500-6000 chars on one important topic |
| 06 | 行业观察 | Industry Watch | 3 min | Market / policy / regulation movements |
| 07 | AI 速递 | AI Pulse | 2 min | Short briefs on adjacent AI happenings (or another adjacent field) |
| 08 | 数据一瞥 | By the Numbers | 1 min | One data visualization with context |
| 09 | 识者之言 | Voices | 1 min | One quote worth sitting with (use sparingly — must be earned) |
| 10 | 下期预告 | Next Week | <1 min | Hook for next issue + editorial team byline |

Total: ~31 minutes. Sweet spot.

## Why these ten

**Why 卷首语 first?** Readers need orientation. The editor's note tells them what this week was about and signals the magazine's voice. Without it, the issue feels like a random aggregation.

**Why 速览 right after?** Different readers have different time budgets. The Brief lets a busy reader leave after 4 minutes with the highlights. It's also a quality check — if the editor can't compress the issue into 5 sentences, the issue isn't ready.

**Why 公司动态 third (not last)?** Two reasons. First, readers of company-published magazines want to know "what's the publisher up to" — surface it early. Second, putting it after the brief contextualizes the editorial perspective: you're reading the publisher's view, here's what they did this week to be in a position to have that view.

**Why 技术前沿 / Tech Radar before the deep dive?** It warms up the reader's "this is a serious magazine" mode. Fresh papers, recent engineering — sets the tone before the long-form payoff.

**Why a single deep dive in the middle?** The structural keystone. Magazines need one substantial piece per issue or they feel like a list. Putting it in the middle is intentional — readers who arrive in The Brief mode will keep reading; readers who arrive in Deep Dive mode have orientation.

**Why 行业观察 after the deep dive?** Cool-down. After 12 minutes of focused reading, readers need a different mode — broader, less intense. Industry Watch gives that without losing them.

**Why 数据一瞥 alone?** Visual rhythm. Eight prose sections in a row exhausts even committed readers. A data piece is a "rest beat" — a single chart with three sentences of context.

**Why 识者之言 second-to-last?** Magazines that quote well are taken more seriously than those that don't. One quote per issue, formatted huge with negative space, sticks with readers.

**Why 下期预告 last?** Drives next-week return. Without a preview, readers move on. With one, they remember to come back.

## Content rules per column

### 01 · 卷首语 / Editor's Note
- 3 paragraphs, ~600 chars total
- Opens with a specific observation or question, not a thesis
- Ends with byline: "[Brand] editorial board · YYYY.MM.DD"
- Voice: first-person plural ("we"), considered, not promotional
- One narrative claim: why this issue exists, what it's trying to do

### 02 · 本期速览 / The Brief
- Exactly 5 items
- Each item: bold lead phrase + 1-2 sentences elaboration
- All in flowing prose, NOT bullet lists (the "5 numbered slots" appear as `<ol class="brief-list">` with custom styling — visually rhythmic without being a checklist)
- Each item should be a different category: news, market, technical, policy, etc. — variety creates "this issue covered the world" effect

### 03 · 公司动态 / Inside [Brand]
- 3-5 news cards
- Each card: date + source line, headline, 2-3 sentence summary
- Cards link to deep articles when available
- This is the only column that needs **real-time freshness** — must be from the past 1-2 weeks
- Each card with a deep article gets `阅读全文 · X 分钟 →` link

### 04 · 技术前沿 / Tech Radar
- 3 stack items
- Each: tag (e.g., 算法 / 硬件 / 安全 / 隐私计算) + source citation + headline + 100-200 char abstract
- Abstract should be one paragraph, no bullet lists
- Mix of paper reviews, engineering announcements, technique deep cuts
- Stack items with deep articles get the `阅读全文 →` link

### 05 · 深度一文 / Deep Dive
- The cover story
- 4500-6000 Chinese characters (English equivalent: 1500-2200 words)
- Strict MIT Tech Review format — see `writing-style.md`
- Lives both in the issue index (full text inline) AND as a standalone deep page (allows direct linking and sharing)
- Always has a hero image at top (AI-generated photographic, with editorial filter)

### 06 · 行业观察 / Industry Watch
- 3 stack items
- Mix of: market data, regulation / policy news, competitor moves, geopolitical signals
- Each item should be analytical, not just "what happened" — say what it means
- Industry Watch is the column that most often becomes worth quoting elsewhere

### 07 · AI 速递 / AI Pulse
- 4 short stack items (shorter than Tech Radar)
- ~80-150 chars each
- Tag style: 深伪 / Agent / 联邦 / 大模型 / 等
- Optional column — drop if not in tech industry
- Substitute: 内容前沿 / 设计趋势 / 投资动向 etc.

### 08 · 数据一瞥 / By the Numbers
- One data piece, displayed as `data-piece` grid
- Left column: caption (h4 + 1 paragraph context + source)
- Right column: SVG visualization
- Numbers should tell a coherent story — not "five random numbers"
- For the inaugural issue, often most powerful when telling the publisher's own story in numbers

### 09 · 识者之言 / Voices
- One quote, one attribution
- Massive typography — `clamp(32px, 4.5vw, 56px)`, italic display serif
- Quote should be earned — used a real, attributed line, ideally from someone the publisher's audience would recognize
- For corporate magazines: founder / CTO quotes work well; avoid quoting random pundits
- The red opening quotation mark is rendered separately and large

### 10 · 下期预告 / Next Week
- Half-revealed motif (visual teaser)
- Headline + 2-sentence teaser
- Release date + time
- Editorial team byline
- Optional: link to subscribe / bookmark

## When to deviate

The 10 columns are calibrated for a tech / industry weekly. For other genres:

- **Lifestyle / culture weekly**: drop AI Pulse, replace Tech Radar with "Reading List", add "Recipe / Practice" or "Q&A"
- **Investment newsletter**: replace Tech Radar with "Position Updates", expand By the Numbers to two pieces
- **Internal company magazine**: expand Inside [Brand] to 5+ cards, add "Team Spotlight" interview
- **Book / publishing**: replace Tech Radar with "Excerpt", add "Book of the Week"

The constants across all variants:
- Editor's note opens
- One deep dive in the middle
- One Voices quote
- Next-issue hook closes
