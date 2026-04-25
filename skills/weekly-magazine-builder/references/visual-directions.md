# Visual directions

Three default visual directions. Pick one or a hybrid based on audience and brand. Each comes with reference publications, color logic, typography, and image style.

## Direction A — Tech Brutalism

```
气质：冷、克制、技术含量高、排版严谨
配色：黑底 + 品牌色点缀 + 大量留白
字体：中文思源黑体 / 苹方 + 英文 Inter / JetBrains Mono
图像：技术示意图、代码块、网格线、光谱图
封面：几何图形 + 期号大字
```

**References**: Stripe Press, Linear Changelog, Vercel Blog, Anthropic press kit.

**When to use:**
- Technical / engineering audiences
- B2B / infrastructure brands
- Want to communicate "serious, no-nonsense, hardcore"

**Risks:**
- Can feel cold or unwelcoming to non-technical readers
- Easy to slip into "corporate dark mode" without character

## Direction B — Editorial Magazine

```
气质：严肃、有深度、像在读一本真正的行业刊物
配色：米白底 + 深灰 + 品牌色做强调色
字体：中文思源宋体（标题）+ 思源黑体（正文）+ 英文 Tiempos / GT Sectra / Spectral / Fraunces
图像：高质量图片 + 数据图表 + 引文版式
封面：大图 + 主标题 + 小字目录
```

**References**: The Information, MIT Technology Review, FT Weekend, The Economist, Harvard Business Review.

**When to use:**
- Investor / analyst / executive audiences
- Industry / public-facing publications
- Want to communicate "authoritative, considered, professional"

**Risks:**
- Requires real editorial content to pay off — design alone can feel pretentious if writing is shallow
- More expensive (custom illustrations vs. stock photos)

## Direction C — Smart Digest

```
气质：轻快、高效、色彩明快、信息密度大
配色：白底 + 品牌色 + 辅助色（蓝/绿）
字体：全无衬线，标题大、正文紧凑
图像：Emoji 标识 + 卡片式 layout + 色块
封面：简洁标题 + 本期亮点列表
```

**References**: Morning Brew, The Hustle, 极客公园 morning, Stratechery (lighter end).

**When to use:**
- Mass-market consumer audiences
- Casual / friendly brand voice
- Want to communicate "easy, accessible, fun"

**Risks:**
- Brand seriousness diluted
- Easy to look like a startup pitch deck rather than a publication

## Hybrid — Tech Brutalism × Editorial Magazine (recommended for technical Chinese brands)

The strongest default for serious B2B / technical Chinese publishers. Combines:

```
封面 + 栏目过渡：方向 A — 黑底 + 品牌色，电影感 reveal 动画
正文阅读页：方向 B — 米白底，宋体大字标题 + 衬线正文，长阅读友好
图像：编辑级 SVG 插图 + 必要时 AI 生成 hero 图配 duotone 滤镜
封面字体：Fraunces + 思源宋体 Heavy
正文字体：Spectral + 思源宋体
副字体：Inter（拉丁文 sans）+ JetBrains Mono（数据 / 代码）
```

This is what 《识界》 ended up using. The cover reads like A (severe, motif-forward), the body reads like B (warm, considered, page-turning).

The dark→light transition between sections becomes part of the editorial rhythm — it feels like turning the page in a physical magazine from cover insert to feature article.

## How to choose

Ask the user one question: "Which existing publication would you most want yours to feel like?"

If they say:
- Stripe Press / Linear → A
- MIT Tech Review / The Economist → B
- Morning Brew / 极客公园 → C
- "Both Stripe and MIT Tech Review depending on the page" → Hybrid (default)

If they don't have a reference at hand, walk through the three with a one-line summary each and let them point. If they're a technical Chinese brand and remain ambivalent, default to the **Hybrid**.

## Once direction is chosen

Lock the following before Phase 2:

- Primary brand color (hex)
- Secondary / accent colors (1-2)
- Display serif font (English)
- Body serif font (English)
- Sans serif font (English + Chinese)
- Mono font (data + code)
- Image treatment style (none / desaturate / duotone / grayscale)
