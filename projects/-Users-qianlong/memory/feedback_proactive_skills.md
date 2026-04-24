---
name: Proactively use marketing skills
description: When marketing-related topics come up, proactively invoke the relevant installed marketing skills instead of waiting for explicit instructions
type: feedback
originSessionId: b57cb493-8b41-41a3-890f-cc0e0d0f08e4
---
Proactively invoke marketing skills when the context matches, don't wait for the user to say "/skill-name".

**Why:** The user has 45+ marketing skills installed (from marketingskills repo and others). They expect these to be used as specialized tools whenever the conversation touches marketing topics — CRO, copywriting, SEO, pricing, analytics, retention, growth, etc.

**How to apply:** When the user discusses any marketing-adjacent topic, identify the best-fit skill and invoke it immediately. Treat the skill trigger descriptions as automatic matchers. Multiple skills can chain together (e.g., `product-marketing-context` first, then `copywriting`). Don't just answer from general knowledge when a specialized skill exists.
