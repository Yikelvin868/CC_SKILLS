# Page templates — HTML scaffolds

Three primary page types. All use absolute paths (rooted at `/`) — this requires deployment from domain root.

## File layout

```
site/
├── index.html              # Homepage (issue list)
├── 404.html
├── css/
│   ├── tokens.css
│   ├── main.css
│   └── issue.css
├── js/
│   ├── motif.js            # iris.js / wave.js / etc.
│   └── app.js
├── assets/
│   ├── fonts/              # if self-hosting
│   └── img/
│       └── 001/            # per-issue images
│           ├── _raw/       # originals (do not deploy)
│           ├── hero-2x.webp
│           ├── hero-2x.jpg
│           ├── hero-1x.webp
│           └── ...
└── issues/
    └── 001/
        ├── index.html      # Issue index (10 columns)
        └── articles/
            ├── article-1.html
            ├── article-2.html
            └── ...
```

## Template 1 — Homepage (`site/index.html`)

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Magazine name] · [English subtitle]</title>
  <meta name="description" content="...">
  <meta property="og:title" content="...">
  <meta name="theme-color" content="#0A0A0F">

  <link rel="preconnect" href="https://fonts.loli.net" crossorigin>
  <link rel="stylesheet" href="https://fonts.loli.net/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,700;9..144,900&family=Spectral:ital,wght@0,400;0,500;0,700;1,400&family=Inter:wght@300;400;500;600&family=Noto+Serif+SC:wght@400;500;700;900&family=JetBrains+Mono:wght@400&display=swap">

  <link rel="stylesheet" href="/css/tokens.css">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  <header class="masthead">...</header>

  <section class="hero">
    <!-- motif reveal animation centerpiece -->
    <div data-hero-motif></div>
    <h1 class="hero-title-cn cn-display">[Magazine]</h1>
    <div class="hero-title-en">[ENGLISH SUBTITLE]</div>
    <p class="hero-tagline">...</p>
    <div class="hero-meta">...</div>
  </section>

  <section class="section">
    <!-- current issue feature card -->
    <article class="issue-card issue-card-feature">...</article>
  </section>

  <section class="manifesto">
    <h2>[About this magazine]</h2>
    <p>... (3-5 paragraphs editorial framing)</p>
  </section>

  <section class="cta-block">
    <h3>Subscribe headline</h3>
    <a href="mailto:..." class="btn">订阅 Subscribe</a>
  </section>

  <footer class="footer">...</footer>

  <div class="reading-progress" data-reading-progress>...</div>

  <script type="module" src="/js/app.js"></script>
</body>
</html>
```

Critical pieces: hero with motif animation slot, current-issue feature card linking to `/issues/001/`, manifesto explaining the publication's premise, subscribe CTA with pre-filled mailto subject + body, footer with 4 columns, reading progress ring.

## Template 2 — Issue index (`site/issues/001/index.html`)

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="dark">
<head>
  <!-- ... metadata + fonts + tokens.css + main.css + issue.css ... -->
</head>
<body>
  <header class="masthead">...</header>

  <!-- Cover -->
  <section class="issue-cover">
    <div class="issue-cover-top">[masthead row]</div>
    <div class="issue-cover-center">
      <div class="issue-cover-iris" data-hero-motif></div>
      <div class="issue-cover-kicker">COVER STORY · 本期封面故事</div>
      <h1 class="issue-cover-title cn-display">[Cover story title]</h1>
      <p class="issue-cover-sub">[Subtitle]</p>
    </div>
    <div class="issue-cover-bottom">[issue meta]</div>
  </section>

  <!-- TOC -->
  <section class="toc">
    <div class="toc-inner">
      <div class="toc-head">
        <div class="kicker">Table of Contents</div>
        <h2>[TOC headline]</h2>
      </div>
      <nav class="toc-list">
        <!-- 10 entries: 01-10, name, time -->
      </nav>
    </div>
  </section>

  <!-- 10 columns, each as <section> with class="chapter" -->
  <section id="c01" class="chapter chapter--dark">
    <div class="chapter-reading">
      <div class="chapter-opener">
        <div class="chapter-num">01</div>
        <div class="chapter-heading">
          <span class="kicker">Editor's Note</span>
          <h2>卷首语</h2>
          <span class="chapter-en">[English subtitle]</span>
        </div>
      </div>
      <article class="editor-note">...</article>
    </div>
  </section>

  <!-- ... c02 through c10 ... -->

  <footer class="footer">...</footer>
  <div class="reading-progress" data-reading-progress>...</div>
  <script type="module">
    import { buildMiniMotif, playMotifReveal } from '/js/motif.js';
    // wire up cover motif, mini iris in masthead, sibling nav, scroll progress
  </script>
</body>
</html>
```

Key patterns:
- Each chapter has `id="c0N"` for anchor links from TOC
- Alternating `--dark` and `--light`/`--paper` chapter classes for editorial rhythm
- The deep-dive section (c05) uses `class="feature"` instead of `chapter` — full-bleed paper background, hero image, drop cap, etc.
- Cards in Inside Brand and stack-items in Tech Radar / Industry Watch get `<a class="card-read-more">阅读全文 · X 分钟</a>` links to the corresponding articles/SLUG.html

## Template 3 — Deep article (`site/issues/001/articles/SLUG.html`)

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <!-- metadata + fonts + tokens.css + main.css + issue.css -->
  <style>
    /* article-figure styles for inline SVG illustrations */
  </style>
</head>
<body>
  <!-- Light-theme masthead override for reading mode -->
  <header class="masthead" data-theme="light" style="background:var(--paper-1);...">
    <a href="/" class="masthead-brand">...</a>
    <a href="/issues/001/">← 回到 N° 001</a>
  </header>

  <main class="article-page">

    <nav class="article-breadcrumb">
      <a href="/">[Magazine]</a> /
      <a href="/issues/001/">N° 001</a> /
      <a href="/issues/001/#c0X">[Column name]</a> /
      <span class="current">[Article title]</span>
    </nav>

    <header class="article-header">
      <div class="kicker">[COLUMN] · [DATE]</div>
      <h1>[Article title]</h1>
      <p class="subtitle">[Subtitle, italic serif]</p>
      <div class="meta">
        <span>[Editorial source]</span>
        <span>[X 分钟阅读]</span>
      </div>
    </header>

    <div class="article-body">
      <p>[Opening paragraph with drop cap]</p>
      <p>...</p>

      <figure class="article-figure">
        <div class="article-figure-inner">
          <svg viewBox="0 0 960 ..." role="img">
            <!-- custom illustration unique to this article -->
          </svg>
        </div>
        <figcaption><strong>[Figure title]</strong> [Caption]</figcaption>
      </figure>

      <h2>[Thematic section header]</h2>
      <p>...</p>

      <blockquote>[Pull quote]</blockquote>

      <h2>...</h2>
      <p>...</p>
    </div>

    <div class="article-byline">
      [Byline + source attribution]
    </div>

    <section class="article-siblings">
      <div class="kicker">Also in [Column] · 本栏目其他报道</div>
      <div class="article-siblings-grid">
        <a href="..." class="sibling-card">
          <div class="tag">[Column]</div>
          <h4>[Other article title]</h4>
        </a>
        <!-- 2-4 sibling cards -->
      </div>
    </section>

  </main>

  <footer class="footer" style="background:var(--ink-0);color:var(--paper-1);">
    <!-- always dark footer for visual separation -->
  </footer>

  <script type="module">
    import { buildMiniMotif } from '/js/motif.js';
    document.querySelectorAll('[data-mini-iris]').forEach(el => {
      el.innerHTML = buildMiniMotif({ size: 22, color: '#E60012' });
    });
  </script>
</body>
</html>
```

Critical:
- `data-theme="light"` on `<html>` for reading mode
- Masthead inverted to paper background
- One `<figure class="article-figure">` per article — full-bleed via negative margins
- Sibling cards point to other articles in same column
- Footer remains dark (`var(--ink-0)`) for visual transition — feels like the "back cover" of the magazine after the article

## Template 4 — 404 page

Short — just a page-centered title with the magazine motif:

```html
<main class="nf">
  <span class="kicker">ISSUE NOT FOUND · 识别失败</span>
  <div class="nf-num">404</div>
  <div class="nf-divider"></div>
  <h1 class="nf-title">[Brand-flavored 404 message]</h1>
  <p class="nf-sub">[Body text + back-to-home link]</p>
</main>
```

The 404 message should be **branded** — for a biometric brand, "this page failed identification". For a publishing brand, "this page is not in our archive". Avoid "Page not found".
