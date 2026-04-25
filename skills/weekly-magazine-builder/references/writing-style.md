# Writing style — MIT Technology Review reference standard

The writing style is what separates a magazine from a blog. Most company-published content fails at this — they default to marketing tone (lists, callouts, emoji-headed sections, "discover how X transforms Y" subtitles). A real magazine uses none of those.

The reference standard is **MIT Technology Review** at its best. Read 2-3 of their feature articles before writing if you're not familiar with the cadence.

## Hard rules — never break

These are not "guidelines." They are absolute. Breaking them visibly drops the perceived quality of the magazine.

**No bullet lists in article body.** No `<ul>`, no `<ol>`, no Markdown `-` lists. Footer navigation is fine. Inside `.article-body`, prose only.

**No tables in article body.** If you want to communicate "X has these properties: a, b, c" — write it as a sentence: "It is fast, lightweight, and self-contained." Tables are appropriate in `数据一瞥` data pieces only, where the SVG visualization handles them.

**No callout boxes.** No "💡 Tip:" / "⚠️ Note:" / colored sidebar boxes. Important things should be in the prose where their importance is obvious from the writing.

**No emoji.** Including 📌 ✅ 🎯 ✨ 🔥 — never. Even single decorative emoji destroy the editorial register. The only exception: emoji being discussed as a topic in the article itself, in which case they appear in quotation marks.

**No section headers with numbers.** "一、市场困境 / 二、技术挑战" reads like a school essay. Use thematic short titles: "一堵墙 / 一颗芯片 / 下一个十五年". Each header should evoke the section's content without being literal.

**No "ALL CAPS" emphasis** in body text. Use italics if you must emphasize.

**No bolded sentences as decoration.** Bold is for genuine lead phrases (start of a paragraph that introduces a new concept) and embedded entity names. If your article has more than 8-10 bold spans across 5000 characters, you're using bold as decoration.

## Length

- **Deep articles**: 4500-6000 Chinese characters (1500-2000 English words)
- **Stack items** (Tech Radar / Industry Watch / AI Pulse abstracts): 100-300 characters
- **News cards** (Inside [Brand]): 100-200 characters
- **Editor's note**: 400-700 characters
- **Brief items**: 80-120 characters each, ×5 = 500-600 total

## Article structure (deep dive)

**Opening (lede)**: Open with a specific scene, observation, number, or moment. Never with a thesis. 

Bad opening: "近年来，虹膜识别技术正在经历快速发展..."
Good opening: "每个工作日的清晨，约旦扎塔里难民营的粮食站前都会排起长队。这里是叙利亚战争以来最大的难民聚集地之一..."

The first 200-300 characters should make the reader want to know what this scene has to do with the article's topic. The connection comes 1-2 paragraphs later, not in sentence one.

**Drop cap on first paragraph**: visual signal that this is a feature article, not a short item. The CSS handles this automatically via `.article-body > p:first-of-type::first-letter`.

**Section structure**: 5-8 thematic sections. Each section starts with an `<h2>` that has a short evocative title (no numbers).

**Pull quote**: 1-2 maximum per article. Use `<blockquote>` for an actual quote-worthy line that you want pulled out. Don't use it for decoration.

**Closing**: Return to the opening scene OR widen out to the long view. The last paragraph is one of the most important — readers remember it. Resist the temptation to summarize what was said; instead, place the article's argument in a longer arc.

## Sentence-level

**Vary sentence length.** Mostly long sentences with information density, occasionally a short punchy one for emphasis.

**Prefer specificity over generality.** "300 项专利" beats "大量专利". "The market grew from $500M in 2015 to $4B in 2024" beats "The market grew rapidly".

**Embed data in sentences, don't break out into tables.** "全球虹膜识别市场从 2015 年的不到 5 亿美元增长到 2024 年的约 40 亿美元，复合增长率约 25%" reads like a magazine. The same content as a table would read like a press release.

**Use connective prose between facts.** "这个数字意味着..."  / "更重要的是..."  / "对此的另一种解读..."  carry the reader through reasoning. Without these, an article feels like a list of facts.

**Quote with attribution and context.** Don't just say "He said X." Say "He said X — a position that reflects the company's broader bet on Y."

## Voice

For corporate-published magazines:

- **First person plural ("we")** in editor's note only
- **Third person** elsewhere ("the company", "the industry", "the publisher")
- **Avoid** "smart phrases" that mark marketing voice: "in today's fast-paced world", "leveraging cutting-edge", "pivotal moment", "paradigm shift"
- **Industry commentator perspective for Industry Watch** — your own brand should be mentioned as a player among others, not as the protagonist

If the publisher itself is the subject of the article (Inside [Brand] column), use **third-person editorial voice**, not first-person promotional voice. "虹识技术成立于 2011 年" — never "我们成立于 2011 年" in editorial body.

## What to do when the user pushes back

A common pattern: the user reads a draft and says "this needs more bullet points to be scannable" or "can you add a callout box for the key takeaway." Hold the line.

Explain: "Bullet points are scannable. But this is a magazine, not documentation. Magazine readers value the experience of reading flowing prose — that's why they come here instead of scrolling Twitter. Adding bullets makes it feel like a slide deck. The article will be less impressive, more forgettable."

Offer the alternative: if a passage is hard to follow, the answer is to rewrite it as clearer prose, not to fragment it into bullets.

If they insist, do it once, but tell them you predict the article will lose a reading-quality grade.
