# Launch communication

The inaugural issue deserves a companion launch announcement on the publisher's existing communication channels. This is **not** a copy of the magazine; it is editorial writing **about** the magazine, in the voice of the host channel.

## When to publish a launch post

- **Inaugural issue (N° 001)** — always
- **Major redesigns** (visual overhaul, new column structure) — usually
- **One-year anniversary** — sometimes
- **Special-themed issue** — occasionally

For routine weekly issues after launch, no companion post needed — readers know to visit weekly.publisher.cn directly.

## Where to publish

The launch post goes on the publisher's most engaged existing channel. Options:

- **WeChat 公众号 article** (Chinese audiences, default)
- **Company blog post**
- **LinkedIn long-form post**
- **Email to existing customer list**
- **Twitter thread + linked landing page**

A multi-channel launch is acceptable but write the post **for the primary channel first**, then adapt for others. Adapting from a Chinese 公众号 article into an English LinkedIn post is much easier than starting from a generic announcement and adapting both ways.

## Voice and angle

The launch post is in the **host channel's voice**, not the magazine's voice. This is critical.

For example: 《识界》 launched on 虹识微刊（technical paper-review focused 公众号）. The launch post on 虹识微刊 framed《识界》as "a longer-form sister to the technical paper reviews you're used to here." It opened with a callback to the kind of content microreaders expect, then explained why some industry stories need more space than 800-character paper reviews.

Had the same magazine launched on a more general / consumer-facing channel, the framing would be different — perhaps "a place to slow down once a week and read about [domain] with care."

The voice match matters because:
- Existing followers of the host channel chose to follow that voice
- A jarring tone shift in the launch post signals "this is a marketing pitch" and reduces engagement
- Readers want to be told why this matters **to them specifically as readers of this channel**

## Structural template

The full launch post is typically 1500-2200 Chinese characters (or 600-900 English words). Structure:

### Opening — meet readers where they are

Start by acknowledging what readers already get from this channel. "If you've subscribed to [channel] for a while, you've come here for [specific content type]." This builds trust before the pivot.

### Pivot — what's missing

Identify what the existing channel can't or doesn't do — the gap the new magazine fills. "But [some category of content] takes more than [the usual format] to cover well."

For 《识界》on 虹识微刊: 800-1500 character paper reviews can summarize a single research finding, but they can't capture the larger industry context — three regulatory and market events happening in the same month, for example. The new magazine fills that gap.

### Concrete recent examples

Don't just describe the gap abstractly — point at specific recent events that exemplify what the magazine will cover. Three events in one month is a strong pattern (it shows there's a real pace of important things to write about).

For 《识界》创刊号: April 2026 brought three signal events (三部门新规 + 行业排名 TOP 1 + 民航 AI 案例汇编). The launch post listed these specifically with dates.

### What the magazine is

After the framing, introduce the magazine concretely:
- Name + subtitle
- Core promise (length, frequency, structure)
- 10-column architecture (briefly listed)
- What "deep dive" means in this magazine

### What's in N° 001 specifically

Name 5-10 articles by title with a one-line teaser each. This is what gives existing followers a reason to click — concrete content, not abstract promises.

### Why the schedule

Briefly explain why your publishing schedule is what it is. "Why Friday afternoon" / "why weekly not daily" / "why 30 minutes."

### What this means for existing readers (critical for retention)

If the new magazine is launching on an existing channel's audience, address explicitly: **does anything change for them?** This is often the most important paragraph — readers worry that a new product means the old one will be neglected.

For 《识界》on 虹识微刊: the launch post explicitly said the existing paper-review format will continue at the same pace; 《识界》is additive, not a replacement. This reassures core followers.

### CTA

End with a clear action:
- URL of the magazine
- How to subscribe / bookmark
- Optional: link to one specific deep article from N° 001 they should read first

### Sign-off

In the host channel's voice. For 《识界》on 虹识微刊: "—— 虹识微刊编辑部 · 2026 年 4 月".

## Image specification

A WeChat 公众号 article needs at minimum:
- **One header cover image** (横版, 16:9, ~1600×900 or 800×450)
- **2-3 inline images** (varied — could be screenshots from the magazine, custom graphics, or small motif variants)
- **One closing CTA image** (often combining motif + URL + tagline)

Cover image best practices:
- Match the magazine's visual identity (motif visible, brand color, typography stack)
- Title visible (not too small)
- Issue number visible
- Looks correct as a thumbnail (when shared in chat, it's small)

The pattern that worked for 《识界》:
- `wechat_cover.svg` — 1600×900 dark cover with motif on right + 大字"识界" on left + ISSUE N° 001 + tagline
- 2 inline screenshots from `weekly.publisher.cn/issues/001/` (cover area + cards wall)
- `wechat_cta.svg` — 1600×600 light CTA with "现在开始读 第 001 期已上线 / weekly.publisher.cn"

Both SVGs convert to PNG via `rsvg-convert -w 1600 input.svg > output.png` (requires `brew install librsvg`) or browser screenshot.

## Multi-channel adaptation

If publishing the same launch on multiple channels:

- **WeChat 公众号 article**: full version (1500-2200 Chinese chars), with 4-5 images, formatted for 微信 编辑器
- **LinkedIn**: shorter version (~500-700 English words), 1 hero image, focus on professional audience hook
- **Twitter/X thread**: 8-12 tweets, one image (the cover), thread starts with a hook tweet (a single striking observation), each subsequent tweet teases one column
- **Email blast**: structured similarly to WeChat post, plain text and one cover image, signed by editor
- **Internal Slack / company chat**: shortest version (~150 words), one image, internal-voice ("the team has been working on...")

Keep all versions consistent on:
- Magazine name and subtitle
- Issue number and date
- Release time and frequency
- URL and how to subscribe

Vary by channel:
- Length and depth
- Voice register (formal / casual)
- Specific examples chosen (pick what resonates with each channel's audience)
- Image count and format

## After launch

The first issue's launch is a one-time event. For subsequent issues, the standing communication is:

- New issue auto-published every Friday at scheduled time
- A short "this week's issue is out: [headline]" notice in the host channel each Friday — 1-2 sentences, not a full post
- Email blast (if email subscriptions are set up) — auto-generated digest from the issue index
- Optional 长图 (long image) summary card for 朋友圈 sharing

Do not write a full launch-style post for every issue. The inaugural launch announcement is the "press release" moment. After that, the magazine should establish rhythm and let readers come to it.
