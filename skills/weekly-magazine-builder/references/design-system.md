# Design system — CSS tokens template

Use this as the starting `tokens.css`. Adjust only:
- Primary brand color (search for `--red-500: #E60012`)
- Font choices (search for `--font-display`)

Everything else is calibrated and battle-tested. Do not casually change spacing scale, easing curves, or animation timings.

## tokens.css

```css
/* ===================================================================
 * [Magazine name] · 设计令牌
 * =================================================================== */

:root {
  /* ── 色彩 ── */
  /* 墨色 · 封面 / 栏目过渡 / 夜间阅读 */
  --ink-0: #0A0A0F;         /* 最深黑 */
  --ink-1: #14141D;
  --ink-2: #1F1F2B;
  --ink-3: #26262F;
  --ink-4: #3A3A45;
  --ink-5: #585863;

  /* 纸色 · 长文阅读 */
  --paper-0: #FAF7F0;       /* 最浅米白 */
  --paper-1: #F4F0E8;       /* 主纸色 */
  --paper-2: #EAE4D8;
  --paper-3: #D4CCB8;

  /* 中性灰 */
  --gray-100: #F2F0EA;
  --gray-200: #DCD8CE;
  --gray-300: #C0BDB3;
  --gray-400: #8A8A93;
  --gray-500: #6B6B76;
  --gray-600: #4A4A55;
  --gray-700: #2E2E37;

  /* 品牌主色（替换为项目色）*/
  --red-500: #E60012;
  --red-600: #B3000E;
  --red-300: #FF3B45;
  --red-glow: rgba(230, 0, 18, 0.14);

  /* 栏目辅助色 · 不同栏目的识别色 */
  --iris-amber: #D4A574;
  --iris-spectrum: #5AA8D4;
  --iris-teal: #3CAB8E;
  --iris-plum: #8B5A9C;

  /* ── 字体 ── */
  --font-display: "Fraunces", "Noto Serif SC", "Source Han Serif SC",
                  "Songti SC", "STSong", SimSun, serif;
  --font-serif:   "Spectral", "Noto Serif SC", "Source Han Serif SC",
                  "Songti SC", "STSong", SimSun, serif;
  --font-sans:    "Inter", -apple-system, BlinkMacSystemFont,
                  "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei",
                  sans-serif;
  --font-mono:    "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;

  /* ── 字号 · 完整跨度 ── */
  --fs-xs: 11px;
  --fs-sm: 13px;
  --fs-base: 16px;
  --fs-md: 18px;
  --fs-body: 19px;       /* 阅读正文 · 偏大增加沉浸感 */
  --fs-lg: 24px;
  --fs-xl: 32px;
  --fs-2xl: 48px;
  --fs-3xl: 64px;
  --fs-display: 96px;
  --fs-hero: 140px;
  --fs-monument: 220px;

  /* ── 字重 ── */
  --fw-light: 300;
  --fw-normal: 400;
  --fw-medium: 500;
  --fw-bold: 700;
  --fw-black: 900;

  /* ── 行高 ── */
  --lh-tight: 1.08;
  --lh-snug: 1.25;
  --lh-normal: 1.55;
  --lh-relaxed: 1.85;     /* 长阅读正文 */

  /* ── 字偶距 ── */
  --tr-tight: -0.02em;
  --tr-normal: 0;
  --tr-wide: 0.05em;
  --tr-wider: 0.15em;
  --tr-widest: 0.32em;

  /* ── 间距 · 4px 基数 ── */
  --sp-0: 0;
  --sp-1: 4px;
  --sp-2: 8px;
  --sp-3: 12px;
  --sp-4: 16px;
  --sp-5: 24px;
  --sp-6: 32px;
  --sp-7: 48px;
  --sp-8: 64px;
  --sp-9: 96px;
  --sp-10: 128px;
  --sp-11: 192px;
  --sp-12: 256px;

  /* ── 布局 ── */
  --w-reading: 680px;     /* 长文阅读栏宽 · 56-72ch */
  --w-content: 880px;
  --w-wide: 1160px;
  --w-full: 1440px;
  --gutter: 40px;

  /* ── 动画 ── 自定义贝塞尔，不用浏览器默认 */
  --ease-out: cubic-bezier(0.16, 1, 0.30, 1);     /* 慢进快出 */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-in: cubic-bezier(0.70, 0, 0.84, 0);
  --ease-serp: cubic-bezier(0.83, 0, 0.17, 1);    /* 戏剧性双曲 */

  /* ── 时长 · 偏慢，杂志感要"镇得住" ── */
  --t-instant: 120ms;
  --t-fast: 240ms;
  --t-normal: 480ms;
  --t-slow: 820ms;
  --t-cinema: 1400ms;
  --t-reveal: 2200ms;     /* 开篇 motif 苏醒 */

  /* ── 层级 ── */
  --z-base: 1;
  --z-sticky: 100;
  --z-reveal: 500;
  --z-cursor: 9999;
}

/* ── 主题切换 ── */
[data-theme="dark"] {
  --bg: var(--ink-0);
  --bg-subtle: var(--ink-1);
  --bg-elevated: var(--ink-2);
  --text: var(--paper-1);
  --text-muted: var(--gray-300);
  --text-subtle: var(--gray-400);
  --border: var(--ink-3);
  --accent: var(--red-500);
}

[data-theme="light"] {
  --bg: var(--paper-0);
  --bg-subtle: var(--paper-1);
  --text: var(--ink-1);
  --text-muted: var(--gray-600);
  --text-subtle: var(--gray-500);
  --border: var(--paper-3);
  --accent: var(--red-500);
}

/* ── 减少动画 · 尊重系统设置 ── */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## main.css highlights

The full main.css (~500 lines) includes: reset, typography defaults, masthead with backdrop-filter, button styles, reading progress ring, issue card components (regular and feature), footer with 4-column grid, utility classes (stack-sm/md/lg, dividers, sr-only), animation keyframes, and responsive breakpoints. The token-based approach means writing it is mostly applying tokens, not making new design decisions.

Key components:

**Masthead** — sticky top, 88% opacity bg, 14px backdrop-filter blur, 0.5px bottom border, hides on scroll-down with `transform: translateY(-100%)`.

**Reading progress ring** — fixed bottom-right 48×48 SVG, two concentric circles (track + bar), `stroke-dasharray: 141.37` (= 2π·22.5), updated via `stroke-dashoffset` on scroll.

**Issue cards** — `display: grid; grid-template-columns: 1fr 1fr; min-height: 320px; border: 0.5px solid;`. Hover: red border + slight Y-translate.

**Buttons** — bottom-only border accent, `letter-spacing: var(--tr-wider)`, uppercase, with `→` arrow that translates 4px on hover.

## issue.css highlights

The issue-specific stylesheet handles cover, TOC, chapter openers, deep-article reading mode (with drop cap, pull quotes, inline figures, sibling nav), data viz containers, and the "Voices" section's massive italic blockquote.

Key components:

**Cover** — full viewport, `data-theme="dark"`, hero image as `::before` background at `opacity: 0.45 mix-blend-mode: luminosity`, radial gradient vignette, motif SVG centered, large display title.

**TOC list** — 2-column grid with `column-gap: var(--sp-8)` (avoid label collision; this is a real bug surface), each entry is `grid-template-columns: 36px 1fr auto` for number / name / read-time.

**Chapter opener** — `grid-template-columns: auto 1fr` with massive red `--fs-3xl` chapter number on left, kicker + heading + English subtitle on right, separated by 0.5px bottom border.

**Feature (deep-dive section in issue index)** — switches the surrounding theme to paper-1 background, has full-bleed hero image, drop cap on first paragraph (`::first-letter` with 4.8em font-size), `feature-h3` subheadings with `data-num` attribute rendered as small monospace prefix.

**Article body figure** — uses negative margins to break out of reading column to full viewport width: `margin: var(--sp-9) calc(50% - 50vw); max-width: 100vw;`. The image inside stays constrained to `max-width: var(--w-wide)`.
