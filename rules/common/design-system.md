# Design System (DESIGN.md)

## What is DESIGN.md?

A plain-text design system document that AI agents read to generate consistent UI.
Introduced by Google Stitch — just drop it in your project root and coding agents
instantly understand how the UI should look and feel.

## Installed Collection

55+ DESIGN.md files are available at:

```
/Users/qianlong/.openclaw/workspace/awesome-design-md/design-md/
```

### Available Styles (by category)

**AI & ML:** claude, cohere, elevenlabs, minimax, mistral.ai, ollama, opencode.ai, replicate, runwayml, together.ai, voltagent, x.ai

**Developer Tools:** cursor, expo, linear.app, lovable, mintlify, posthog, raycast, resend, sentry, supabase, superhuman, vercel, warp, zapier

**Infrastructure & Cloud:** clickhouse, composio, hashicorp, mongodb, sanity, stripe

**Design & Productivity:** airtable, cal, clay, figma, framer, intercom, miro, notion, pinterest, webflow

**Fintech & Crypto:** coinbase, kraken, revolut, wise

**Enterprise & Consumer:** airbnb, apple, bmw, ibm, nvidia, spacex, spotify, uber

## How to Use

### Option 1 — Copy to project root (recommended)
```bash
cp /Users/qianlong/.openclaw/workspace/awesome-design-md/design-md/<site>/DESIGN.md ./DESIGN.md
```
Then tell the agent: "Build a UI that matches DESIGN.md"

### Option 2 — Reference inline
Read the file and include it in your prompt context:
```bash
cat /Users/qianlong/.openclaw/workspace/awesome-design-md/design-md/<site>/DESIGN.md
```

### Option 3 — Read directly in agent context
```
Read /Users/qianlong/.openclaw/workspace/awesome-design-md/design-md/vercel/DESIGN.md
and use it as the design system for this project.
```

## What Each DESIGN.md Contains

| # | Section | What it captures |
|---|---------|-----------------|
| 1 | Visual Theme & Atmosphere | Mood, density, design philosophy |
| 2 | Color Palette & Roles | Semantic name + hex + functional role |
| 3 | Typography Rules | Font families, full hierarchy table |
| 4 | Component Stylings | Buttons, cards, inputs, navigation with states |
| 5 | Layout Principles | Spacing scale, grid, whitespace philosophy |
| 6 | Depth & Elevation | Shadow system, surface hierarchy |
| 7 | Do's and Don'ts | Design guardrails and anti-patterns |
| 8 | Responsive Behavior | Breakpoints, touch targets, collapsing strategy |
| 9 | Agent Prompt Guide | Quick color reference, ready-to-use prompts |

## Rules for Claude Code

- When a user says "use [brand] style" or "match [site] design", automatically load the
  corresponding DESIGN.md from the collection above.
- When DESIGN.md exists in the project root, always read it before generating any UI code.
- Respect all color, typography, spacing, and component rules defined in DESIGN.md.
- Never override DESIGN.md tokens with arbitrary values — use the defined palette.
- If no DESIGN.md is present and the user wants a specific aesthetic, suggest one from the collection.
