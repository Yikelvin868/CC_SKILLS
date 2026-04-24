# SEO / GEO Skills for Claude Desktop

> 以下是 SEO 和 GEO（Generative Engine Optimization）相关技能的完整参考。
> 用于优化网站在传统搜索引擎和 AI 搜索引擎中的表现。

---


---


# GEO-SEO Analysis Tool — Claude Code Skill (February 2026)

> **Philosophy:** GEO-first, SEO-supported. AI search is eating traditional search.
> This tool optimizes for where traffic is going, not where it was.


## Quick Reference

| Command | What It Does |
|---------|-------------|
| `/geo audit <url>` | Full GEO + SEO audit with parallel subagents |
| `/geo page <url>` | Deep single-page GEO analysis |
| `/geo citability <url>` | Score content for AI citation readiness |
| `/geo crawlers <url>` | Check AI crawler access (robots.txt analysis) |
| `/geo llmstxt <url>` | Analyze or generate llms.txt file |
| `/geo brands <url>` | Scan brand mentions across AI-cited platforms |
| `/geo platforms <url>` | Platform-specific optimization (ChatGPT, Perplexity, Google AIO) |
| `/geo schema <url>` | Detect, validate, and generate structured data |
| `/geo technical <url>` | Traditional technical SEO audit |
| `/geo content <url>` | Content quality and E-E-A-T assessment |
| `/geo report <url>` | Generate client-ready GEO deliverable |
| `/geo report-pdf <url>` | Generate professional PDF report with charts and scores |
| `/geo quick <url>` | 60-second GEO visibility snapshot |


## Market Context (Why GEO Matters)

| Metric | Value | Source |
|--------|-------|--------|
| GEO services market (2025) | $850M-$886M | Yahoo Finance / Superlines |
| Projected GEO market (2031) | $7.3B (34% CAGR) | Industry analysts |
| AI-referred sessions growth | +527% (Jan-May 2025) | SparkToro |
| AI traffic conversion vs organic | 4.4x higher | Industry data |
| Google AI Overviews reach | 1.5B users/month, 200+ countries | Google |
| ChatGPT weekly active users | 900M+ | OpenAI |
| Perplexity monthly queries | 500M+ | Perplexity |
| Gartner: search traffic drop by 2028 | -50% | Gartner |
| Marketers investing in GEO | Only 23% | Industry surveys |
| Brand mentions vs backlinks for AI | 3x stronger correlation | Ahrefs (Dec 2025) |


## Orchestration Logic

### Full Audit (`/geo audit <url>`)

**Phase 1: Discovery (Sequential)**
1. Fetch homepage HTML (curl or WebFetch)
2. Detect business type (SaaS, Local, E-commerce, Publisher, Agency, Other)
3. Extract key pages from sitemap.xml or internal links (up to 50 pages)

**Phase 2: Parallel Analysis (Delegate to Subagents)**
Launch these 5 subagents simultaneously:

| Subagent | File | Responsibility |
|----------|------|---------------|
| geo-ai-visibility | `agents/geo-ai-visibility.md` | GEO audit, citability, AI crawlers, llms.txt, brand mentions |
| geo-platform-analysis | `agents/geo-platform-analysis.md` | Platform-specific optimization (ChatGPT, Perplexity, Google AIO) |
| geo-technical | `agents/geo-technical.md` | Technical SEO, Core Web Vitals, crawlability, indexability |
| geo-content | `agents/geo-content.md` | Content quality, E-E-A-T, readability, AI content detection |
| geo-schema | `agents/geo-schema.md` | Schema markup detection, validation, generation |

**Phase 3: Synthesis (Sequential)**
1. Collect all subagent reports
2. Calculate composite GEO Score (0-100)
3. Generate prioritized action plan
4. Output client-ready report

### Scoring Methodology

| Category | Weight | Measured By |
|----------|--------|-------------|
| AI Citability & Visibility | 25% | Passage scoring, answer block quality, AI crawler access |
| Brand Authority Signals | 20% | Mentions on Reddit, YouTube, Wikipedia, LinkedIn; entity presence |
| Content Quality & E-E-A-T | 20% | Expertise signals, original data, author credentials |
| Technical Foundations | 15% | SSR, Core Web Vitals, crawlability, mobile, security |
| Structured Data | 10% | Schema completeness, JSON-LD validation, rich result eligibility |
| Platform Optimization | 10% | Platform-specific readiness (Google AIO, ChatGPT, Perplexity) |


## Business Type Detection

Analyze homepage for patterns:

| Type | Signals |
|------|---------|
| **SaaS** | Pricing page, "Sign up", "Free trial", "/app", "/dashboard", API docs |
| **Local Service** | Phone number, address, "Near me", Google Maps embed, service area |
| **E-commerce** | Product pages, cart, "Add to cart", price elements, product schema |
| **Publisher** | Blog, articles, bylines, publication dates, article schema |
| **Agency** | Portfolio, case studies, "Our services", client logos, testimonials |
| **Other** | Default — apply general GEO best practices |

Adjust recommendations based on detected type. Local businesses need LocalBusiness schema and Google Business Profile optimization. SaaS needs SoftwareApplication schema and comparison page strategy. E-commerce needs Product schema and review aggregation.


## Sub-Skills (10 Specialized Components)

| # | Skill | Directory | Purpose |
|---|-------|-----------|---------|
| 1 | geo-audit | `skills/geo-audit/` | Full audit orchestration and scoring |
| 2 | geo-citability | `skills/geo-citability/` | Passage-level AI citation readiness |
| 3 | geo-crawlers | `skills/geo-crawlers/` | AI crawler access and robots.txt |
| 4 | geo-llmstxt | `skills/geo-llmstxt/` | llms.txt standard analysis and generation |
| 5 | geo-brand-mentions | `skills/geo-brand-mentions/` | Brand presence on AI-cited platforms |
| 6 | geo-platform-optimizer | `skills/geo-platform-optimizer/` | Platform-specific AI search optimization |
| 7 | geo-schema | `skills/geo-schema/` | Structured data for AI discoverability |
| 8 | geo-technical | `skills/geo-technical/` | Technical SEO foundations |
| 9 | geo-content | `skills/geo-content/` | Content quality and E-E-A-T |
| 10 | geo-report | `skills/geo-report/` | Client-ready deliverable generation |


## Subagents (5 Parallel Workers)

| Agent | File | Skills Used |
|-------|------|-------------|
| geo-ai-visibility | `agents/geo-ai-visibility.md` | geo-citability, geo-crawlers, geo-llmstxt, geo-brand-mentions |
| geo-platform-analysis | `agents/geo-platform-analysis.md` | geo-platform-optimizer |
| geo-technical | `agents/geo-technical.md` | geo-technical |
| geo-content | `agents/geo-content.md` | geo-content |
| geo-schema | `agents/geo-schema.md` | geo-schema |


## Output Files

All commands generate structured output:

| Command | Output File |
|---------|------------|
| `/geo audit` | `GEO-AUDIT-REPORT.md` |
| `/geo page` | `GEO-PAGE-ANALYSIS.md` |
| `/geo citability` | `GEO-CITABILITY-SCORE.md` |
| `/geo crawlers` | `GEO-CRAWLER-ACCESS.md` |
| `/geo llmstxt` | `llms.txt` (ready to deploy) |
| `/geo brands` | `GEO-BRAND-MENTIONS.md` |
| `/geo platforms` | `GEO-PLATFORM-OPTIMIZATION.md` |
| `/geo schema` | `GEO-SCHEMA-REPORT.md` + generated JSON-LD |
| `/geo technical` | `GEO-TECHNICAL-AUDIT.md` |
| `/geo content` | `GEO-CONTENT-ANALYSIS.md` |
| `/geo report` | `GEO-CLIENT-REPORT.md` (presentation-ready) |
| `/geo report-pdf` | `GEO-REPORT.pdf` (professional PDF with charts) |
| `/geo quick` | Inline summary (no file) |


## PDF Report Generation

The `/geo report-pdf <url>` command generates a professional, branded PDF report:

### How It Works
1. Run the full audit or individual analyses first
2. Collect all scores and findings into a JSON structure
3. Execute the PDF generator: `python3 ~/.claude/skills/geo/scripts/generate_pdf_report.py data.json GEO-REPORT.pdf`

### What the PDF Includes
- **Cover page** with GEO score gauge visualization
- **Score breakdown** with color-coded bar charts
- **AI Platform Readiness** dashboard with horizontal bar chart
- **Crawler Access** status table with color-coded Allow/Block
- **Key Findings** categorized by severity (Critical/High/Medium/Low)
- **Prioritized Action Plan** (Quick Wins, Medium-Term, Strategic)
- **Methodology & Glossary** appendix

### Workflow
1. First run `/geo audit <url>` to collect all data
2. Then run `/geo report-pdf <url>` to generate the PDF
3. The tool will compile audit data into JSON, then generate the PDF
4. Output: `GEO-REPORT.pdf` in the current directory


## Quality Gates

- **Crawl limit:** Max 50 pages per audit (focus on quality over quantity)
- **Timeout:** 30 seconds per page fetch
- **Rate limiting:** 1-second delay between requests, max 5 concurrent
- **Robots.txt:** Always respect, always check
- **Duplicate detection:** Skip pages with >80% content similarity


## Quick Start Examples

```
# Full GEO audit of a website
/geo audit https://example.com

# Check if AI bots can see your site
/geo crawlers https://example.com

# Score a specific page for AI citability
/geo citability https://example.com/blog/best-article

# Generate an llms.txt file for your site
/geo llmstxt https://example.com

# Get a 60-second visibility snapshot
/geo quick https://example.com

# Generate a client-ready report
/geo report https://example.com
```


---


# GEO Audit Orchestration Skill

## Purpose

This skill performs a comprehensive Generative Engine Optimization (GEO) audit of any website. GEO is the practice of optimizing web content so that AI systems (ChatGPT, Claude, Perplexity, Gemini, etc.) can discover, understand, cite, and recommend it. This audit measures how well a site performs across all GEO dimensions and produces an actionable improvement plan.

## Key Insight

Traditional SEO optimizes for search engine rankings. GEO optimizes for AI citation and recommendation. Sites that score high on GEO metrics see 30-115% more visibility in AI-generated responses (Georgia Tech / Princeton / IIT Delhi 2024 study). The two disciplines overlap but have distinct requirements.


## Audit Workflow

### Phase 1: Discovery and Reconnaissance

**Step 1: Fetch Homepage and Detect Business Type**

1. Use WebFetch to retrieve the homepage at the provided URL.
2. Extract the following signals:
   - Page title, meta description, H1 heading
   - Navigation menu items (reveals site structure)
   - Footer content (reveals business info, location, legal pages)
   - Schema.org markup on homepage (Organization, LocalBusiness, etc.)
   - Pricing page link (SaaS indicator)
   - Product listing patterns (E-commerce indicator)
   - Blog/resource section (Publisher indicator)
   - Service pages (Agency indicator)
   - Address/phone/Google Maps embed (Local business indicator)

3. Classify the business type using these patterns:

| Business Type | Detection Signals |
|---|---|
| **SaaS** | Pricing page, "Sign up" / "Free trial" CTAs, app.domain.com subdomain, feature comparison tables, integration pages |
| **Local Business** | Physical address on homepage, Google Maps embed, "Near me" content, LocalBusiness schema, service area pages |
| **E-commerce** | Product listings, shopping cart, product schema, category pages, price displays, "Add to cart" buttons |
| **Publisher** | Blog-heavy navigation, article schema, author pages, date-based archives, RSS feeds, high content volume |
| **Agency/Services** | Case studies, portfolio, "Our Work" section, team page, client logos, service descriptions |
| **Hybrid** | Combination of above signals -- classify by dominant pattern |

**Step 2: Crawl Sitemap and Internal Links**

1. Attempt to fetch `/sitemap.xml` and `/sitemap_index.xml`.
2. If sitemap exists, extract up to 50 unique page URLs prioritized by:
   - Homepage (always include)
   - Top-level navigation pages
   - High-value pages (pricing, about, contact, key service/product pages)
   - Blog posts (sample 5-10 most recent)
   - Category/landing pages
3. If no sitemap exists, crawl internal links from the homepage:
   - Extract all `<a href>` links pointing to the same domain
   - Follow up to 2 levels deep
   - Prioritize pages linked from main navigation
4. Respect `robots.txt` directives -- do not fetch disallowed paths.
5. Enforce a maximum of 50 pages and a 30-second timeout per fetch.

**Step 3: Collect Page-Level Data**

For each page in the crawl set, record:
- URL, title, meta description, canonical URL
- H1-H6 heading structure
- Word count of main content
- Schema.org types present
- Internal/external link counts
- Images with/without alt text
- Open Graph and Twitter Card meta tags
- Response status code
- Whether the page has structured data


### Phase 2: Parallel Subagent Delegation

Delegate analysis to 5 specialized subagents. Each subagent operates on the collected page data and produces a category score (0-100) plus findings.

**Subagent 1: AI Citability Analysis (geo-citability)**
- Analyze content blocks for quotability by AI systems
- Score passage self-containment, answer block quality, statistical density
- Identify high-value pages that could be reformatted for better AI citation

**Subagent 2: Platform & Brand Analysis (geo-brand-mentions)**
- Check brand presence across YouTube, Reddit, Wikipedia, LinkedIn
- Assess third-party mention volume and sentiment
- Score brand authority signals that AI models use for entity recognition

**Subagent 3: Technical GEO Infrastructure (geo-crawlers + geo-llmstxt)**
- Analyze robots.txt for AI crawler access
- Check for llms.txt presence and quality
- Verify meta tags, headers, and technical accessibility for AI systems
- Check page speed and rendering (JS-heavy sites are harder for AI crawlers)

**Subagent 4: Content E-E-A-T Quality (geo-content)**
- Evaluate Experience, Expertise, Authoritativeness, Trustworthiness signals
- Check author bios, credentials, source citations
- Assess content freshness, depth, and originality
- Verify "About" page quality and team credentials

**Subagent 5: Schema & Structured Data (geo-schema)**
- Validate all schema.org markup
- Check for GEO-critical schema types (FAQ, HowTo, Organization, Product, Article)
- Assess schema completeness and accuracy
- Identify missing schema opportunities


### Phase 3: Score Aggregation and Report Generation

#### Composite GEO Score Calculation

The overall GEO Score (0-100) is a weighted average of six category scores:

| Category | Weight | What It Measures |
|---|---|---|
| **AI Citability** | 25% | How quotable/extractable content is for AI systems |
| **Brand Authority** | 20% | Third-party mentions, entity recognition signals |
| **Content E-E-A-T** | 20% | Experience, Expertise, Authoritativeness, Trustworthiness |
| **Technical GEO** | 15% | AI crawler access, llms.txt, rendering, speed |
| **Schema & Structured Data** | 10% | Schema.org markup quality and completeness |
| **Platform Optimization** | 10% | Presence on platforms AI models train on and cite |

**Formula:**
```
GEO_Score = (Citability * 0.25) + (Brand * 0.20) + (EEAT * 0.20) + (Technical * 0.15) + (Schema * 0.10) + (Platform * 0.10)
```

#### Score Interpretation

| Score Range | Rating | Interpretation |
|---|---|---|
| 90-100 | Excellent | Top-tier GEO optimization; site is highly likely to be cited by AI |
| 75-89 | Good | Strong GEO foundation with room for improvement |
| 60-74 | Fair | Moderate GEO presence; significant optimization opportunities exist |
| 40-59 | Poor | Weak GEO signals; AI systems may struggle to cite or recommend |
| 0-39 | Critical | Minimal GEO optimization; site is largely invisible to AI systems |


## Issue Severity Classification

Every issue found during the audit is classified by severity:

### Critical (Fix Immediately)
- All AI crawlers blocked in robots.txt
- No indexable content (JavaScript-rendered only with no SSR)
- Domain-level noindex directive
- Site returns 5xx errors on key pages
- Complete absence of any structured data
- Brand not recognized as an entity by any AI system

### High (Fix Within 1 Week)
- Key AI crawlers (GPTBot, ClaudeBot, PerplexityBot) blocked
- No llms.txt file present
- Zero question-answering content blocks on key pages
- Missing Organization or LocalBusiness schema
- No author attribution on content pages
- All content behind login/paywall with no preview

### Medium (Fix Within 1 Month)
- Partial AI crawler blocking (some allowed, some blocked)
- llms.txt exists but is incomplete or malformed
- Content blocks average under 50 citability score
- Missing FAQ schema on pages with FAQ content
- Thin author bios without credentials
- No Wikipedia or Reddit brand presence

### Low (Optimize When Possible)
- Minor schema validation errors
- Some images missing alt text
- Content freshness issues on non-critical pages
- Missing Open Graph tags
- Suboptimal heading hierarchy on some pages
- LinkedIn company page exists but is incomplete


## Output Format

Generate a file called `GEO-AUDIT-REPORT.md` with the following structure:

```markdown
# GEO Audit Report: [Site Name]

**Audit Date:** [Date]
**URL:** [URL]
**Business Type:** [Detected Type]
**Pages Analyzed:** [Count]


## Executive Summary

**Overall GEO Score: [X]/100 ([Rating])**

[2-3 sentence summary of the site's GEO health, biggest strengths, and most critical gaps.]

### Score Breakdown

| Category | Score | Weight | Weighted Score |
|---|---|---|---|
| AI Citability | [X]/100 | 25% | [X] |
| Brand Authority | [X]/100 | 20% | [X] |
| Content E-E-A-T | [X]/100 | 20% | [X] |
| Technical GEO | [X]/100 | 15% | [X] |
| Schema & Structured Data | [X]/100 | 10% | [X] |
| Platform Optimization | [X]/100 | 10% | [X] |
| **Overall GEO Score** | | | **[X]/100** |


## Critical Issues (Fix Immediately)

[List each critical issue with specific page URLs and recommended fix]

## High Priority Issues

[List each high-priority issue with details]

## Medium Priority Issues

[List each medium-priority issue]

## Low Priority Issues

[List each low-priority issue]


## Category Deep Dives

### AI Citability ([X]/100)
[Detailed findings, examples of good/bad passages, rewrite suggestions]

### Brand Authority ([X]/100)
[Platform presence map, mention volume, sentiment]

### Content E-E-A-T ([X]/100)
[Author quality, source citations, freshness, depth]

### Technical GEO ([X]/100)
[Crawler access, llms.txt, rendering, headers]

### Schema & Structured Data ([X]/100)
[Schema types found, validation results, missing opportunities]

### Platform Optimization ([X]/100)
[Presence on YouTube, Reddit, Wikipedia, etc.]


## Quick Wins (Implement This Week)

1. [Specific, actionable quick win with expected impact]
2. [Another quick win]
3. [Another quick win]
4. [Another quick win]
5. [Another quick win]

## 30-Day Action Plan

### Week 1: [Theme]
- [ ] Action item 1
- [ ] Action item 2

### Week 2: [Theme]
- [ ] Action item 1
- [ ] Action item 2

### Week 3: [Theme]
- [ ] Action item 1
- [ ] Action item 2

### Week 4: [Theme]
- [ ] Action item 1
- [ ] Action item 2


## Appendix: Pages Analyzed

| URL | Title | GEO Issues |
|---|---|---|
| [url] | [title] | [issue count] |
```


## Quality Gates

- **Page Limit:** Never crawl more than 50 pages per audit. Prioritize high-value pages.
- **Timeout:** 30-second maximum per page fetch. Skip pages that exceed this.
- **Robots.txt:** Always check and respect robots.txt before crawling. Note any AI-specific directives.
- **Rate Limiting:** Wait at least 1 second between page fetches to avoid overloading the server.
- **Error Handling:** Log failed fetches but continue the audit. Report fetch failures in the appendix.
- **Content Type:** Only analyze HTML pages. Skip PDFs, images, and other binary content.
- **Deduplication:** Canonicalize URLs before crawling. Skip duplicate content (e.g., HTTP vs HTTPS, www vs non-www, trailing slashes).


## Business-Type-Specific Audit Adjustments

### SaaS Sites
- Extra weight on: Feature comparison tables (high citability), integration pages, documentation quality
- Check for: API documentation structure, changelog pages, knowledge base organization
- Key schema: SoftwareApplication, FAQPage, HowTo

### Local Businesses
- Extra weight on: NAP consistency, Google Business Profile signals, local schema
- Check for: Service area pages, location-specific content, review markup
- Key schema: LocalBusiness, GeoCoordinates, OpeningHoursSpecification

### E-commerce Sites
- Extra weight on: Product descriptions (citability), comparison content, buying guides
- Check for: Product schema completeness, review aggregation, FAQ sections on product pages
- Key schema: Product, AggregateRating, Offer, BreadcrumbList

### Publishers
- Extra weight on: Article quality, author credentials, source citation practices
- Check for: Article schema, author pages, publication date freshness, original research
- Key schema: Article, NewsArticle, Person (author), ClaimReview

### Agency/Services
- Extra weight on: Case studies (citability), expertise demonstration, thought leadership
- Check for: Portfolio schema, team credentials, industry-specific expertise signals
- Key schema: Organization, Service, Person (team), Review


---


# AI Citability Scoring Skill

## Core Insight

AI language models cite passages that meet specific structural criteria. Research from Princeton, Georgia Tech, and IIT Delhi (2024) found that GEO-optimized content achieves 30-115% higher visibility in AI-generated responses. The key finding: AI systems preferentially extract and cite passages that are **134-167 words long**, **self-contained** (understandable without surrounding context), **fact-rich** (containing specific statistics, dates, or named entities), and **directly answer a question** in the first 1-2 sentences.

This is fundamentally different from traditional SEO copywriting, which optimizes for keyword density and user engagement metrics. GEO citability optimizes for **extractability** -- the ease with which an AI system can pull a passage from your content and present it as a direct answer.


## Citability Scoring Rubric (0-100)

### Category 1: Answer Block Quality (30% of total score)

This measures whether content contains clear, quotable answer passages that AI systems can extract verbatim.

**Scoring Criteria:**

| Score | Criteria |
|---|---|
| **90-100** | Every major section opens with a 1-2 sentence direct answer. Uses "X is..." or "X refers to..." patterns. First 40-60 words of each section can stand alone as a complete answer. |
| **70-89** | Most sections have clear answer openings. Some definition patterns present. Answers are identifiable but may need minor context. |
| **50-69** | Some sections have answer-like openings but many bury the answer in the middle or end of paragraphs. Few explicit definition patterns. |
| **30-49** | Answers are generally buried in long paragraphs. No consistent definition patterns. Content is narrative-driven rather than answer-driven. |
| **0-29** | No identifiable answer blocks. Content is entirely narrative, conversational, or fragmented. AI would struggle to extract any quotable passage. |

**What to look for:**

- **Definition patterns:** "X is [definition]." / "X refers to [explanation]." / "X means [meaning]."
- **Answer-first structure:** The answer appears in the first sentence, followed by supporting detail.
- **Quantified answers:** "The average cost of X is $Y" rather than "Many factors affect the cost of X."
- **Comparison answers:** "X differs from Y in three ways: [list]" rather than "X and Y are often confused."

**High-citability example:**
```
Content delivery networks (CDNs) are distributed server systems that cache and serve
web content from locations geographically close to end users. A CDN reduces latency
by 50-70% on average by serving assets from edge servers rather than a single origin
server. The three largest CDN providers as of 2025 are Cloudflare (serving approximately
20% of all websites), Amazon CloudFront, and Akamai Technologies.
```
Word count: 58. Self-contained: Yes. Facts: 3 specific data points. Definition pattern: Yes.

**Low-citability example:**
```
If you've ever wondered why some websites load faster than others, the answer might
surprise you. There's this amazing technology that has been around for a while now.
It's changed the way we think about web performance. Let me explain how it works and
why you should care about it for your business.
```
Word count: 52. Self-contained: No (no topic identified). Facts: 0. Definition pattern: No.


### Category 2: Passage Self-Containment (25% of total score)

This measures whether individual passages can be extracted and understood without needing the surrounding content.

**Scoring Criteria:**

| Score | Criteria |
|---|---|
| **90-100** | 80%+ of content blocks are fully self-contained. Each passage names its subject explicitly. No reliance on pronouns referencing earlier content. Contains specific facts within the passage. |
| **70-89** | 60-79% of content blocks are self-contained. Most passages name their subject. Occasional pronoun references that require context. |
| **50-69** | 40-59% of content blocks are self-contained. Mixed use of explicit subjects and pronouns. Some passages require reading prior sections. |
| **30-49** | 20-39% of content blocks are self-contained. Heavy reliance on pronouns and contextual references. Most passages need surrounding text. |
| **0-29** | Under 20% self-contained. Content reads as a continuous narrative where extracting any paragraph loses meaning. |

**Self-containment checklist for each passage:**

1. Does the passage explicitly name the subject (not "it," "this," "they")?
2. Can someone understand the main point reading ONLY this passage?
3. Does the passage contain at least one specific fact, statistic, or named entity?
4. Is the passage between 50-200 words (the optimal extraction length)?
5. Does the passage avoid starting with conjunctions ("But," "However," "And") that imply prior context?


### Category 3: Structural Readability (20% of total score)

This measures the structural formatting that helps AI systems parse and segment content.

**Scoring Criteria:**

| Score | Criteria |
|---|---|
| **90-100** | Clean H1 > H2 > H3 hierarchy. Question-based headings for informational content. Short paragraphs (2-4 sentences). Tables for comparisons. Ordered lists for processes. Unordered lists for features/options. |
| **70-89** | Good heading hierarchy with minor skips. Some question-based headings. Mostly short paragraphs. Some use of tables and lists. |
| **50-69** | Heading hierarchy present but inconsistent. Few question-based headings. Mix of short and long paragraphs. Limited tables/lists. |
| **30-49** | Minimal heading structure. No question-based headings. Long paragraphs dominate. Rare use of tables/lists. |
| **0-29** | No heading structure or severely broken hierarchy. Wall-of-text paragraphs. No tables or lists. |

**Structural best practices for AI citability:**

- **Heading hierarchy:** H1 (page title) > H2 (major sections) > H3 (subsections). Never skip levels.
- **Question-based headings:** "What is [topic]?" and "How does [topic] work?" are directly matchable to AI queries.
- **Paragraph length:** 2-4 sentences per paragraph. AI systems parse short paragraphs more reliably.
- **Tables:** Use for any comparison of 3+ items. AI systems extract table data with high accuracy.
- **Lists:** Use ordered lists for sequential processes, unordered lists for non-sequential items.
- **Bold key terms:** Bold the first use of important terms. This aids AI entity recognition.


### Category 4: Statistical Density (15% of total score)

This measures the presence of specific, verifiable data points that AI systems prioritize when selecting citation sources.

**Scoring Criteria:**

| Score | Criteria |
|---|---|
| **90-100** | 5+ specific statistics per 500 words. All claims backed by named sources or dates. Uses exact numbers (not "many" or "several"). Includes percentages, dollar amounts, timeframes, and named studies. |
| **70-89** | 3-4 statistics per 500 words. Most claims have sources. Mostly specific numbers with occasional vague quantifiers. |
| **50-69** | 1-2 statistics per 500 words. Some claims sourced. Mix of specific and vague numbers. |
| **30-49** | Less than 1 statistic per 500 words. Few sourced claims. Predominantly vague quantifiers. |
| **0-29** | No statistics. No sourced claims. All quantifiers are vague ("many," "most," "a lot"). |

**What counts as a statistic:**
- Specific percentages: "73% of marketers report..."
- Dollar amounts: "The average cost is $4,500 per month"
- Timeframes: "Implementation takes 6-8 weeks on average"
- Named studies: "According to the 2025 HubSpot State of Marketing Report..."
- Specific counts: "The platform integrates with 340+ tools"
- Comparison data: "40% faster than the industry average"

**What does NOT count:**
- "Many companies use..." (vague)
- "A significant percentage..." (vague)
- "Studies show that..." (no named source)
- "Experts agree..." (no named experts)


### Category 5: Uniqueness & Original Data (10% of total score)

This measures whether the content provides information that AI systems cannot find elsewhere, making it a necessary citation source.

**Scoring Criteria:**

| Score | Criteria |
|---|---|
| **90-100** | Contains first-party research, proprietary data, original surveys, or unique datasets. Presents analysis or insights not found on any other page. Clear methodological descriptions. |
| **70-89** | Contains some original insights or unique analysis of existing data. Offers a distinct perspective with original examples. |
| **50-69** | Mostly synthesizes existing information but adds some unique commentary or examples. |
| **30-49** | Largely derivative content that restates common knowledge with minimal original contribution. |
| **0-29** | Entirely derivative. All information is available (often verbatim) on higher-authority sources. |

**Signals of unique content:**
- "Our analysis of [X] data found..."
- "We surveyed [N] [professionals] and found..."
- "Based on our experience with [N] clients..."
- Custom charts, graphs, or data visualizations
- Case studies with specific named outcomes
- Original frameworks, methodologies, or taxonomies


## Analysis Procedure

### Step 1: Fetch and Parse Page Content

1. Use WebFetch to retrieve the target URL.
2. Extract the main content area (exclude navigation, footer, sidebar, ads).
3. Preserve heading structure (H1-H6 tags).
4. Preserve paragraph boundaries, lists, and tables.
5. Calculate total word count of main content.

### Step 2: Segment Content into Blocks

1. Split content at each heading (H2 or H3) to create content blocks.
2. For each block, record:
   - The heading text
   - The full text content under that heading
   - Word count of the block
   - Number of paragraphs
   - Number of lists and tables
   - Number of statistics/data points
   - Whether the block contains a definition pattern
   - Whether the first 60 words form a standalone answer

### Step 3: Score Each Block

For each content block, calculate:
- Answer Block Quality sub-score (0-100)
- Self-Containment sub-score (0-100)
- Structural Readability sub-score (0-100)
- Statistical Density sub-score (0-100)
- Uniqueness sub-score (0-100)

**Block Citability Score** = (Answer * 0.30) + (SelfContain * 0.25) + (Structure * 0.20) + (Stats * 0.15) + (Unique * 0.10)

### Step 4: Calculate Page-Level Score

1. Calculate the average of all block scores for the page-level citability score.
2. Identify the top 3 highest-scoring blocks (highlight as strengths).
3. Identify the bottom 3 lowest-scoring blocks (flag for rewriting).
4. Calculate the percentage of blocks scoring above 70 (the "citability coverage" metric).

### Step 5: Generate Rewrite Suggestions

For each block scoring below 60, generate a specific rewrite suggestion:
1. Identify the primary weakness (buried answer, lack of facts, poor structure, etc.).
2. Propose a rewritten opening sentence using a definition or answer-first pattern.
3. Suggest specific statistics or facts that could be added.
4. Recommend structural improvements (add list, add table, split paragraph).


## Output Format

Generate a file called `GEO-CITABILITY-SCORE.md`:

```markdown
# AI Citability Analysis: [Page Title]

**URL:** [URL]
**Analysis Date:** [Date]
**Overall Citability Score: [X]/100**
**Citability Coverage:** [X]% of content blocks score above 70


## Score Summary

| Category | Score | Weight | Weighted |
|---|---|---|---|
| Answer Block Quality | [X]/100 | 30% | [X] |
| Passage Self-Containment | [X]/100 | 25% | [X] |
| Structural Readability | [X]/100 | 20% | [X] |
| Statistical Density | [X]/100 | 15% | [X] |
| Uniqueness & Original Data | [X]/100 | 10% | [X] |
| **Overall** | | | **[X]/100** |


## Strongest Content Blocks

### 1. "[Heading]" -- Score: [X]/100
> [First 2 sentences of the block]

**Why it works:** [Explanation]

### 2. "[Heading]" -- Score: [X]/100
> [First 2 sentences of the block]

**Why it works:** [Explanation]


## Weakest Content Blocks (Rewrite Priority)

### 1. "[Heading]" -- Score: [X]/100

**Current opening:**
> [First 2 sentences as they exist]

**Problem:** [Specific issue -- buried answer, no facts, etc.]

**Suggested rewrite:**
> [Rewritten opening 2-3 sentences with answer-first pattern and facts]

**Additional improvements:**
- [Add table comparing X, Y, Z]
- [Include statistic about ...]
- [Split long paragraph into 2-3 shorter ones]


## Quick Win Reformatting Recommendations

1. **[Specific recommendation]** -- Expected citability lift: +[X] points
2. **[Specific recommendation]** -- Expected citability lift: +[X] points
3. **[Specific recommendation]** -- Expected citability lift: +[X] points
4. **[Specific recommendation]** -- Expected citability lift: +[X] points
5. **[Specific recommendation]** -- Expected citability lift: +[X] points


## Per-Section Scores

| Section Heading | Words | Answer Quality | Self-Contained | Structure | Stats | Unique | Overall |
|---|---|---|---|---|---|---|---|
| [H2 heading] | [N] | [X] | [X] | [X] | [X] | [X] | [X] |
```


## Reference Data

### Optimal Passage Characteristics (from GEO Research)

- **Optimal length for AI citation:** 134-167 words (Bortolato 2025 analysis of AI Overview passages)
- **Definition patterns increase citation rate by:** 2.1x (Georgia Tech 2024)
- **Adding statistics to passages increases citation by:** 40% (Princeton GEO study 2024)
- **Adding quotations from authorities increases citation by:** 115% in certain categories (IIT Delhi 2024)
- **Fluency optimization increases visibility by:** 30% on average across all query types
- **Content with source citations is cited:** 20-25% more often by Perplexity and ChatGPT search

### AI System Citation Preferences

| AI System | Citation Preference |
|---|---|
| **ChatGPT (Search)** | Prefers passages with explicit definitions, named sources, and recent dates. Tends to cite 2-4 sources per response. |
| **Perplexity** | Heavily favors fact-dense passages with statistics. Cites 4-8 sources per response. Values recency highly. |
| **Claude** | Prefers well-structured, comprehensive passages. Values nuance and accuracy over brevity. |
| **Gemini (AI Overviews)** | Prefers concise answer blocks (40-60 words). Values content already ranking in top 10 organic results. |
| **Copilot (Bing)** | Similar to Gemini. Prefers passages from high-authority domains with clear factual claims. |


---


# AI Crawler Access Analysis Skill

## Purpose

This skill analyzes a website's accessibility to AI crawlers -- the bots that AI companies use to discover, index, and train on web content. If AI crawlers are blocked, the site's content cannot appear in AI-generated responses regardless of its quality. Crawler access is the foundational technical requirement for GEO.

## Key Insight

As of early 2026, many websites inadvertently block AI crawlers through overly aggressive robots.txt rules, inherited from legacy SEO configurations. A Originality.ai 2025 study found that over 35% of the top 1,000 websites block at least one major AI crawler, and 5-10% block all AI crawlers. Blocking AI crawlers is the single fastest way to become invisible in AI-generated search results.


## Complete AI Crawler Reference

### Tier 1: Critical for AI Search Visibility (RECOMMEND: ALLOW)

These crawlers power the AI search products where users actively look for answers. Blocking them directly reduces your visibility in AI-generated responses.

#### GPTBot
- **Operator:** OpenAI
- **User-Agent:** `GPTBot`
- **Full User-Agent String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.2; +https://openai.com/gptbot)`
- **Purpose:** Fetches content for ChatGPT's web browsing, plugins, and search features. Content accessed by GPTBot may be used to improve OpenAI models.
- **Impact of Blocking:** Content will NOT appear in ChatGPT Search results or be accessible when users ask ChatGPT to browse the web. This is the highest-impact AI crawler to allow.
- **Recommendation:** **ALLOW** -- ChatGPT has 300M+ weekly active users as of 2025. Blocking GPTBot removes your content from one of the largest AI search surfaces.

#### OAI-SearchBot
- **Operator:** OpenAI
- **User-Agent:** `OAI-SearchBot`
- **Full User-Agent String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.0; +https://docs.openai.com/bots/overview)`
- **Purpose:** Specifically powers ChatGPT's search feature. Unlike GPTBot, content accessed by OAI-SearchBot is NOT used for model training -- only for live search results.
- **Impact of Blocking:** Content will not appear in ChatGPT's search results even if GPTBot is allowed.
- **Recommendation:** **ALLOW** -- This is a search-only crawler with no training implications. There is no strategic reason to block it.

#### ChatGPT-User
- **Operator:** OpenAI
- **User-Agent:** `ChatGPT-User`
- **Full User-Agent String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ChatGPT-User/1.0; +https://openai.com/bot)`
- **Purpose:** Used when a ChatGPT user explicitly asks the model to visit a specific URL. Acts like a browser agent on behalf of the user.
- **Impact of Blocking:** ChatGPT cannot visit your pages when users ask it to read or summarize them. This prevents direct user-initiated traffic.
- **Recommendation:** **ALLOW** -- Blocking this bot prevents users who are actively trying to engage with your content from accessing it through ChatGPT.

#### ClaudeBot
- **Operator:** Anthropic
- **User-Agent:** `ClaudeBot`
- **Full User-Agent String:** `ClaudeBot/1.0; +https://www.anthropic.com/claude-bot`
- **Purpose:** Fetches web content for Claude's features including web search, citations, and analysis tools.
- **Impact of Blocking:** Content will not be accessible to Claude for web search or when users ask Claude to analyze specific URLs.
- **Recommendation:** **ALLOW** -- Claude is a major AI assistant with growing market share. Blocking ClaudeBot reduces your AI search footprint.

#### PerplexityBot
- **Operator:** Perplexity AI
- **User-Agent:** `PerplexityBot`
- **Full User-Agent String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`
- **Purpose:** Powers Perplexity's AI search engine, which provides sourced answers with direct citations and links back to source pages.
- **Impact of Blocking:** Content will not appear in Perplexity search results. Perplexity is one of the best referral traffic sources among AI search products because it always displays source links.
- **Recommendation:** **ALLOW** -- Perplexity drives actual referral traffic and always attributes sources. High-value AI crawler for publishers and businesses.


### Tier 2: Important for Broader AI Ecosystem (RECOMMEND: ALLOW)

These crawlers serve large AI platforms or search ecosystems. Allowing them increases your content's reach.

#### Google-Extended
- **Operator:** Google
- **User-Agent:** `Google-Extended`
- **Purpose:** Controls whether Google uses your content for Gemini model training and AI Overviews improvement. **CRITICAL NOTE:** Blocking Google-Extended does NOT affect your Google Search rankings or your appearance in Google Search results. That is controlled by the standard Googlebot.
- **Impact of Blocking:** Content may not be used for Gemini training or to improve AI Overviews. However, your content can still appear in AI Overviews based on standard search indexing.
- **Recommendation:** **ALLOW** -- Blocking provides minimal content protection upside while reducing your presence in Google's AI features. Since it does not affect standard search ranking, the only reason to block is philosophical objection to training data usage.

#### GoogleOther
- **Operator:** Google
- **User-Agent:** `GoogleOther`
- **Purpose:** Used by Google for various non-search-ranking purposes including research, one-off crawls, and AI-related data collection.
- **Impact of Blocking:** Minimal impact on search rankings. May reduce presence in Google's AI research and experimental features.
- **Recommendation:** **ALLOW** -- Low risk, moderate potential benefit for AI feature inclusion.

#### Applebot-Extended
- **Operator:** Apple
- **User-Agent:** `Applebot-Extended`
- **Purpose:** Used by Apple to train and improve Apple Intelligence features, Siri, and Apple's AI products. Separate from standard Applebot (which powers Siri search and Spotlight Suggestions).
- **Impact of Blocking:** Content may not be used in Apple Intelligence features. Standard Siri and Spotlight functionality is unaffected (controlled by Applebot).
- **Recommendation:** **ALLOW** -- Apple Intelligence is integrated into all Apple devices (2B+ active devices). Presence in Apple's AI features has growing strategic value.

#### Amazonbot
- **Operator:** Amazon
- **User-Agent:** `Amazonbot`
- **Full User-Agent String:** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (compatible; Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)`
- **Purpose:** Indexes content for Alexa answers and Amazon's AI features.
- **Impact of Blocking:** Content will not appear in Alexa voice responses or Amazon's AI-powered search features.
- **Recommendation:** **ALLOW** -- Relevant for voice search optimization. Lower priority than Tier 1 crawlers but no downside to allowing.

#### FacebookBot
- **Operator:** Meta
- **User-Agent:** `FacebookBot`
- **Purpose:** Used by Meta for AI features across Facebook, Instagram, WhatsApp, and Meta AI assistant.
- **Impact of Blocking:** Content may not be accessible to Meta AI. Link previews on Facebook/Instagram are handled by a different crawler and are unaffected.
- **Recommendation:** **ALLOW** -- Meta AI is embedded in apps with 3B+ combined users. Growing importance for AI visibility.


### Tier 3: Training-Only Crawlers (ALLOW or BLOCK Based on Strategy)

These crawlers are primarily used for AI model training rather than live search features. Blocking them does not affect AI search visibility.

#### CCBot
- **Operator:** Common Crawl (nonprofit)
- **User-Agent:** `CCBot`
- **Full User-Agent String:** `CCBot/2.0 (https://commoncrawl.org/faq/)`
- **Purpose:** Builds the Common Crawl dataset, which is used as training data by many AI companies (Google, Meta, Stability AI, and others).
- **Impact of Blocking:** Content will not appear in future Common Crawl datasets. Does NOT affect any live AI search product.
- **Recommendation:** **CONTEXT-DEPENDENT** -- Allow if you want maximum long-term AI training presence. Block if you want to control training data usage. No impact on search visibility.

#### anthropic-ai
- **Operator:** Anthropic
- **User-Agent:** `anthropic-ai`
- **Purpose:** Used by Anthropic for AI safety research and Claude model training. Separate from ClaudeBot (which powers live features).
- **Impact of Blocking:** Content will not be used for Claude training. Does NOT affect Claude's live search or web browsing features (controlled by ClaudeBot).
- **Recommendation:** **CONTEXT-DEPENDENT** -- Similar to CCBot. Allow for training presence, block for training data control. No impact on live AI search.

#### Bytespider
- **Operator:** ByteDance
- **User-Agent:** `Bytespider`
- **Purpose:** Used by ByteDance for various AI products including TikTok's AI features and Doubao (their ChatGPT competitor in China).
- **Impact of Blocking:** Content will not be used for ByteDance AI products. Minimal impact for Western-market businesses.
- **Recommendation:** **BLOCK** for most Western businesses (aggressive crawling behavior reported, minimal search visibility benefit). **ALLOW** if targeting Chinese/Asian markets.

#### cohere-ai
- **Operator:** Cohere
- **User-Agent:** `cohere-ai`
- **Purpose:** Used by Cohere for model training. Cohere powers enterprise AI solutions and the Coral chat product.
- **Impact of Blocking:** Content will not be used for Cohere model training. Minimal direct consumer-facing impact.
- **Recommendation:** **CONTEXT-DEPENDENT** -- Low priority. Allow or block based on general training data stance.


## Recommendation Matrix Summary

| Crawler | Tier | Recommendation | Reason |
|---|---|---|---|
| GPTBot | 1 | **ALLOW** | Powers ChatGPT Search (300M+ users) |
| OAI-SearchBot | 1 | **ALLOW** | Search-only, no training use |
| ChatGPT-User | 1 | **ALLOW** | User-initiated browsing |
| ClaudeBot | 1 | **ALLOW** | Claude web search and analysis |
| PerplexityBot | 1 | **ALLOW** | Best referral traffic AI search |
| Google-Extended | 2 | **ALLOW** | Gemini features; no search rank impact |
| GoogleOther | 2 | **ALLOW** | Google AI research |
| Applebot-Extended | 2 | **ALLOW** | Apple Intelligence (2B+ devices) |
| Amazonbot | 2 | **ALLOW** | Alexa and Amazon AI |
| FacebookBot | 2 | **ALLOW** | Meta AI (3B+ app users) |
| CCBot | 3 | Context | Training data only |
| anthropic-ai | 3 | Context | Training data only |
| Bytespider | 3 | **BLOCK** | Aggressive crawler, low benefit |
| cohere-ai | 3 | Context | Training data only |

### Maximum AI Visibility Configuration (robots.txt)

For sites wanting maximum AI search visibility:

```
# AI Crawlers - ALLOWED for AI search visibility
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GoogleOther
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: FacebookBot
Allow: /

# AI Crawlers - BLOCKED (aggressive/low value)
User-agent: Bytespider
Disallow: /

User-agent: CCBot
Disallow: /
```


## Analysis Procedure

### Step 1: Fetch and Parse robots.txt

1. Use WebFetch to retrieve `[domain]/robots.txt`.
2. Parse all User-agent directives and their associated Allow/Disallow rules.
3. For each AI crawler in the reference list above:
   - Check if there is a specific User-agent block for that crawler
   - Check if there is a wildcard (`User-agent: *`) block that would apply
   - Determine effective access: **Allowed**, **Blocked**, or **Not Mentioned** (inherits wildcard rules)
4. Note any `Crawl-delay` directives that may slow AI crawler access.
5. Check for `Sitemap` directives (AI crawlers use these for discovery).

### Step 2: Check Meta Robots Tags

1. For a sample of 5-10 key pages, fetch the HTML and check for:
   - `<meta name="robots" content="noindex">` -- blocks all bots
   - `<meta name="robots" content="nofollow">` -- prevents link following
   - `<meta name="robots" content="noai">` -- emerging tag to block AI use
   - `<meta name="robots" content="noimageai">` -- blocks AI image training
   - Bot-specific meta tags: `<meta name="GPTBot" content="noindex">`
2. Record any page-level overrides of the robots.txt directives.

### Step 3: Check HTTP Headers

1. For the same sample pages, check response headers for:
   - `X-Robots-Tag: noindex` -- HTTP header equivalent of meta noindex
   - `X-Robots-Tag: noai` -- HTTP header to block AI use
   - `X-Robots-Tag: noimageai` -- blocks AI image training
   - Bot-specific headers: `X-Robots-Tag: GPTBot: noindex`
2. Note that HTTP headers override meta tags and apply to non-HTML resources too.

### Step 4: Check for AI-Specific Files

1. Check for `/llms.txt` (emerging standard for AI crawler guidance).
2. Check for `/.well-known/ai-plugin.json` (OpenAI plugin manifest).
3. Check for `/ai.txt` (proposed standard, similar to ads.txt for AI).
4. Record presence/absence and quality of each file.

### Step 5: Assess JavaScript Rendering Requirements

1. Check if the site is a Single Page Application (SPA) or heavily JavaScript-rendered.
2. AI crawlers vary in their JavaScript rendering capabilities:
   - GPTBot: Limited JS rendering
   - ClaudeBot: Limited JS rendering
   - PerplexityBot: Limited JS rendering
   - Googlebot: Full JS rendering (but Google-Extended inherits this)
3. If critical content requires JS rendering, flag this as a potential issue.
4. Check for Server-Side Rendering (SSR) or Static Site Generation (SSG) as mitigations.


## Output Format

Generate a file called `GEO-CRAWLER-ACCESS.md`:

```markdown
# AI Crawler Access Report: [Domain]

**Analysis Date:** [Date]
**Domain:** [Domain]
**robots.txt Status:** [Found/Not Found/Error]


## Crawler Access Summary

| Crawler | Operator | Tier | Status | Impact |
|---|---|---|---|---|
| GPTBot | OpenAI | 1 | [Allowed/Blocked/Not Mentioned] | [Impact description] |
| OAI-SearchBot | OpenAI | 1 | [Status] | [Impact] |
| ChatGPT-User | OpenAI | 1 | [Status] | [Impact] |
| ClaudeBot | Anthropic | 1 | [Status] | [Impact] |
| PerplexityBot | Perplexity | 1 | [Status] | [Impact] |
| Google-Extended | Google | 2 | [Status] | [Impact] |
| GoogleOther | Google | 2 | [Status] | [Impact] |
| Applebot-Extended | Apple | 2 | [Status] | [Impact] |
| Amazonbot | Amazon | 2 | [Status] | [Impact] |
| FacebookBot | Meta | 2 | [Status] | [Impact] |
| CCBot | Common Crawl | 3 | [Status] | [Impact] |
| anthropic-ai | Anthropic | 3 | [Status] | [Impact] |
| Bytespider | ByteDance | 3 | [Status] | [Impact] |
| cohere-ai | Cohere | 3 | [Status] | [Impact] |

## AI Visibility Score: [X]/100

**Tier 1 Access:** [X/5 crawlers allowed]
**Tier 2 Access:** [X/5 crawlers allowed]
**Tier 3 Access:** [X/4 crawlers allowed]


## Critical Issues

[List any Tier 1 crawlers that are blocked]

## Recommendations

### Immediate Actions
[Specific robots.txt changes needed]

### robots.txt Recommendation
```
[Complete recommended robots.txt content for AI crawlers]
```

### Additional Technical Findings
- **Meta Robots Tags:** [Findings]
- **X-Robots-Tag Headers:** [Findings]
- **JavaScript Rendering:** [Assessment]
- **llms.txt:** [Present/Absent]
- **Sitemap Accessibility:** [Assessment]
```


## Scoring for Crawler Access

The AI Crawler Access Score is calculated as:

| Component | Weight | Scoring |
|---|---|---|
| Tier 1 Crawlers Allowed | 50% | 20 points per Tier 1 crawler allowed (5 crawlers = 100 points max, scaled to 50) |
| Tier 2 Crawlers Allowed | 25% | 20 points per Tier 2 crawler allowed (5 crawlers = 100 points max, scaled to 25) |
| No Blanket AI Blocks | 15% | Full points if no `User-agent: *` Disallow: / and no noai meta tags |
| AI-Specific Files Present | 10% | 5 points for llms.txt, 5 points for sitemap accessible to AI crawlers |

Final score = sum of all weighted components, capped at 100.


---


# llms.txt Standard Analysis and Generation Skill

## Purpose

This skill handles everything related to the `llms.txt` standard -- an emerging convention (proposed by Jeremy Howard in September 2024, gaining adoption through 2025-2026) that allows websites to provide structured guidance to AI systems about their content, structure, and key information. It is analogous to `robots.txt` (which tells crawlers what NOT to access) but instead tells AI systems what IS most useful to understand about the site.

## Why llms.txt Matters

AI language models face a fundamental challenge when processing websites: they must determine which pages are most important, what the site is about, and how content is organized -- typically by crawling many pages and inferring structure. `llms.txt` solves this by providing an explicit, machine-readable (and human-readable) summary.

**Benefits of having a well-crafted llms.txt:**

1. **Faster AI comprehension:** AI systems can understand your site's purpose and structure from a single file rather than crawling dozens of pages.
2. **Controlled narrative:** You choose which pages and facts AI systems see first, shaping how they represent your brand.
3. **Higher citation accuracy:** AI systems that consult llms.txt can cite the correct, authoritative page for each topic.
4. **Reduced misrepresentation:** Key facts (pricing, features, locations) are stated explicitly, reducing AI hallucination about your business.
5. **Early adopter advantage:** As of early 2026, fewer than 5% of websites have an llms.txt file, making it a differentiator.


## The llms.txt Specification

### File Location

The file MUST be located at the root of the domain:
```
https://example.com/llms.txt
```

### Format Specification

The file uses Markdown formatting with specific conventions:

```markdown
# [Site Name]

> [One-sentence description of what the site/business does. Keep under 200 characters.]

## Docs

- [Page Title](https://example.com/page-url): Concise description of what this page covers and why it matters.
- [Another Page](https://example.com/another-page): Description of content.

## Optional

- [Less Critical Page](https://example.com/optional-page): Description.
```

### Detailed Format Rules

**1. Title (Required)**
```markdown
# Site Name
```
- Must be the first line of the file.
- Should be the official business/site name.
- Use the H1 heading format (single `#`).

**2. Description (Required)**
```markdown
> Brief description of the site/business
```
- Must appear immediately after the title.
- Use Markdown blockquote format (`>`).
- Keep under 200 characters.
- Should clearly state what the business does and who it serves.
- Avoid marketing fluff -- be factual and specific.

**3. Main Sections (Required -- at least one)**

Use H2 headings (`##`) to organize pages by category. Common section names:

| Section Name | Purpose | Example Content |
|---|---|---|
| `## Docs` | Primary documentation or key pages | Product pages, service descriptions, core content |
| `## Optional` | Secondary pages worth knowing about | Blog posts, supplementary resources |
| `## API` | API documentation | API reference, authentication guides |
| `## Blog` | Blog or news content | Recent/popular articles |
| `## Products` | Product catalog | Product pages, pricing |
| `## Services` | Service offerings | Service descriptions, process pages |
| `## About` | Company information | About page, team, mission |
| `## Resources` | Educational/reference content | Guides, tutorials, whitepapers |
| `## Legal` | Legal documents | Terms of service, privacy policy |
| `## Contact` | Contact information | Contact page, support channels |

**4. Page Entries (Required)**

Each entry follows the format:
```markdown
- [Page Title](URL): Description of page content
```

Rules for page entries:
- **Title:** Use the actual page title or a clear descriptive title.
- **URL:** Must be a full, absolute URL (not relative paths).
- **Description:** 10-30 words describing what the page covers. Be specific about the information available.
- **Order:** List pages in order of importance within each section.
- **Limit:** Include 10-30 page entries total. Prioritize your most authoritative and useful pages.

**5. Key Facts Section (Recommended)**

```markdown
## Key Facts
- Founded in [year] by [founder(s)]
- Headquarters: [City, Country]
- [X] customers/users in [Y] countries
- Key products: [Product A], [Product B], [Product C]
- Industry: [Industry classification]
```

This section provides quick reference data that AI systems frequently need to answer user queries about your business.

**6. Contact Section (Recommended)**

```markdown
## Contact
- Website: https://example.com
- Email: hello@example.com
- Support: support@example.com
- Phone: +1-555-123-4567
- Address: 123 Main St, City, State, ZIP, Country
```


## llms-full.txt (Extended Version)

In addition to `llms.txt`, sites can provide `/llms-full.txt` -- an extended version with more detail.

**Differences from llms.txt:**

| Feature | llms.txt | llms-full.txt |
|---|---|---|
| **Length** | Concise (50-150 lines) | Comprehensive (150-500+ lines) |
| **Page entries** | 10-30 key pages | 30-100+ pages |
| **Descriptions** | 10-30 words per entry | 30-100 words per entry, may include key facts from each page |
| **Audience** | Quick AI comprehension | Deep AI analysis |
| **Sections** | 3-6 sections | 8-15 sections |
| **Key facts** | Business-level facts | Page-level facts and data points |

Both files can coexist. AI systems check for `llms.txt` first, then may optionally load `llms-full.txt` for deeper understanding.


## Analysis Mode

When checking an existing llms.txt file:

### Step 1: Fetch the File

1. Use WebFetch to retrieve `[domain]/llms.txt`.
2. Also check for `[domain]/llms-full.txt`.
3. Record HTTP status code:
   - **200:** File exists -- proceed to validation.
   - **404:** File does not exist -- recommend generation.
   - **403:** File exists but is blocked -- flag as misconfiguration.
   - **301/302:** Redirect -- follow and note the redirect.

### Step 2: Validate Format

Check each structural element:

| Element | Check | Severity if Missing |
|---|---|---|
| H1 Title | Present, matches business name | Critical |
| Blockquote description | Present, under 200 chars, factual | High |
| At least one H2 section | Present | Critical |
| Page entries with URLs | At least 5 entries present | High |
| URLs are absolute | All URLs use full https:// paths | High |
| URLs are valid | All URLs return 200 status | Medium |
| Descriptions present | Every entry has a description after the colon | Medium |
| Key Facts section | Present with business information | Medium |
| Contact section | Present with at least email | Low |
| Reasonable length | 30-200 lines | Low |
| No broken Markdown | Proper formatting throughout | Medium |

### Step 3: Assess Content Quality

Rate the llms.txt on these dimensions:

**Completeness (0-100):**
- Does it cover all major site sections visible in the navigation?
- Are the most important/highest-traffic pages included?
- Is the Key Facts section present with accurate business data?
- Does it include recent/updated content?

**Accuracy (0-100):**
- Do descriptions accurately reflect page content?
- Are URLs valid and pointing to the correct pages?
- Are Key Facts verifiable and current?
- Is the business description accurate?

**Usefulness (0-100):**
- Would an AI system understand the site's purpose from this file alone?
- Are descriptions specific enough to differentiate pages?
- Are the most citation-worthy pages highlighted?
- Is the organization logical and intuitive?

**Overall llms.txt Score** = (Completeness * 0.40) + (Accuracy * 0.35) + (Usefulness * 0.25)

### Step 4: Compare Against Site Content

1. Crawl the site's main navigation and sitemap.
2. Identify important pages NOT listed in llms.txt.
3. Check if any listed URLs are broken or redirected.
4. Verify that the business description matches current homepage messaging.
5. Flag stale entries (pages that have been significantly updated since the llms.txt was written).


## Generation Mode

When creating a new llms.txt file from scratch:

### Step 1: Site Discovery

1. Fetch the homepage and extract:
   - Site name (from `<title>`, `<meta property="og:site_name">`, or H1)
   - Business description (from meta description or hero section)
   - Main navigation links
   - Footer links
2. Fetch `/sitemap.xml` to discover all public pages.
3. Identify the site's primary business type (SaaS, E-commerce, Local, Publisher, Agency).

### Step 2: Page Prioritization

Categorize all discovered pages and select the most important ones:

**Always Include:**
- Homepage
- About / Company page
- Pricing page (if exists)
- Primary product/service pages (top 3-5)
- Contact page
- Documentation landing page (if exists)

**Include if High Quality:**
- Top blog posts (by apparent importance, recency, or comprehensiveness)
- Case studies or customer stories
- Key resource/guide pages
- FAQ page
- Careers page (for large companies)

**Skip:**
- Thin category/tag pages
- Pagination pages
- Login/signup pages
- Legal boilerplate (unless specifically relevant)
- Duplicate or near-duplicate content
- Pages with minimal unique content

### Step 3: Write Descriptions

For each selected page:

1. Fetch the page content using WebFetch.
2. Read the H1, meta description, and first 2-3 paragraphs.
3. Write a description that:
   - Is 10-30 words long
   - States what information is on the page
   - Mentions specific topics, data, or features covered
   - Avoids marketing language ("best," "leading," "revolutionary")
   - Uses factual, informative language

**Good description examples:**
- `Explains the three pricing tiers (Free, Pro, Enterprise) with feature comparison and annual/monthly costs.`
- `Details the company's founding in 2018, team of 45 employees, and office locations in Austin and London.`
- `Covers integration setup for Slack, Salesforce, and HubSpot with step-by-step guides and API endpoints.`

**Bad description examples:**
- `Our amazing pricing page!` (marketing language, no specifics)
- `Learn more about our company.` (too vague)
- `Click here for details.` (not descriptive)

### Step 4: Compile Key Facts

Gather key business facts from the site:

- Year founded
- Founder name(s)
- Headquarters location
- Number of employees (if public)
- Number of customers/users (if public)
- Key products or services (list top 3-5)
- Industry classification
- Notable clients or partnerships (if public)
- Key differentiators (what makes this business unique)
- Recent milestones or achievements (last 12 months)

### Step 5: Assemble the File

Construct the llms.txt following this template:

```markdown
# [Site Name]

> [One clear sentence: what the business does, who it serves, and its primary value proposition. Under 200 characters.]

## Docs

- [Most Important Page](https://example.com/page): Description covering the key content on this page.
- [Second Page](https://example.com/page-2): Description of this page's content and value.
- [Third Page](https://example.com/page-3): What users and AI systems will find here.

## Products

- [Product A](https://example.com/product-a): Core features, target users, and pricing model for Product A.
- [Product B](https://example.com/product-b): What Product B does and how it differs from Product A.

## Resources

- [Guide Title](https://example.com/guide): Comprehensive guide covering [topic] with [X] sections and practical examples.
- [Blog Post](https://example.com/blog/post): Analysis of [topic] with original data from [source].

## Key Facts

- Founded in [year] by [name(s)]
- Headquartered in [City, Country]
- [Specific metric: e.g., "Serves 10,000+ businesses in 40 countries"]
- [Key differentiator: e.g., "Only platform offering real-time X and Y integration"]
- Industry: [Classification]

## Contact

- Website: https://example.com
- Email: [primary contact email]
- Support: [support URL or email]
```

### Step 6: Validate the Generated File

Before outputting:
1. Verify all URLs are reachable (200 status).
2. Confirm total entry count is between 10-30.
3. Check that no description exceeds 50 words.
4. Verify the overall file length is 50-150 lines.
5. Ensure Markdown formatting is clean and consistent.


## Output Format

### For Analysis Mode

Generate `GEO-LLMSTXT-ANALYSIS.md`:

```markdown
# llms.txt Analysis: [Domain]

**Analysis Date:** [Date]
**llms.txt Status:** [Found at URL / Not Found / Error]
**llms-full.txt Status:** [Found / Not Found]


## Overall llms.txt Score: [X]/100

| Dimension | Score |
|---|---|
| Completeness | [X]/100 |
| Accuracy | [X]/100 |
| Usefulness | [X]/100 |


## Format Validation

| Element | Status | Notes |
|---|---|---|
| H1 Title | [Pass/Fail] | [Notes] |
| Description blockquote | [Pass/Fail] | [Notes] |
| H2 Sections | [Pass/Fail] | [X sections found] |
| Page entries | [Pass/Fail] | [X entries found] |
| URL validity | [Pass/Fail] | [X broken URLs] |
| Entry descriptions | [Pass/Fail] | [X missing descriptions] |
| Key Facts | [Pass/Fail] | [Notes] |
| Contact section | [Pass/Fail] | [Notes] |


## Missing Pages

These important pages were found on the site but not in llms.txt:

1. [Page Title](URL) -- [Why it should be included]
2. [Page Title](URL) -- [Why it should be included]

## Improvement Recommendations

1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]

## Suggested Updated llms.txt

[Complete rewritten llms.txt file if significant improvements are needed]
```

### For Generation Mode

Output the complete `llms.txt` file content, ready to be saved to the site's root directory. Also output a brief `GEO-LLMSTXT-GENERATION.md` report explaining:
- How many pages were discovered and how many were selected
- The prioritization rationale
- Any pages that were borderline (might add later)
- Recommended update frequency (e.g., monthly for active blogs, quarterly for stable sites)


## Best Practices Reference

1. **Update regularly.** If your site publishes weekly blog posts, update llms.txt monthly. If your product changes quarterly, update after each release.
2. **Lead with your strongest content.** The first entries in each section should be your most authoritative, comprehensive pages.
3. **Be specific in descriptions.** "Comprehensive 3,000-word guide to React Server Components with code examples" is far more useful than "React guide."
4. **Include your differentiators.** If your site has unique data, original research, or exclusive features, highlight these in descriptions and Key Facts.
5. **Keep it concise.** The llms.txt should be scannable in under 60 seconds. Save detail for llms-full.txt.
6. **Use absolute URLs.** Always include the full `https://` URL, never relative paths.
7. **Test after deployment.** After uploading, verify the file is accessible at `https://yourdomain.com/llms.txt` with no redirects.
8. **Coordinate with robots.txt.** Ensure pages listed in llms.txt are not blocked in robots.txt for AI crawlers.
9. **Mirror your site structure.** Section names in llms.txt should roughly correspond to your main navigation categories.
10. **Avoid sensitive pages.** Do not include internal tools, admin panels, or pages with sensitive information.


---


# Brand Mention Scanner Skill

## Core Insight

Brand mentions correlate approximately 3x more strongly with AI visibility than traditional backlinks. An Ahrefs study published in December 2025, analyzing 75,000 brands across AI search platforms, found that **unlinked brand mentions** -- references to a brand name without a hyperlink -- are a stronger predictor of whether AI systems cite and recommend a brand than Domain Rating or backlink count.

The critical finding: **the platform where the mention appears matters enormously.** Not all mentions are equal. A mention on YouTube or Reddit carries far more weight for AI citation than a mention on a low-authority blog, because AI training data and retrieval systems disproportionately index high-engagement platforms.

This inverts a core assumption of traditional SEO. In traditional SEO, a backlink from a high-DR site is the gold standard. In GEO, an unlinked mention on Reddit or a YouTube video description may be more valuable than a dofollow backlink from a DR 70 blog.


## Platform Importance Ranking for AI Citations

Based on the Ahrefs December 2025 study and corroborating research from Profound (2025) and Terakeet (2025):

### 1. YouTube Mentions -- Correlation ~0.737 (STRONGEST)

**Why YouTube matters most:**
- YouTube is the second-largest search engine and the largest video platform globally (2.5B+ monthly users).
- AI training datasets heavily incorporate YouTube transcripts, descriptions, and metadata.
- Google's Gemini and AI Overviews directly reference YouTube content.
- Perplexity and ChatGPT both index and cite YouTube video content.
- YouTube transcripts are particularly valuable because they contain natural language mentions in conversational context, which aligns with how AI models process and generate text.

**What to check:**
- **Brand YouTube channel:** Does the brand have an active YouTube channel? How many subscribers? Video count? Upload frequency?
- **Third-party video mentions:** Are other YouTubers or channels mentioning the brand? In what context (reviews, tutorials, comparisons)?
- **Video descriptions:** Does the brand name appear in video descriptions of industry-relevant content?
- **Video transcripts:** Is the brand mentioned in spoken content of relevant videos? (AI models index transcripts)
- **YouTube search presence:** When searching "[brand name]" on YouTube, do results appear? Are they positive?
- **Comment mentions:** Is the brand mentioned in comments on relevant industry videos?

**Scoring for YouTube (0-100):**

| Score | Criteria |
|---|---|
| 90-100 | Active channel with 10K+ subscribers, regular uploads, brand mentioned in 20+ third-party videos, appears in YouTube search results for industry terms |
| 70-89 | Active channel with 1K+ subscribers, brand mentioned in 10-19 third-party videos, some YouTube search presence |
| 50-69 | Channel exists with some content, brand mentioned in 5-9 third-party videos, limited YouTube search presence |
| 30-49 | Channel exists but inactive, brand mentioned in 1-4 third-party videos |
| 10-29 | No channel or empty channel, brand mentioned in 1-2 videos only |
| 0-9 | No YouTube presence whatsoever |


### 2. Reddit Mentions -- High Correlation

**Why Reddit matters:**
- Reddit is one of the most heavily indexed platforms in AI training data (confirmed in Google's $60M/year Reddit licensing deal, 2024).
- AI systems heavily weight Reddit for product recommendations, comparisons, and user sentiment.
- "Reddit" is now appended to an estimated 10-15% of Google searches by users seeking authentic opinions.
- Perplexity frequently cites Reddit threads as sources.
- ChatGPT and Claude both reference Reddit discussions when answering product/service questions.

**What to check:**
- **Subreddit presence:** Is the brand discussed in relevant subreddits? Which ones?
- **Mention volume:** How many Reddit threads mention the brand? What is the trend (increasing/decreasing)?
- **Sentiment:** Are mentions mostly positive, negative, or neutral? What are common praise points and complaints?
- **Official presence:** Does the brand have an official Reddit account? Do they participate in discussions? Have they done AMAs?
- **Recommendation threads:** Does the brand appear in "What do you recommend for X?" threads? Is it the top recommendation or an also-ran?
- **Subreddit community:** Does the brand have its own subreddit? How active is it?

**Scoring for Reddit (0-100):**

| Score | Criteria |
|---|---|
| 90-100 | Frequently recommended in relevant subreddits, predominantly positive sentiment, active official presence, own subreddit with 5K+ members, appears in top recommendations for industry queries |
| 70-89 | Regularly mentioned in relevant subreddits, mostly positive sentiment, some official presence, appears in multiple recommendation threads |
| 50-69 | Mentioned in several relevant threads, mixed sentiment, brand name is recognized by community members |
| 30-49 | Occasional mentions, limited to 1-2 subreddits, no official presence |
| 10-29 | Rare mentions, brand largely unknown on Reddit |
| 0-9 | No Reddit presence |


### 3. Wikipedia Presence -- High Correlation

**Why Wikipedia matters:**
- Wikipedia is one of the highest-authority sources in AI training data. All major AI models have been trained on Wikipedia dumps.
- AI systems use Wikipedia as a primary source for entity recognition -- determining whether a brand is a "real" entity worth knowing about.
- Wikidata (Wikipedia's structured data sibling) provides machine-readable facts that AI models use for knowledge graph construction.
- Having a Wikipedia page is a strong signal of notability, which correlates with AI systems treating the brand as an authoritative entity.

**What to check:**
- **Wikipedia page:** Does the brand or company have its own Wikipedia article? Is it marked for deletion or quality issues?
- **Founder page:** Does the founder/CEO have a Wikipedia page? (Strong authority signal)
- **Wikipedia citations:** Is the brand's website cited as a reference in any Wikipedia articles?
- **Wikidata entry:** Does the brand have a Wikidata item (Q-number)? How complete is it?
- **Wikipedia mentions:** Is the brand mentioned in other Wikipedia articles (industry articles, competitor pages, category pages)?
- **Article quality:** If a Wikipedia page exists, is it a stub, start-class, or higher quality?

**Scoring for Wikipedia (0-100):**

| Score | Criteria |
|---|---|
| 90-100 | Detailed Wikipedia article (B-class or higher), Wikidata entry with complete properties, brand cited as reference in multiple articles, founder has Wikipedia page |
| 70-89 | Wikipedia article exists (start-class or higher), Wikidata entry exists, brand mentioned in 2+ other Wikipedia articles |
| 50-69 | Wikipedia article exists (stub or start), basic Wikidata entry, limited mentions in other articles |
| 30-49 | No Wikipedia article but brand is mentioned in other articles or cited as reference; Wikidata entry may exist |
| 10-29 | Brand mentioned in 1-2 Wikipedia articles as a passing reference only |
| 0-9 | No Wikipedia or Wikidata presence of any kind |


### 4. LinkedIn Presence -- Moderate Correlation

**Why LinkedIn matters:**
- LinkedIn content is increasingly indexed by AI systems for professional and B2B context.
- Company LinkedIn pages and employee thought leadership posts build brand entity signals.
- AI models reference LinkedIn for company information, team credentials, and professional authority.
- LinkedIn articles and posts are indexed by search engines and AI crawlers.

**What to check:**
- **Company page:** Does the brand have a LinkedIn company page? Follower count? Post frequency?
- **Employee thought leadership:** Are employees (especially leadership) posting thought leadership content that mentions the brand?
- **Company mentions:** Is the brand mentioned in LinkedIn posts by non-employees? Industry analysts? Customers?
- **LinkedIn articles:** Are there long-form LinkedIn articles about or mentioning the brand?
- **Employee profiles:** Do employees list the company with detailed descriptions? Do they have strong professional profiles?
- **Engagement metrics:** What is the typical engagement (likes, comments, shares) on company posts?

**Scoring for LinkedIn (0-100):**

| Score | Criteria |
|---|---|
| 90-100 | Active company page with 10K+ followers, leadership regularly posts thought leadership, brand frequently mentioned by industry professionals, strong employee profiles |
| 70-89 | Active company page with 5K+ followers, some employee thought leadership, occasional third-party mentions |
| 50-69 | Company page exists with 1K+ followers, irregular posting, limited third-party mentions |
| 30-49 | Company page exists but is sparse or inactive, few followers, no third-party mentions |
| 10-29 | Basic company page with minimal information |
| 0-9 | No LinkedIn company page |


### 5. Other Platform Presence -- Supplementary

These platforms have lower but still meaningful correlation with AI visibility:

#### Quora
- **Relevance:** Quora answers are frequently included in AI training data and cited by Perplexity.
- **What to check:** Is the brand mentioned in Quora answers to industry-relevant questions? Does the brand have an official Quora presence?
- **Signal strength:** Moderate for B2C, lower for B2B.

#### Stack Overflow / Stack Exchange
- **Relevance:** Critical for developer-facing brands (SaaS, dev tools, APIs).
- **What to check:** Is the brand's product discussed in Stack Overflow questions/answers? Does the brand have a tag? Do they have an official account answering questions?
- **Signal strength:** High for technical products, irrelevant for most B2C.

#### GitHub
- **Relevance:** Critical for open-source and developer-focused brands.
- **What to check:** Does the brand have a GitHub organization? Stars on repositories? Mentions in other repos' documentation or discussions?
- **Signal strength:** High for dev tools and open-source, low for non-technical brands.

#### Industry Forums and Communities
- **Relevance:** Niche authority signals that AI models pick up from domain-specific training data.
- **What to check:** Is the brand discussed in industry-specific forums (e.g., Hacker News for tech, ProductHunt for startups, industry-specific Slack communities)?
- **Signal strength:** Moderate, but valuable for establishing niche authority.

#### News and Press
- **Relevance:** News mentions build entity authority and recency signals.
- **What to check:** Has the brand been covered by major news outlets or industry publications? How recently? What was the context?
- **Signal strength:** Moderate. Recency matters -- a mention in the last 6 months is far more valuable than one from 3 years ago.

#### Podcasts
- **Relevance:** Growing AI training data source. Transcripts are increasingly indexed.
- **What to check:** Has the brand or its leadership appeared on podcasts? Are podcast transcripts mentioning the brand indexed by search engines?
- **Signal strength:** Moderate and growing.


## Composite Brand Authority Score

### Scoring Formula

| Platform | Weight | Rationale |
|---|---|---|
| YouTube Presence | 25% | Strongest correlation with AI citation (0.737) |
| Reddit Presence | 25% | Second strongest correlation; critical for product recommendations |
| Wikipedia / Wikidata | 20% | Entity recognition foundation; AI training data cornerstone |
| LinkedIn Authority | 15% | Professional authority signals; B2B relevance |
| Other Platforms | 15% | Supplementary signals from Quora, GitHub, news, forums, podcasts |

**Formula:**
```
Brand_Authority_Score = (YouTube * 0.25) + (Reddit * 0.25) + (Wikipedia * 0.20) + (LinkedIn * 0.15) + (Other * 0.15)
```

### Score Interpretation

| Score Range | Rating | Interpretation |
|---|---|---|
| 85-100 | Dominant | Brand is a well-recognized entity across AI platforms. Highly likely to be cited and recommended by AI systems. |
| 70-84 | Strong | Brand has solid cross-platform presence. AI systems likely recognize and cite it for relevant queries. |
| 50-69 | Moderate | Brand has presence on some platforms but gaps exist. AI citation is inconsistent. |
| 30-49 | Weak | Brand has limited platform presence. AI systems may not recognize it as a distinct entity. |
| 0-29 | Minimal | Brand has negligible platform presence. AI systems are unlikely to cite or recommend it. |


## Analysis Procedure

### Step 1: Identify Brand Information

Gather the following from the user or from the website:
- **Brand name** (exact spelling, including any official variants)
- **Founder/CEO name(s)**
- **Domain URL**
- **Industry/category**
- **Key products or services** (top 3)
- **Key competitors** (for comparison context)

### Step 2: Platform Scanning

For each platform, use WebFetch to search and assess presence:

**YouTube Check:**
1. Search: `[brand name] site:youtube.com`
2. Check: `youtube.com/@[brand-name]` or `youtube.com/c/[brand-name]` for official channel
3. Search: `"[brand name]" site:youtube.com` (exact match for mentions in descriptions)
4. Note: Channel subscriber count, video count, latest upload date, third-party mention count

**Reddit Check:**
1. Search: `[brand name] site:reddit.com`
2. Search: `"[brand name]" site:reddit.com` (exact match)
3. Check: `reddit.com/r/[brand-name]` for official subreddit
4. Check: `reddit.com/user/[brand-name]` for official account
5. Note: Thread count, dominant subreddits, sentiment (positive/negative/neutral), recommendation frequency

**Wikipedia Check (IMPORTANT — use BOTH methods to avoid false negatives):**

**Method 1 — Python API check (MOST RELIABLE, do this FIRST):**
```bash
python3 -c "
import requests, json
from urllib.parse import quote_plus
brand = '[Brand_Name]'
# Check Wikipedia API directly
api_url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={quote_plus(brand)}&format=json'
r = requests.get(api_url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
data = r.json()
results = data.get('query', {}).get('search', [])
if results and brand.lower() in results[0].get('title', '').lower():
    print(f'WIKIPEDIA PAGE EXISTS: {results[0][\"title\"]}')
    print(f'URL: https://en.wikipedia.org/wiki/{results[0][\"title\"].replace(\" \", \"_\")}')
else:
    print('No direct Wikipedia page found')
# Check Wikidata
wd_url = f'https://www.wikidata.org/w/api.php?action=wbsearchentities&search={quote_plus(brand)}&language=en&format=json'
r2 = requests.get(wd_url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
wd = r2.json()
entities = wd.get('search', [])
if entities:
    print(f'WIKIDATA ENTRY: {entities[0].get(\"id\", \"\")} — {entities[0].get(\"description\", \"\")}')
"
```

**Method 2 — Direct URL check (backup verification):**
1. WebFetch: `https://en.wikipedia.org/wiki/[Brand_Name]` — check if the page loads (not a redirect to search)
2. WebFetch: `https://en.wikipedia.org/wiki/[Founder_Name]` for founder article

**Method 3 — Search (least reliable, use only for supplemental info):**
1. Search: `[brand name] site:wikipedia.org`
2. Search: `[brand name] site:wikidata.org`

**CRITICAL:** Web search alone is NOT reliable for determining Wikipedia presence. ALWAYS run the Python API check first. If the API says a page exists, it exists — do not override this with a search result that fails to find it.

5. Note: Article existence, quality, edit history, Wikidata completeness

**LinkedIn Check:**
1. Search: `[brand name] site:linkedin.com`
2. Check: `linkedin.com/company/[brand-name]` for company page
3. Note: Follower count, post frequency, employee count listed, engagement levels

**Other Platforms:**
1. Search: `[brand name] site:quora.com`
2. Search: `[brand name] site:stackoverflow.com` (if technical brand)
3. Search: `[brand name] site:github.com` (if technical brand)
4. Search: `[brand name] site:news.ycombinator.com` (Hacker News)
5. Search: `"[brand name]"` broadly for news mentions (filter to last 6 months)
6. Note: Presence/absence and quality of mentions on each platform

### Step 3: Sentiment Assessment

For Reddit and other discussion platforms, assess sentiment by analyzing the most recent and most prominent mentions:

| Sentiment | Indicators |
|---|---|
| **Positive** | Recommendations ("I love [brand]," "We switched to [brand] and...", "Highly recommend"), upvoted mentions, positive comparison against competitors |
| **Neutral** | Factual mentions ("We use [brand] for...", "[Brand] offers..."), questions about the brand, balanced comparisons |
| **Negative** | Complaints ("Avoid [brand]", "[Brand] has terrible support"), downvoted recommendations, negative comparisons |
| **Mixed** | Combination of positive and negative. Note the ratio and primary themes. |

### Step 4: Competitive Comparison (Optional)

If competitors are identified, do a quick scan of their platform presence for context. This helps calibrate the score -- a brand with "moderate" Reddit presence in an industry where competitors have zero Reddit presence is relatively strong.

### Step 5: Score Calculation

1. Score each platform (0-100) using the rubrics above.
2. Apply weights to calculate the composite Brand Authority Score.
3. Identify the strongest and weakest platforms.
4. Generate specific, actionable recommendations for the weakest platforms.


## Output Format

Generate a file called `GEO-BRAND-MENTIONS.md`:

```markdown
# Brand Authority Report: [Brand Name]

**Analysis Date:** [Date]
**Brand:** [Brand Name]
**Domain:** [URL]
**Industry:** [Industry]


## Brand Authority Score: [X]/100 ([Rating])

### Platform Breakdown

| Platform | Score | Weight | Weighted | Status |
|---|---|---|---|---|
| YouTube | [X]/100 | 25% | [X] | [Active Channel / Mentioned / Absent] |
| Reddit | [X]/100 | 25% | [X] | [Active / Discussed / Absent] |
| Wikipedia | [X]/100 | 20% | [X] | [Article / Mentioned / Absent] |
| LinkedIn | [X]/100 | 15% | [X] | [Active / Basic / Absent] |
| Other Platforms | [X]/100 | 15% | [X] | [Summary] |
| **Total** | | | **[X]/100** | |


## Platform Detail

### YouTube ([X]/100)

**Official Channel:** [Yes/No] | [URL if exists]
**Subscribers:** [Count or N/A]
**Videos:** [Count or N/A]
**Last Upload:** [Date or N/A]
**Third-Party Mentions:** [Estimated count]
**Key Findings:**
- [Finding 1]
- [Finding 2]

### Reddit ([X]/100)

**Official Account:** [Yes/No] | [URL if exists]
**Own Subreddit:** [Yes/No] | [URL and member count if exists]
**Mention Volume:** [Estimated thread count]
**Primary Subreddits:** [List of subreddits where brand is discussed]
**Sentiment:** [Positive/Negative/Neutral/Mixed]
**Key Findings:**
- [Finding 1]
- [Finding 2]

### Wikipedia ([X]/100)

**Company Article:** [Yes/No] | [URL if exists]
**Founder Article:** [Yes/No] | [URL if exists]
**Wikidata Entry:** [Yes/No] | [Q-number if exists]
**Cited in Other Articles:** [Yes/No] | [Which articles]
**Key Findings:**
- [Finding 1]
- [Finding 2]

### LinkedIn ([X]/100)

**Company Page:** [Yes/No] | [URL if exists]
**Followers:** [Count or N/A]
**Post Frequency:** [Weekly/Monthly/Rare/Never]
**Key Findings:**
- [Finding 1]
- [Finding 2]

### Other Platforms ([X]/100)

| Platform | Presence | Notes |
|---|---|---|
| Quora | [Yes/No] | [Brief note] |
| Stack Overflow | [Yes/No] | [Brief note] |
| GitHub | [Yes/No] | [Brief note] |
| Hacker News | [Yes/No] | [Brief note] |
| News/Press | [Yes/No] | [Brief note] |
| Podcasts | [Yes/No] | [Brief note] |


## Recommendations

### Immediate Actions (Week 1-2)

1. **[Platform]:** [Specific action to take with expected impact]
2. **[Platform]:** [Specific action]

### Short-Term Strategy (Month 1-3)

1. **[Platform]:** [Strategy with tactics]
2. **[Platform]:** [Strategy with tactics]

### Long-Term Authority Building (Month 3-12)

1. **[Platform]:** [Long-term strategy]
2. **[Platform]:** [Long-term strategy]


## Competitive Context

[If competitors were analyzed, show a brief comparison table]

| Brand | YouTube | Reddit | Wikipedia | LinkedIn | Other | Total |
|---|---|---|---|---|---|---|
| [Subject Brand] | [X] | [X] | [X] | [X] | [X] | **[X]** |
| [Competitor 1] | [X] | [X] | [X] | [X] | [X] | **[X]** |
| [Competitor 2] | [X] | [X] | [X] | [X] | [X] | **[X]** |

## Key Takeaway

[1-2 sentence summary of the brand's AI visibility standing and the single most impactful action to take]
```


## Reference Data

### Correlation Strengths (Ahrefs Dec 2025, 75K Brands)

| Signal | Correlation with AI Citation | Traditional SEO Value |
|---|---|---|
| YouTube mentions | ~0.737 | Low (not a ranking factor) |
| Reddit mentions | High (exact coefficient not published) | Low |
| Wikipedia presence | High | Moderate (trust signal) |
| LinkedIn presence | Moderate | Low |
| Domain Rating | ~0.266 | Very High |
| Backlink count | ~0.266 | Very High |
| Organic traffic | Moderate | Very High |

**Key insight:** The signals that matter most for AI visibility (YouTube, Reddit) are almost irrelevant in traditional SEO, and the signals that matter most for traditional SEO (backlinks, DR) are weak predictors of AI visibility. This requires a fundamentally different optimization strategy.

### Platform-Specific Tips for Building Presence

**YouTube Quick Wins:**
- Create a channel and upload 3-5 explainer videos about your core topics.
- Ensure your brand name appears in video titles, descriptions, and spoken content.
- Pursue guest appearances on relevant industry YouTube channels.
- Create comparison or "alternatives" videos (these get cited by AI for comparison queries).

**Reddit Quick Wins:**
- Identify 3-5 subreddits where your target audience is active.
- Participate authentically (do not shill -- Reddit communities detect and punish this).
- Do an AMA if appropriate for your brand.
- Monitor and respond to mentions of your brand.
- Create genuinely helpful posts that naturally mention your brand's expertise.

**Wikipedia Strategy:**
- Hire a Wikipedia-knowledgeable consultant -- do NOT edit your own article (conflict of interest).
- Build notability through press coverage, academic citations, and industry recognition first.
- Ensure your Wikidata entry is complete even if you do not have a Wikipedia article.
- Contribute to industry-relevant articles where your brand can be naturally cited as a source.

**LinkedIn Quick Wins:**
- Optimize your company page with complete information and regular posting.
- Encourage leadership to post thought leadership content weekly.
- Publish LinkedIn articles on topics where your brand has unique expertise.
- Engage with industry discussions to increase brand visibility in professional contexts.


---


# GEO Content Quality & E-E-A-T Assessment

## Purpose

AI search platforms do not just find content — they evaluate whether content deserves to be cited. The primary framework for this evaluation is **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness), which per Google's December 2025 Quality Rater Guidelines update now applies to **ALL competitive queries**, not just YMYL (Your Money Your Life) topics. Content that scores high on E-E-A-T is dramatically more likely to be cited by AI platforms.

This skill evaluates content through two lenses:
1. **E-E-A-T signals** — does the content demonstrate real expertise and trust?
2. **AI citability** — is the content structured so AI platforms can extract and cite specific claims?

## How to Use This Skill

1. Fetch the target page(s) — homepage, key blog posts, service/product pages
2. Evaluate E-E-A-T across the 4 dimensions (25% each)
3. Assess content quality metrics (structure, readability, depth)
4. Check for AI content quality signals
5. Evaluate topical authority across the site
6. Score and generate GEO-CONTENT-ANALYSIS.md


## E-E-A-T Framework (100 points total)

### Experience — 25 points
First-hand knowledge and direct involvement with the topic. AI platforms increasingly distinguish between content that reports on a topic and content from someone who has DONE it.

**Signals to evaluate:**

| Signal | Points | How to Score |
|---|---|---|
| First-person accounts ("I tested...", "We implemented...") | 5 | 5 if present and specific, 3 if generic, 0 if absent |
| Original research or data not available elsewhere | 5 | 5 if original data, 3 if references original work, 0 if none |
| Case studies with specific results | 4 | 4 if detailed with numbers, 2 if general, 0 if none |
| Screenshots, photos, or evidence of direct use | 3 | 3 if authentic evidence, 1 if stock/generic, 0 if none |
| Specific examples from personal experience | 4 | 4 if specific and unique, 2 if somewhat specific, 0 if generic |
| Demonstrations of process (not just outcome) | 4 | 4 if step-by-step from experience, 2 if partial, 0 if none |

**What to flag as weak Experience:**
- Content that only summarizes what other sources say without adding new perspective
- Generic advice that could apply to any situation ("It depends on your needs")
- No mention of actual usage, testing, or direct involvement
- Hedging language that suggests lack of direct knowledge ("reportedly", "supposedly", "some say")

### Expertise — 25 points
Demonstrated knowledge depth and professional competence in the subject matter.

**Signals to evaluate:**

| Signal | Points | How to Score |
|---|---|---|
| Author credentials visible (bio, degrees, certifications) | 5 | 5 if full credentials, 3 if basic bio, 0 if no author |
| Technical depth appropriate to topic | 5 | 5 if thorough technical treatment, 3 if adequate, 0 if superficial |
| Methodology explanation (how conclusions were reached) | 4 | 4 if clear methodology, 2 if some explanation, 0 if none |
| Data-backed claims (statistics, research citations) | 4 | 4 if well-sourced, 2 if some data, 0 if unsupported claims |
| Industry-specific terminology used correctly | 3 | 3 if accurate specialized language, 1 if basic, 0 if errors |
| Author page with detailed professional background | 4 | 4 if dedicated author page, 2 if brief bio, 0 if none |

**What to flag as weak Expertise:**
- Claims without supporting evidence or sources
- Surface-level coverage of complex topics
- Misuse of technical terminology
- No visible author or author without relevant credentials
- Content that is broad and generic rather than deep and specific

### Authoritativeness — 25 points
Recognition by others as a credible source on the topic.

**Signals to evaluate:**

| Signal | Points | How to Score |
|---|---|---|
| Inbound citations from authoritative sources | 5 | 5 if cited by major sources, 3 if some citations, 0 if none |
| Author quoted or cited in press/media | 4 | 4 if media mentions, 2 if industry mentions, 0 if none |
| Industry awards or recognition mentioned | 3 | 3 if relevant awards, 1 if tangential, 0 if none |
| Speaker credentials (conferences, events) | 3 | 3 if listed, 0 if none |
| Published in peer-reviewed or respected outlets | 4 | 4 if tier-1 publications, 2 if industry outlets, 0 if none |
| Comprehensive topic coverage (topical authority) | 3 | 3 if site covers topic thoroughly, 1 if some coverage, 0 if isolated |
| Brand mentioned on Wikipedia or authoritative references | 3 | 3 if Wikipedia, 2 if other encyclopedic refs, 0 if none |

**What to flag as weak Authoritativeness:**
- Single-topic site with no depth of coverage
- No external validation of expertise claims
- No backlinks from authoritative sources
- Claims of authority without evidence (self-proclaimed "expert")

### Trustworthiness — 25 points
Signals that the content and its publisher are reliable and transparent.

**Signals to evaluate:**

| Signal | Points | How to Score |
|---|---|---|
| Contact information visible (address, phone, email) | 4 | 4 if full contact info, 2 if email only, 0 if none |
| Privacy policy present and linked | 2 | 2 if present, 0 if absent |
| Terms of service present | 1 | 1 if present, 0 if absent |
| HTTPS with valid certificate | 2 | 2 if valid HTTPS, 0 if not |
| Editorial standards or corrections policy | 3 | 3 if documented, 1 if implicit, 0 if none |
| Transparent about business model and conflicts | 3 | 3 if clear disclosures, 1 if some, 0 if none |
| Reviews and testimonials from real customers | 3 | 3 if verified reviews, 1 if testimonials, 0 if none |
| Accurate claims (no misinformation detected) | 4 | 4 if all claims accurate, 2 if mostly accurate, 0 if errors found |
| Clear affiliate/sponsorship disclosures | 3 | 3 if properly disclosed, 0 if undisclosed or absent |

**What to flag as weak Trustworthiness:**
- No contact information or physical address
- Missing privacy policy or terms
- Undisclosed affiliate links or sponsored content
- Claims that are verifiably false or misleading
- No way to contact the publisher for corrections


## Content Quality Metrics

### Word Count Benchmarks
These are **floors, not targets**. More words does not mean better content. The benchmark is the minimum length to adequately cover a topic for AI citability.

| Page Type | Minimum Words | Ideal Range | Notes |
|---|---|---|---|
| Homepage | 500 | 500-1,500 | Clear value proposition, not a wall of text |
| Blog post | 1,500 | 1,500-3,000 | Thorough but focused |
| Pillar content / Ultimate guide | 2,000 | 2,500-5,000 | Comprehensive topic coverage |
| Product page | 300 | 500-1,500 | Descriptions, specs, use cases |
| Service page | 500 | 800-2,000 | What, how, why, for whom |
| About page | 300 | 500-1,000 | Company/person story and credentials |
| FAQ page | 500 | 1,000-2,500 | Thorough answers, not one-liners |

### Readability Assessment
- **Target Flesch Reading Ease**: 60-70 (8th-9th grade level)
- This is NOT a direct ranking factor but affects citability — AI platforms prefer content that is clear and unambiguous
- Overly academic writing (score < 30) reduces citability for general queries
- Overly simple writing (score > 80) may lack the depth needed for expertise signals

**How to estimate without a tool:**
- Average sentence length: 15-20 words is ideal
- Average paragraph length: 2-4 sentences
- Presence of jargon: should be defined when first used
- Passive voice: < 15% of sentences

### Paragraph Structure for AI Parsing
AI platforms extract content at the paragraph level. Each paragraph should be a self-contained unit of meaning.

**Optimal paragraph structure:**
- **2-4 sentences** per paragraph (1-sentence paragraphs are weak; 5+ sentences are hard to extract)
- **One idea per paragraph** — do not mix topics within a paragraph
- **Lead with the key claim** — first sentence should contain the main point
- **Support with evidence** — remaining sentences provide data, examples, or context
- **Quotable standalone** — each paragraph should make sense if extracted in isolation

### Heading Structure
- **One H1 per page** — the primary topic/title
- **H2 for major sections** — should represent distinct subtopics
- **H3 for subsections** — nested under relevant H2
- **No skipped levels** — do not go from H1 to H3 without an H2
- **Descriptive headings** — "How to Optimize for AI Search" not "Section 2"
- **Question-based headings** where appropriate — these map directly to AI queries

### Internal Linking
- Every content page should link to 3-5 related pages on the same site
- Links should use descriptive anchor text (not "click here")
- Create a topic cluster structure: pillar page linked to/from all related subtopic pages
- Orphan pages (no internal links pointing to them) are rarely cited by AI


## AI Content Assessment

### AI-Generated Content Policy
AI-generated content is **acceptable** per Google's guidance (March 2024 clarification) as long as it demonstrates genuine E-E-A-T signals and has human oversight. The concern is not HOW content is created but WHETHER it provides value.

### Signs of Low-Quality AI Content (flag these)

| Signal | Description |
|---|---|
| Generic phrasing | "In today's fast-paced world...", "It's important to note that...", "At the end of the day..." |
| No original insight | Content that only rephrases widely available information |
| Lack of first-hand experience | No personal anecdotes, case studies, or specific examples |
| Perfect but empty structure | Well-formatted headings with shallow content beneath them |
| No specific examples | Uses abstract explanations without concrete instances |
| Repetitive conclusions | Each section ends with a variation of the same point |
| Hedging overload | "Generally speaking", "In most cases", "It depends on various factors" without specifying which factors |
| Missing human voice | No opinions, preferences, or professional judgment expressed |
| Filler content | Paragraphs that could be deleted without losing information |
| No data or sources | Claims presented as facts without attribution or evidence |

### High-Quality Content Signals (regardless of production method)

| Signal | Description |
|---|---|
| Original data | Surveys, experiments, benchmarks, proprietary analysis |
| Specific examples | Named products, companies, dates, numbers |
| Contrarian or nuanced views | Disagreement with conventional wisdom, backed by reasoning |
| First-person experience | "When I tested this..." or "Our team found..." |
| Updated information | References to recent events, current data |
| Expert opinion | Clear professional judgment, not just facts |
| Practical recommendations | Specific, actionable advice, not vague guidance |
| Trade-offs acknowledged | "This approach works well for X but not for Y because..." |


## Content Freshness Assessment

### Publication Dates
- Check for visible `datePublished` and `dateModified` in both the content and structured data
- Content without dates is treated as less trustworthy by AI platforms
- Dates should be specific (January 15, 2026) not vague ("recently")

### Freshness Scoring

| Criterion | Score |
|---|---|
| Updated within 3 months | Excellent — current and relevant |
| Updated within 6 months | Good — still reasonably current |
| Updated within 12 months | Acceptable — may need refresh |
| Updated 12-24 months ago | Warning — review for accuracy |
| No date or 24+ months old | Critical — AI platforms may deprioritize |

### Evergreen Indicators
Some content remains relevant regardless of age. Flag content as evergreen if:
- It covers fundamental concepts that do not change (physics, basic math, legal definitions)
- It is clearly labeled as a reference/guide for lasting concepts
- It does not contain time-dependent claims ("the latest", "currently", "in 2024")


## Topical Authority Assessment

### What It Is
Topical authority measures whether a site comprehensively covers a topic rather than touching on it superficially. AI platforms prefer citing sites that are recognized authorities on their topics.

### How to Assess
1. **Content breadth**: Does the site have multiple pages covering different aspects of its core topic?
2. **Content depth**: Do individual pages go deep into subtopics?
3. **Topic clustering**: Are pages organized into logical groups with internal linking?
4. **Content gaps**: Are there obvious subtopics that the site should cover but does not?
5. **Competitor comparison**: Do competitors cover subtopics that this site misses?

### Scoring

| Level | Description | Score Impact |
|---|---|---|
| Authority | 20+ pages covering topic comprehensively, strong clustering | +10 bonus |
| Developing | 10-20 pages with some clustering | +5 bonus |
| Emerging | 5-10 pages on topic, limited clustering | +0 |
| Thin | < 5 pages, no clustering | -5 penalty |


## Overall Scoring (0-100)

### Score Composition
| Component | Weight | Max Points |
|---|---|---|
| Experience | 25% | 25 |
| Expertise | 25% | 25 |
| Authoritativeness | 25% | 25 |
| Trustworthiness | 25% | 25 |
| **Subtotal** | | **100** |
| Topical Authority Modifier | | +10 to -5 |
| **Final Score** | | **Capped at 100** |

### Score Interpretation
- **85-100**: Exceptional — strong AI citation candidate across platforms
- **70-84**: Good — solid foundation, specific improvements will increase citability
- **55-69**: Average — multiple E-E-A-T gaps reducing AI visibility
- **40-54**: Below Average — significant content quality and trust issues
- **0-39**: Poor — fundamental content strategy overhaul needed


## Output Format

Generate **GEO-CONTENT-ANALYSIS.md** with:

```markdown
# GEO Content Quality & E-E-A-T Analysis — [Domain]
Date: [Date]

## Content Score: XX/100

## E-E-A-T Breakdown
| Dimension | Score | Key Finding |
|---|---|---|
| Experience | XX/25 | [One-line summary] |
| Expertise | XX/25 | [One-line summary] |
| Authoritativeness | XX/25 | [One-line summary] |
| Trustworthiness | XX/25 | [One-line summary] |

## Topical Authority Modifier: [+10 to -5]

## Pages Analyzed
| Page | Word Count | Readability | Heading Structure | Citability Rating |
|---|---|---|---|---|
| [URL] | [Count] | [Score] | [Pass/Warn/Fail] | [High/Medium/Low] |

## E-E-A-T Detailed Findings

### Experience
[Specific passages and pages with strong/weak experience signals]

### Expertise
[Author credentials found, technical depth assessment, specific gaps]

### Authoritativeness
[External validation found, topical authority assessment, gaps]

### Trustworthiness
[Trust signals present/missing, accuracy concerns if any]

## Content Quality Issues
[Specific passages flagged with reasons and rewrite suggestions]

## AI Content Concerns
[Any low-quality AI content patterns detected, with specific examples]

## Freshness Assessment
| Page | Published | Last Updated | Status |
|---|---|---|---|
| [URL] | [Date] | [Date] | [Current/Stale/No Date] |

## Citability Assessment
### Most Citable Passages
[Top 5 passages that AI platforms are most likely to cite, with reasons]

### Least Citable Pages
[Pages with lowest citability, with specific improvement recommendations]

## Improvement Recommendations
### Quick Wins
[Specific content changes that can be made immediately]

### Content Gaps
[Topics the site should cover to strengthen topical authority]

### Author/E-E-A-T Improvements
[Specific steps to strengthen E-E-A-T signals]
```


---


# GEO Platform Optimizer

## Core Insight

Only **11% of domains** are cited by BOTH ChatGPT and Google AI Overviews for the same query. Each AI search platform uses different indexes, ranking logic, and source preferences. A page optimized for Google AI Overviews may be invisible to ChatGPT, and vice versa. Platform-specific optimization is not optional — it is the foundation of any serious GEO strategy.

## How to Use This Skill

1. Collect the target URL and the site's primary topic/industry
2. Run each platform checklist below against the site
3. Score each platform on the 0-100 rubric
4. Generate GEO-PLATFORM-OPTIMIZATION.md with per-platform scores, gaps, and action items


## Platform 1: Google AI Overviews (AIO)

### How AIO Selects Sources
- 92% of AIO citations come from pages already ranking in the **top 10 organic results** — traditional SEO is the gateway
- However, 47% of citations come from pages ranking **below position 5** — AIO has its own selection logic favoring clarity and directness over raw rank
- AIO strongly favors pages with **clean structure, direct answers, and scannable formatting**
- Featured snippet optimization has ~70% overlap with AIO optimization
- AIO prefers **concise, factual, unambiguous answers** — hedging and filler reduce citation probability

### Optimization Checklist

1. **Question-Based Headings**: Use H2/H3 headings phrased as questions matching real user queries. Check Google's "People Also Ask" for the target topic and mirror those exact phrasings.
2. **Direct Answer in First Paragraph**: After each question heading, provide a clear 1-2 sentence answer immediately. Then expand with supporting detail. The first sentence should be a standalone citation candidate.
3. **Tables and Structured Comparisons**: AIO heavily cites tables. Convert any comparison, pricing, specification, or feature data into HTML tables. Use clear column headers.
4. **Ordered and Unordered Lists**: Step-by-step processes should use ordered lists. Feature lists should use unordered lists. AIO extracts these directly.
5. **FAQ Sections**: Add a dedicated FAQ section with 5-10 real questions. Use proper H3 headings for each question. While FAQPage schema rich results are restricted to govt/health sites since Aug 2023, the content pattern still helps AIO extraction.
6. **Definitions and Glossary Boxes**: For any industry-specific term, provide a clear definition. Format: "**[Term]** is [concise definition]." AIO frequently cites definitions.
7. **Statistics with Sources**: Include specific numbers with attribution. "According to [Source], [statistic]." AIO prefers citeable, specific claims over vague assertions.
8. **Publication Date**: Include a visible publication date and last-updated date. AIO deprioritizes undated content for time-sensitive queries.
9. **Author Byline**: Display author name with credentials. Link to an author page with bio, credentials, and sameAs links.
10. **Page Depth**: Keep target pages within 3 clicks of homepage. AIO rarely cites deep, orphaned content.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Ranks in top 10 for target queries | 20 | 20 if yes, 10 if top 20, 0 if beyond |
| Question-based headings present | 10 | 2 points per question heading, max 10 |
| Direct answers after headings | 15 | 3 points per direct answer, max 15 |
| Tables present for comparison data | 10 | 10 if tables used appropriately, 5 if partial, 0 if absent |
| Lists for processes/features | 10 | 10 if present, 5 if partial |
| FAQ section with 5+ questions | 10 | 10 if 5+, 5 if 1-4, 0 if none |
| Statistics with citations | 10 | 2 points per cited stat, max 10 |
| Publication/updated date visible | 5 | 5 if both dates, 3 if one, 0 if none |
| Author byline with credentials | 5 | 5 if full byline, 3 if name only, 0 if none |
| Clean URL + heading hierarchy | 5 | 5 if H1>H2>H3 clean, 3 if minor issues, 0 if broken |


## Platform 2: ChatGPT Web Search

### How ChatGPT Selects Sources
- Uses **Bing's search index** as its foundation (not Google)
- Top citation sources by domain share: **Wikipedia (47.9%)**, Reddit (11.3%), YouTube, major news outlets
- ChatGPT heavily weights **entity recognition** — if your brand exists as a structured entity (Wikipedia, Wikidata, Crunchbase), it is far more likely to be cited
- Prefers **authoritative, well-established sources** over new or niche sites
- Longer, more comprehensive articles get cited more often than short pieces
- ChatGPT tends to cite **the most canonical source** for a claim rather than the original

### Optimization Checklist

1. **Wikipedia Presence**: Check if the brand/person/product has a Wikipedia article. If not, assess notability criteria. If notable, create a draft. If an article exists, ensure it is accurate and current.
2. **Wikidata Entity**: Verify the entity exists on Wikidata (wikidata.org). If not, create a Wikidata item with key properties: instance of, official website, social media links, founding date, headquarters location.
3. **Bing Webmaster Tools**: Verify the site is registered in Bing Webmaster Tools. Submit sitemap. Check for crawl errors.
4. **Bing Index Coverage**: Use `site:domain.com` on Bing to verify key pages are indexed. Bing may have different indexed pages than Google.
5. **Reddit Authority**: Check for brand mentions on Reddit. Identify relevant subreddits. Assess whether the brand participates authentically in discussions.
6. **YouTube Presence**: Verify YouTube channel exists with relevant content. Video descriptions should contain full URLs and entity information.
7. **Authoritative Backlinks**: ChatGPT/Bing weight .edu, .gov, and major publication backlinks heavily. Audit backlink profile for these sources.
8. **Entity Consistency**: Brand name, founding date, leadership, and key facts must be consistent across Wikipedia, Crunchbase, LinkedIn, and the official website.
9. **Comprehensive Content**: Pages targeting ChatGPT citation should be **2000+ words** with thorough topic coverage. ChatGPT prefers single authoritative sources over combining multiple thin pages.
10. **Clear Attribution**: Include "About" sections, company descriptions, and founding stories. ChatGPT uses these for entity grounding.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Wikipedia article exists and is accurate | 20 | 20 if exists, 10 if stub, 0 if none |
| Wikidata entity with 5+ properties | 10 | 10 if complete, 5 if basic, 0 if none |
| Bing index coverage of key pages | 10 | 10 if full, 5 if partial, 0 if poor |
| Reddit brand mentions (positive) | 10 | 10 if active discussions, 5 if mentions, 0 if none |
| YouTube channel with relevant content | 10 | 10 if active, 5 if present but sparse, 0 if none |
| Authoritative backlinks (.edu, .gov, press) | 15 | 3 points per authoritative backlink category, max 15 |
| Entity consistency across platforms | 10 | 10 if consistent, 5 if minor discrepancies, 0 if major |
| Content comprehensiveness (2000+ words) | 10 | 10 if thorough, 5 if adequate, 0 if thin |
| Bing Webmaster Tools configured | 5 | 5 if verified, 0 if not |


## Platform 3: Perplexity AI

### How Perplexity Selects Sources
- Top citation sources: **Reddit (46.7%)**, Wikipedia, YouTube, major publications
- Perplexity places the **heaviest emphasis on community validation** of all AI search platforms
- Strongly favors **discussion threads** where claims are debated, validated, or expanded by multiple participants
- Prefers recent content — publication date is a strong ranking signal
- Cites **multiple sources per answer** (typically 5-15), so there is more opportunity for mid-authority sites to appear
- Uses its own crawling infrastructure in addition to search APIs

### Optimization Checklist

1. **Active Reddit Presence**: The brand or its representatives should participate authentically in relevant subreddit discussions. Not promotional — helpful, specific, and community-oriented.
2. **Reddit AMAs and Threads**: Encourage or participate in AMAs, detailed discussion threads, and community Q&As. Perplexity treats these as high-signal content.
3. **Forum and Community Presence**: Beyond Reddit, check Hacker News, Stack Overflow, Quora, and niche industry forums. Perplexity indexes these heavily.
4. **Discussion-Friendly Content**: Publish content that invites discussion — opinion pieces, research findings, contrarian takes, original data. Content that gets shared and debated in communities ranks higher.
5. **Freshness Signals**: Publish content with clear dates. Update content regularly. Perplexity deprioritizes stale content more aggressively than other platforms.
6. **Multiple Source Validation**: Claims in your content should be supported by other sources. Perplexity cross-references and prefers claims it can verify from multiple origins.
7. **YouTube Video Content**: Create video content that Perplexity can reference. Ensure video titles, descriptions, and transcripts contain target information.
8. **Direct, Quotable Passages**: Write paragraphs that can stand alone as citations. Each paragraph should make one clear point with supporting evidence.
9. **Original Data and Research**: Publish original surveys, benchmarks, case studies, or datasets. Perplexity heavily favors primary sources.
10. **Perplexity Pages**: Check if Perplexity has created a "Page" about your topic/brand. These are curated summaries that influence future citations.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Active Reddit presence in relevant subreddits | 20 | 20 if active contributor, 10 if mentioned, 0 if absent |
| Forum/community mentions (HN, SO, Quora) | 10 | 10 if multiple platforms, 5 if one, 0 if none |
| Content freshness (updated within 6 months) | 10 | 10 if recent, 5 if within year, 0 if older |
| Original research/data published | 15 | 15 if original research, 10 if case studies, 5 if some data, 0 if none |
| YouTube content with transcripts | 10 | 10 if active channel, 5 if some videos, 0 if none |
| Quotable, standalone paragraphs | 10 | 2 points per well-structured quotable paragraph, max 10 |
| Multi-source claim validation | 10 | 10 if claims well-sourced, 5 if some sourcing, 0 if none |
| Discussion-generating content | 10 | 10 if content gets shared/discussed, 5 if some engagement, 0 if none |
| Wikipedia/Wikidata presence | 5 | 5 if present, 0 if absent |


## Platform 4: Google Gemini

### How Gemini Selects Sources
- Uses **Google's search index** plus strong weighting toward **Google-owned properties**
- YouTube content is weighted significantly more heavily than in standard Google Search
- Google Business Profile data is directly accessible to Gemini
- Gemini uses Google's Knowledge Graph directly — entity presence in Knowledge Graph is a major advantage
- Structured data (Schema.org) is consumed directly by Gemini for entity understanding
- Gemini multi-modal: can reference images, videos, and text together

### Optimization Checklist

1. **Google Knowledge Panel**: Check if the brand has a Google Knowledge Panel. If not, claim it through Google Business Profile or structured data. Ensure all information is accurate.
2. **Google Business Profile**: Complete and optimize GBP with all fields: hours, services, photos, posts, Q&A. Gemini pulls directly from GBP for local queries.
3. **YouTube Strategy**: Create YouTube content for every key topic. Optimize titles, descriptions, timestamps, and closed captions. Gemini cites YouTube more than any other AI platform.
4. **YouTube Chapters and Timestamps**: Use chapters (timestamps in description) so Gemini can reference specific segments of videos.
5. **Google Merchant Center**: For e-commerce, ensure products are in Google Merchant Center. Gemini references product data directly.
6. **Structured Data (Schema.org)**: Implement comprehensive Schema.org markup. Gemini uses this for entity understanding more aggressively than other platforms.
7. **Google Sites Ecosystem**: Ensure presence across Google ecosystem: Google Scholar (for research), Google News (for publishers), Google Maps (for local).
8. **Image Optimization**: Gemini is multi-modal. Use descriptive alt text, structured image filenames, and high-quality images. Include relevant images with every piece of content.
9. **Google E-E-A-T Signals**: All standard Google E-E-A-T signals apply with extra weight. Author pages, about pages, editorial policies, and expertise demonstrations.
10. **Chrome Web Store / Google Workspace Marketplace**: For software companies, presence on Google platforms adds entity signals.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Google Knowledge Panel exists | 15 | 15 if complete, 10 if partial, 0 if none |
| Google Business Profile complete | 10 | 10 if fully optimized, 5 if basic, 0 if none |
| YouTube channel with topic-relevant content | 20 | 20 if active with chapters, 10 if present, 0 if none |
| Schema.org structured data implemented | 15 | 15 if comprehensive, 10 if basic, 5 if minimal, 0 if none |
| Google ecosystem presence (Scholar, News, Maps) | 10 | 10 if 3+, 5 if 1-2, 0 if none |
| Image optimization (alt text, filenames) | 10 | 10 if all images optimized, 5 if partial, 0 if none |
| E-E-A-T signals (author pages, about, editorial) | 10 | 10 if strong, 5 if partial, 0 if weak |
| Google Merchant Center (if e-commerce) | 5 | 5 if applicable and active, N/A otherwise |
| Multi-modal content (text + images + video) | 5 | 5 if rich multi-modal, 3 if some, 0 if text-only |


## Platform 5: Bing Copilot

### How Copilot Selects Sources
- Uses **Bing's search index** (shared infrastructure with ChatGPT but different ranking/selection)
- Supports **IndexNow protocol** for near-instant indexing of new and updated content
- Copilot tends to cite **fewer sources per answer** (typically 3-5) but gives more prominent attribution
- Microsoft ecosystem integration: LinkedIn, GitHub, Microsoft Learn content is weighted
- Copilot prefers pages with clear, structured markup and fast load times

### Optimization Checklist

1. **Bing Webmaster Tools**: Register and verify site. Submit XML sitemap. Review and fix any crawl issues.
2. **IndexNow Implementation**: Implement the IndexNow protocol to notify Bing of content changes in real-time. Submit a key file at `/.well-known/indexnow-key.txt` and ping the IndexNow API on content publish/update.
3. **LinkedIn Company Page**: Ensure the company LinkedIn page is complete with accurate description, employee connections, and regular posts. Copilot indexes LinkedIn content.
4. **GitHub Presence**: For tech companies, maintain an active GitHub presence. Copilot references GitHub repos, documentation, and README files.
5. **Microsoft Learn / Documentation**: If relevant, contribute to Microsoft Learn or ensure documentation is compatible with Microsoft's documentation standards.
6. **Bing Places for Business**: Equivalent to Google Business Profile. Complete all fields for local search visibility in Copilot.
7. **Clear Meta Descriptions**: Bing/Copilot weights meta descriptions more heavily than Google does. Write compelling, keyword-rich meta descriptions for every page.
8. **Social Signals**: Bing has historically weighted social signals (shares, likes, engagement) more than Google. Maintain active social media presence.
9. **Exact-Match Keywords**: Bing's algorithm is more literal about keyword matching than Google. Include exact target phrases in titles, headings, and body content.
10. **Fast Page Load**: Copilot deprioritizes slow pages. Target sub-2-second load time. Optimize images, enable compression, minimize render-blocking resources.

### Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Bing Webmaster Tools verified + sitemap | 15 | 15 if verified, 5 if partial, 0 if not |
| IndexNow protocol implemented | 15 | 15 if active, 0 if not |
| Bing index coverage of key pages | 10 | 10 if full, 5 if partial, 0 if poor |
| LinkedIn company page (complete) | 10 | 10 if complete, 5 if basic, 0 if none |
| GitHub presence (if applicable) | 5 | 5 if active, N/A if not applicable |
| Meta descriptions optimized | 10 | 10 if all key pages, 5 if partial, 0 if missing |
| Social media engagement signals | 10 | 10 if active engagement, 5 if present, 0 if none |
| Exact-match keywords in titles/headings | 10 | 10 if well-optimized, 5 if partial, 0 if not |
| Page load speed < 2 seconds | 10 | 10 if < 2s, 5 if < 4s, 0 if > 4s |
| Bing Places configured (if local) | 5 | 5 if complete, N/A if not local |


## Cross-Platform Summary

### Universal Optimization Actions (help ALL platforms)
1. Wikipedia/Wikidata entity presence
2. YouTube channel with relevant content
3. Comprehensive, well-structured content with clear headings
4. Schema.org structured data (especially Organization + sameAs)
5. Fast page load and clean HTML
6. Author pages with credentials and sameAs links
7. Regular content updates with visible dates

### Platform-Specific Priorities
| Priority | Google AIO | ChatGPT | Perplexity | Gemini | Copilot |
|---|---|---|---|---|---|
| #1 | Top-10 ranking | Wikipedia | Reddit presence | YouTube | IndexNow |
| #2 | Q&A structure | Entity graph | Original research | Knowledge Panel | Bing WMT |
| #3 | Tables/lists | Bing SEO | Freshness | Schema.org | LinkedIn |
| #4 | Featured snippets | Reddit | Community forums | GBP | Meta descriptions |


## Output Format

Generate **GEO-PLATFORM-OPTIMIZATION.md** with the following structure:

```markdown
# GEO Platform Optimization Report — [Domain]
Date: [Date]

## Overall Platform Readiness
- Combined GEO Score: XX/100 (average of all platform scores)

## Platform Scores
| Platform | Score | Status |
|---|---|---|
| Google AI Overviews | XX/100 | [Strong/Moderate/Weak] |
| ChatGPT Web Search | XX/100 | [Strong/Moderate/Weak] |
| Perplexity AI | XX/100 | [Strong/Moderate/Weak] |
| Google Gemini | XX/100 | [Strong/Moderate/Weak] |
| Bing Copilot | XX/100 | [Strong/Moderate/Weak] |

Status thresholds: Strong = 70+, Moderate = 40-69, Weak = 0-39

## Platform Details
[Per-platform breakdown with score, gaps found, specific actions]

## Prioritized Action Plan
### Quick Wins (this week)
[Actions that improve multiple platform scores with minimal effort]

### Medium-Term (this month)
[Actions requiring content creation or technical changes]

### Strategic (this quarter)
[Actions requiring entity building, community development, or platform presence]
```


---


# GEO Client Report Generator

## Purpose

This skill aggregates outputs from all GEO audit skills into a single, professional report that can be delivered directly to a client or stakeholder. The report is written for **business owners and marketing leaders**, not developers — technical findings are translated into business impact and clear action items with priority levels.

## How to Use This Skill

1. Run the following audits first (or use existing report data):
   - `geo-platform-optimizer` -> GEO-PLATFORM-OPTIMIZATION.md
   - `geo-schema` -> GEO-SCHEMA-REPORT.md
   - `geo-technical` -> GEO-TECHNICAL-AUDIT.md
   - `geo-content` -> GEO-CONTENT-ANALYSIS.md
   - (Optional) `geo-llms-txt` -> llms.txt assessment
   - (Optional) `geo-brand-mentions` -> brand authority data
2. Collect all scores and findings
3. Calculate the composite GEO Readiness Score
4. Generate the client report using the template below
5. Output: GEO-CLIENT-REPORT.md


## GEO Readiness Score Calculation

### Component Weights

| Component | Weight | Source Skill |
|---|---|---|
| AI Platform Readiness | 25% | geo-platform-optimizer |
| Content Quality & E-E-A-T | 25% | geo-content |
| Technical Foundation | 20% | geo-technical |
| Schema & Structured Data | 15% | geo-schema |
| Brand Authority & Entity Presence | 15% | geo-platform-optimizer (entity signals) |

### Score Formula
```
GEO Score = (Platform Score * 0.25) + (Content Score * 0.25) + (Technical Score * 0.20) + (Schema Score * 0.15) + (Brand Score * 0.15)
```

Round to the nearest integer. Cap at 100.

### Score Interpretation for Clients

| Score Range | Label | Client-Facing Description |
|---|---|---|
| 85-100 | Excellent | Your site is well-positioned for AI search. Focus on maintaining and expanding your advantage. |
| 70-84 | Good | Solid foundation with clear opportunities to improve AI visibility. Targeted optimizations will yield significant results. |
| 55-69 | Moderate | Your site has gaps in AI readiness that competitors may be exploiting. A structured optimization plan will close these gaps. |
| 40-54 | Below Average | Significant barriers to AI search visibility exist. Without action, your brand risks being invisible in AI-generated answers. |
| 0-39 | Needs Attention | Critical AI readiness issues require immediate action. Your competitors are likely capturing the AI search traffic your brand should own. |


## Report Template

The complete report follows this exact structure. Each section includes instructions on what to write and how.


### Section 1: Executive Summary

Write exactly ONE paragraph (4-6 sentences) covering:
- What was analyzed (domain, number of pages, date of analysis)
- The overall GEO Readiness Score with context ("XX/100, which places [brand] in the [label] tier")
- The single most impactful finding (positive or negative)
- Top 3 priority recommendations in one sentence
- One sentence on the business impact ("Addressing these recommendations could increase AI-driven traffic by an estimated XX%, representing approximately $X,XXX/month based on current traffic patterns")

**Tone**: Confident, direct, professional. No jargon. No hedging. Write as a consultant delivering findings, not as a tool generating a report.

### Section 2: GEO Readiness Score

Present the overall score prominently:

```
## GEO Readiness Score: XX/100 — [Label]
```

Then break down by component in a table:

```markdown
| Component | Score | Weight | Weighted Score |
|---|---|---|---|
| AI Platform Readiness | XX/100 | 25% | XX |
| Content Quality & E-E-A-T | XX/100 | 25% | XX |
| Technical Foundation | XX/100 | 20% | XX |
| Schema & Structured Data | XX/100 | 15% | XX |
| Brand Authority | XX/100 | 15% | XX |
| **Overall** | | | **XX/100** |
```

### Section 3: AI Visibility Dashboard

Present per-platform readiness scores:

```markdown
## AI Visibility Dashboard

| AI Platform | Readiness Score | Key Gap | Priority Action |
|---|---|---|---|
| Google AI Overviews | XX/100 | [One-line gap] | [One-line action] |
| ChatGPT Web Search | XX/100 | [One-line gap] | [One-line action] |
| Perplexity AI | XX/100 | [One-line gap] | [One-line action] |
| Google Gemini | XX/100 | [One-line gap] | [One-line action] |
| Bing Copilot | XX/100 | [One-line gap] | [One-line action] |
```

Add a brief paragraph explaining what these scores mean: "These scores reflect how likely your content is to be cited by each AI search platform. A score below 50 indicates significant barriers to citation on that platform."

### Section 4: AI Crawler Access Status

Present as a clear table:

```markdown
## AI Crawler Access

| AI Crawler | Platform | Status | Impact | Recommendation |
|---|---|---|---|---|
| Googlebot | Google Search + AIO | Allowed/Blocked | Critical | [Action] |
| GPTBot | ChatGPT / OpenAI | Allowed/Blocked | High | [Action] |
| Bingbot | Bing + Copilot + ChatGPT | Allowed/Blocked | High | [Action] |
| PerplexityBot | Perplexity AI | Allowed/Blocked | Medium | [Action] |
| Google-Extended | Gemini Training | Allowed/Blocked | Medium | [Action] |
| ClaudeBot | Anthropic Claude | Allowed/Blocked | Medium | [Action] |
| Applebot-Extended | Apple Intelligence | Allowed/Blocked | Medium | [Action] |
```

**Translate for the client**: "Blocking AI crawlers is like closing your store during business hours. If a crawler cannot access your site, the AI platform it powers cannot cite your content. We recommend allowing all major AI crawlers unless you have a specific data licensing concern."

### Section 5: Brand Authority Analysis

Present entity presence across platforms:

```markdown
## Brand Authority

| Platform | Presence | Status | Impact on AI Visibility |
|---|---|---|---|
| Wikipedia | Yes/No | [Detail] | Very High — 47.9% of ChatGPT citations are Wikipedia |
| Wikidata | Yes/No | [Detail] | High — machine-readable entity data |
| LinkedIn | Yes/No | [Detail] | High — Bing Copilot and ChatGPT signal |
| YouTube | Yes/No | [Detail] | High — Gemini and Perplexity signal |
| Reddit | Yes/No | [Detail] | Very High — 46.7% of Perplexity citations are Reddit |
| Google Knowledge Panel | Yes/No | [Detail] | High — Gemini entity recognition |
| Crunchbase | Yes/No | [Detail] | Medium — entity validation |
| GitHub | Yes/No | [Detail] | Medium — tech brand signal |
```

**Translate for the client**: "AI platforms build trust by cross-referencing your brand across multiple authoritative sources. Each platform where your brand has an accurate, consistent presence increases the likelihood of being cited in AI answers."

### Section 6: Citability Analysis

#### Top 5 Most Citable Pages
For each page:
- URL
- Why it is citable (structure, depth, E-E-A-T signals)
- One specific improvement that would make it even more citable

#### Top 5 Least Citable Pages
For each page:
- URL
- Why it is unlikely to be cited (thin content, poor structure, missing signals)
- Specific rewrite or restructure recommendation

**Business impact framing**: "Your most citable pages are your best candidates for appearing in AI-generated answers. Improving the 5 least citable pages represents the highest-ROI content investment you can make for AI visibility."

### Section 7: Technical Health Summary

Present the key technical findings in business-friendly language:

```markdown
## Technical Health

| Area | Status | Business Impact |
|---|---|---|
| Core Web Vitals | Good/Needs Work/Poor | [Impact on user experience and rankings] |
| Server-Side Rendering | Yes/Partial/No | [Impact on AI crawler visibility] |
| Mobile Optimization | Good/Needs Work/Poor | [Impact on Google's mobile-first indexing] |
| Security (HTTPS + Headers) | Good/Needs Work/Poor | [Impact on trust signals] |
| Page Speed | Fast/Average/Slow | [Impact on user experience and crawl budget] |
| IndexNow Protocol | Implemented/Not | [Impact on Bing/ChatGPT indexing speed] |
```

**Critical finding callout**: If SSR is missing or partial, highlight this prominently: "Your site uses client-side rendering, which means AI crawlers see an empty page when they visit. This is the single most impactful technical issue for AI search visibility. Until this is resolved, most AI platforms cannot cite your content."

### Section 8: Schema & Structured Data

```markdown
## Schema & Structured Data

### Current Implementation
| Schema Type | Present | Status | AI Impact |
|---|---|---|---|
| Organization | Yes/No | [Valid/Issues] | Critical — entity recognition |
| Article + Author | Yes/No | [Valid/Issues] | High — E-E-A-T signal |
| sameAs (entity links) | Yes/No | [Count] links | Critical — cross-platform entity graph |
| [Business-specific] | Yes/No | [Valid/Issues] | [Impact] |
| WebSite + SearchAction | Yes/No | [Valid/Issues] | Medium — sitelinks |
| BreadcrumbList | Yes/No | [Valid/Issues] | Low-Medium — navigation context |
```

If schemas are missing, note: "Ready-to-use structured data code has been prepared and is included in the technical appendix. Your development team can add this to your site with minimal effort."

### Section 9: llms.txt Status

```markdown
## llms.txt — AI Content Guide

| File | Status | Recommendation |
|---|---|---|
| /llms.txt | Present/Missing | [Action] |
| /llms-full.txt | Present/Missing | [Action] |
```

**Translate for the client**: "llms.txt is an emerging standard (similar to robots.txt) that tells AI systems what your site is about and which pages are most important. While not universally adopted yet, implementing it positions your brand ahead of competitors and provides direct guidance to AI platforms."

### Section 10: Prioritized Action Plan

This is the most important section of the report. Organize actions by timeline and impact.

```markdown
## Prioritized Action Plan

### Quick Wins (This Week)
*High impact, low effort — can be implemented immediately*

| # | Action | Impact | Effort | Platforms Affected |
|---|---|---|---|---|
| 1 | [Specific action] | [High/Med] | [Hours estimate] | [Which AI platforms] |
| 2 | [Specific action] | [High/Med] | [Hours estimate] | [Which AI platforms] |
```

**Quick Win criteria**: Can be done in < 4 hours by one person. Examples:
- Unblock AI crawlers in robots.txt
- Add publication dates to existing content
- Add author bylines with credentials
- Fix broken meta descriptions
- Add sameAs properties to existing Organization schema
- Create/claim llms.txt file

```markdown
### Medium-Term Improvements (This Month)
*Significant impact, moderate effort — requires content or technical changes*

| # | Action | Impact | Effort | Platforms Affected |
|---|---|---|---|---|
| 1 | [Specific action] | [High/Med] | [Days estimate] | [Which AI platforms] |
```

**Medium-Term criteria**: 1-5 days of work. Examples:
- Restructure top 10 pages with question-based headings and direct answers
- Implement comprehensive Schema.org markup
- Create author pages with credentials and sameAs links
- Optimize Core Web Vitals (image compression, code splitting)
- Register and configure Bing Webmaster Tools
- Implement IndexNow protocol

```markdown
### Strategic Initiatives (This Quarter)
*Long-term competitive advantage, requires ongoing investment*

| # | Action | Impact | Effort | Platforms Affected |
|---|---|---|---|---|
| 1 | [Specific action] | [High/Med] | [Weeks estimate] | [Which AI platforms] |
```

**Strategic criteria**: Ongoing effort over weeks/months. Examples:
- Build Wikipedia/Wikidata entity presence
- Develop active Reddit community engagement strategy
- Create YouTube content strategy aligned with search queries
- Implement server-side rendering (if currently client-rendered)
- Build topical authority through comprehensive content strategy
- Establish original research/data publication program

### Estimated Impact
After the action plan, include an impact estimate:

"Based on industry benchmarks and the specific gaps identified in this audit:
- **Quick Wins alone** could improve your GEO score by approximately [X-Y] points
- **Full implementation** of this action plan could improve your GEO score to approximately [XX]/100
- At current traffic levels and conversion rates, improved AI visibility represents an estimated **$X,XXX - $XX,XXX per month** in additional organic value"

Use conservative estimates. Base the dollar figure on:
- Current estimated organic traffic value (from analytics if available, or estimate from industry benchmarks)
- AI search is projected to drive 25-40% of organic discovery by end of 2026
- A 10-point GEO score improvement typically correlates with a 15-25% increase in AI citation frequency

### Section 11: Competitor Comparison (if competitor URLs provided)

If competitor URLs were analyzed alongside the primary domain:

```markdown
## Competitor Comparison

| Metric | [Your Brand] | [Competitor 1] | [Competitor 2] |
|---|---|---|---|
| Overall GEO Score | XX/100 | XX/100 | XX/100 |
| Google AIO Readiness | XX/100 | XX/100 | XX/100 |
| ChatGPT Readiness | XX/100 | XX/100 | XX/100 |
| Perplexity Readiness | XX/100 | XX/100 | XX/100 |
| Schema Coverage | [Detail] | [Detail] | [Detail] |
| Wikipedia Presence | Yes/No | Yes/No | Yes/No |
| Reddit Authority | [Detail] | [Detail] | [Detail] |
| SSR Status | Yes/No | Yes/No | Yes/No |

### Where You Lead
[Specific areas where the brand outperforms competitors]

### Where You Trail
[Specific areas where competitors have an advantage, with actions to close the gap]
```

### Section 12: Appendix

```markdown
## Appendix

### Methodology
This GEO audit was conducted using the following methodology:
- **Pages analyzed**: [List of specific URLs audited]
- **Platforms assessed**: Google AI Overviews, ChatGPT, Perplexity AI, Google Gemini, Bing Copilot
- **Technical checks**: HTTP headers, robots.txt, HTML source analysis, structured data validation
- **Content assessment**: E-E-A-T framework (Experience, Expertise, Authoritativeness, Trustworthiness) per Google's December 2025 Quality Rater Guidelines
- **Schema validation**: JSON-LD parsing and Schema.org specification compliance
- **Date of analysis**: [Date]

### Data Sources
- Google Search Quality Rater Guidelines (December 2025 update)
- Schema.org full type hierarchy
- Industry citation studies (Zyppy, Authoritas, Semrush AI search research, 2025-2026)
- Core Web Vitals thresholds (web.dev, 2026 standards)
- AI crawler user-agent documentation (per-platform official docs)

### Glossary

| Term | Definition |
|---|---|
| GEO | Generative Engine Optimization — optimizing content to be cited by AI search platforms |
| AIO | AI Overviews — Google's AI-generated answer boxes at the top of search results |
| E-E-A-T | Experience, Expertise, Authoritativeness, Trustworthiness — Google's content quality framework |
| SSR | Server-Side Rendering — generating HTML on the server so crawlers can read content without JavaScript |
| CWV | Core Web Vitals — Google's page experience metrics (LCP, INP, CLS) |
| LCP | Largest Contentful Paint — time to render the largest visible element |
| INP | Interaction to Next Paint — responsiveness metric (replaced FID in March 2024) |
| CLS | Cumulative Layout Shift — visual stability metric |
| JSON-LD | JavaScript Object Notation for Linked Data — preferred structured data format |
| sameAs | Schema.org property linking an entity to its profiles on other platforms |
| IndexNow | Protocol for instantly notifying search engines of content changes |
| llms.txt | Proposed standard file for guiding AI systems about a site's content |
| YMYL | Your Money or Your Life — topics requiring highest E-E-A-T standards |
| SERP | Search Engine Results Page |
| Topical Authority | The depth and breadth of a site's coverage of its core topic area |
```


## Formatting and Tone Guidelines

### Formatting
- Use clean markdown throughout: tables, headers (H2/H3), bullet points, bold for emphasis
- Tables for data, bullets for recommendations, bold for key terms
- One blank line between sections for readability
- Use horizontal rules (---) to separate major sections
- All URLs should be absolute (not relative)

### Tone
- **Professional but accessible** — written for a business owner, not a developer
- **Confident and direct** — state findings as conclusions, not possibilities
- **Action-oriented** — every finding should connect to a specific action
- **Business-impact focused** — translate technical issues into business outcomes
- Avoid: jargon without explanation, hedging language, passive voice, excessive caveats
- Use: "Your site [does/does not]...", "We recommend...", "This impacts..."

### Dollar-Value Framing
Where possible, connect recommendations to business value:
- "Improving your Google AIO readiness from 35 to 70 could increase your presence in AI Overviews by an estimated 50%, which at current search volumes represents approximately 2,000 additional monthly visitors"
- "Server-side rendering would make your content accessible to ChatGPT, Perplexity, and other AI platforms — collectively representing an audience your competitors are already reaching"
- "The investment in Schema.org markup (estimated 8-16 hours of developer time) could increase your entity recognition score from 20 to 75, significantly improving citation probability"

Be conservative with estimates. State assumptions clearly. Never guarantee specific results.


## Output

Generate **GEO-CLIENT-REPORT.md** using the complete template above, filled with actual audit data. The report should be:
- 40-80 pages equivalent in detail (3,000-6,000 words)
- Ready to send to a client without editing
- Self-contained (no references to other report files — all relevant data is included)
- Printable and presentable (clean markdown formatting)


---


# GEO PDF Report Generator

## Purpose

This skill generates a professional, visually polished PDF report from GEO audit data. The PDF includes score gauges, bar charts, platform readiness visualizations, color-coded tables, and a prioritized action plan — ready to deliver directly to clients.

## Prerequisites

- **ReportLab** must be installed: `pip install reportlab`
- The PDF generation script is located at: `~/.claude/skills/geo/scripts/generate_pdf_report.py`
- Run a full GEO audit first (using `/geo-audit`) to have data to include in the report

## How to Generate a PDF Report

### Step 1: Collect Audit Data

After running a full `/geo-audit`, collect all scores, findings, and recommendations into a JSON structure. The JSON data must follow this schema:

```json
{
    "url": "https://example.com",
    "brand_name": "Example Company",
    "date": "2026-02-18",
    "geo_score": 65,
    "scores": {
        "ai_citability": 62,
        "brand_authority": 78,
        "content_eeat": 74,
        "technical": 72,
        "schema": 45,
        "platform_optimization": 59
    },
    "platforms": {
        "Google AI Overviews": 68,
        "ChatGPT": 62,
        "Perplexity": 55,
        "Gemini": 60,
        "Bing Copilot": 50
    },
    "executive_summary": "A 4-6 sentence summary of the audit findings...",
    "findings": [
        {
            "severity": "critical",
            "title": "Finding Title",
            "description": "Description of the finding and its impact."
        }
    ],
    "quick_wins": [
        "Action item 1",
        "Action item 2"
    ],
    "medium_term": [
        "Action item 1",
        "Action item 2"
    ],
    "strategic": [
        "Action item 1",
        "Action item 2"
    ],
    "crawler_access": {
        "GPTBot": {"platform": "ChatGPT", "status": "Allowed", "recommendation": "Keep allowed"},
        "ClaudeBot": {"platform": "Claude", "status": "Blocked", "recommendation": "Unblock for visibility"}
    }
}
```

### Step 2: Write JSON Data to a Temp File

Write the collected audit data to a temporary JSON file:

```bash
# Write audit data to temp file
cat > /tmp/geo-audit-data.json << 'EOF'
{ ... audit JSON data ... }
EOF
```

### Step 3: Generate the PDF

Run the PDF generation script:

```bash
python3 ~/.claude/skills/geo/scripts/generate_pdf_report.py /tmp/geo-audit-data.json GEO-REPORT-[brand].pdf
```

The script will produce a professional PDF report with:
- **Cover Page** — Brand name, URL, date, overall GEO score with visual gauge
- **Executive Summary** — Key findings and top recommendations
- **Score Breakdown** — Table and bar chart of all 6 scoring categories
- **AI Platform Readiness** — Visual horizontal bar chart per platform with scores
- **AI Crawler Access** — Color-coded table (green=allowed, red=blocked)
- **Key Findings** — Severity-coded findings list (critical/high/medium/low)
- **Prioritized Action Plan** — Quick wins, medium-term, and strategic initiatives
- **Appendix** — Methodology, data sources, and glossary

### Step 4: Return the PDF Path

After generation, tell the user where the PDF was saved and its file size.

## Complete Workflow Example

When the user runs this skill, follow this exact sequence:

1. **Check for existing audit data** — Look for recent GEO audit reports in the current directory:
   - `GEO-CLIENT-REPORT.md`
   - `GEO-AUDIT-REPORT.md`
   - Or any `GEO-*.md` files from a recent audit

2. **If no audit data exists** — Tell the user to run `/geo-audit <url>` first, then come back for the PDF.

3. **If audit data exists** — Parse the markdown report to extract:
   - Overall GEO score
   - Category scores (citability, brand authority, content/E-E-A-T, technical, schema, platform)
   - Platform readiness scores (Google AIO, ChatGPT, Perplexity, Gemini, Bing Copilot)
   - AI crawler access status
   - Key findings with severity levels
   - Quick wins, medium-term, and strategic action items
   - Executive summary

4. **Build the JSON** — Structure all data into the JSON schema shown above.

5. **Write JSON to temp file** — Save to `/tmp/geo-audit-data.json`

6. **Run the PDF generator**:
   ```bash
   python3 ~/.claude/skills/geo/scripts/generate_pdf_report.py /tmp/geo-audit-data.json "GEO-REPORT-[brand_name].pdf"
   ```

7. **Report success** — Tell the user the PDF was generated, its location, and file size.

## If the User Provides a URL

If the user runs `/geo-report-pdf https://example.com` with a URL:
1. First run a full audit: invoke the `geo-audit` skill for that URL
2. Then collect all the audit data from the generated report files
3. Generate the PDF as described above

## Parsing Markdown Audit Data

When extracting data from existing GEO markdown reports, look for these patterns:

- **GEO Score**: Look for "GEO Score: XX/100" or "Overall: XX/100" or "GEO Readiness Score: XX"
- **Category Scores**: Look for score tables with columns like "Component | Score | Weight"
- **Platform Scores**: Look for tables with "Google AI Overviews", "ChatGPT", "Perplexity", etc.
- **Crawler Status**: Look for tables with "Allowed" or "Blocked" status for crawlers like GPTBot, ClaudeBot
- **Findings**: Look for sections titled "Key Findings", "Critical Issues", "Recommendations"
- **Action Items**: Look for sections titled "Quick Wins", "Action Plan", "Recommendations"

## Notes

- If ReportLab is not installed, run: `pip install reportlab`
- The PDF is designed for US Letter size (8.5" x 11")
- Color palette: Navy primary (#1a1a2e), Blue accent (#0f3460), Coral highlight (#e94560), Green success (#00b894)
- Each page has a header line, page numbers, "Confidential" watermark, and generation date
- Score gauges use traffic-light colors: green (80+), blue (60-79), yellow (40-59), red (below 40)


---


# GEO Schema & Structured Data

## Purpose

Structured data is the primary machine-readable signal that tells AI systems what an entity IS, what it does, and how it connects to other entities. While schema markup has traditionally been about earning Google rich results, its role in GEO is fundamentally different: **structured data is how AI models understand and trust your entity**. A complete entity graph in structured data dramatically increases citation probability across all AI search platforms.

## How to Use This Skill

1. Fetch the target page HTML using curl or WebFetch
2. Detect all existing structured data (JSON-LD, Microdata, RDFa)
3. Validate detected schemas against Schema.org specifications
4. Identify missing recommended schemas based on business type
5. Generate ready-to-use JSON-LD code blocks
6. Output GEO-SCHEMA-REPORT.md


## Step 1: Detection

### Scan for JSON-LD
Look for `<script type="application/ld+json">` blocks in the HTML. Parse each block as JSON. A page may contain multiple JSON-LD blocks — collect all of them.

### Scan for Microdata
Look for elements with `itemscope`, `itemtype`, and `itemprop` attributes. Map the hierarchy of nested items. Note: Microdata is harder for AI crawlers to parse than JSON-LD. Flag a recommendation to migrate to JSON-LD if Microdata is the only format found.

### Scan for RDFa
Look for elements with `typeof`, `property`, and `vocab` attributes. Similar to Microdata — recommend migration to JSON-LD.

### Priority Order
JSON-LD is the **strongly recommended format** for GEO. Google, Bing, and AI platforms all process JSON-LD most reliably. If the site uses Microdata or RDFa exclusively, flag this as a high-priority migration.


## Step 2: Validation

For each detected schema block, validate:

1. **Valid JSON**: Is the JSON-LD syntactically valid? Check for trailing commas, unquoted keys, malformed strings.
2. **Valid @type**: Does the `@type` match a recognized Schema.org type? Check against https://schema.org/docs/full.html.
3. **Required Properties**: Does the schema include all required properties for its type? (See per-type requirements below.)
4. **Recommended Properties**: Does the schema include recommended properties that increase AI discoverability?
5. **sameAs Links**: Does the schema include `sameAs` properties linking to other platform presences?
6. **URL Validity**: Do all URLs in the schema resolve (not 404)?
7. **Nesting**: Is the schema properly nested (e.g., author inside Article, address inside Organization)?
8. **Rendering Method**: Is the JSON-LD in the server-rendered HTML or injected via JavaScript? Per Google's December 2025 guidance, **JavaScript-injected structured data may face delayed processing**. Flag any schema that requires JS execution.


## Step 3: Schema Types for GEO

### Organization (CRITICAL — every business site)
Essential for entity recognition across all AI platforms. This is how AI models identify WHAT the business is.

**Required properties:**
- `@type`: "Organization" (or subtype: Corporation, LocalBusiness, etc.)
- `name`: Official business name
- `url`: Official website URL
- `logo`: URL to logo image (ImageObject preferred)

**Recommended properties for GEO:**
- `sameAs`: Array of ALL platform URLs (see sameAs strategy below)
- `description`: 1-2 sentence description of the organization
- `foundingDate`: ISO 8601 date
- `founder`: Person schema
- `address`: PostalAddress schema
- `contactPoint`: ContactPoint with telephone, email, contactType
- `areaServed`: Geographic area
- `numberOfEmployees`: QuantitativeValue
- `industry`: Text or DefinedTerm
- `award`: Array of awards received
- `knowsAbout`: Array of topics the organization is expert in (strong GEO signal)

### LocalBusiness (for businesses with physical locations)
Extends Organization. Critical for local AI search results and Google Gemini.

**Additional required properties:**
- `address`: Full PostalAddress
- `telephone`: Phone number
- `openingHoursSpecification`: Operating hours

**Recommended for GEO:**
- `geo`: GeoCoordinates (latitude, longitude)
- `priceRange`: Price indicator
- `aggregateRating`: AggregateRating schema
- `review`: Array of Review schemas
- `hasMap`: URL to Google Maps

### Article + Author (CRITICAL for publishers)
The Author schema is one of the strongest E-E-A-T signals for AI platforms.

**Article required:**
- `@type`: "Article" (or NewsArticle, BlogPosting, TechArticle)
- `headline`: Article title
- `datePublished`: ISO 8601
- `dateModified`: ISO 8601 (critical for freshness signals)
- `author`: Person or Organization schema
- `publisher`: Organization schema with logo
- `image`: Representative image

**Author (Person) required for GEO:**
- `name`: Full name
- `url`: Author page URL on the site
- `sameAs`: LinkedIn, Twitter, personal site, Google Scholar, ORCID
- `jobTitle`: Professional title
- `worksFor`: Organization schema
- `knowsAbout`: Array of expertise areas
- `alumniOf`: Educational institutions
- `award`: Professional awards

### Product (for e-commerce)
**Required:**
- `name`, `description`, `image`
- `offers`: Offer with price, priceCurrency, availability
- `brand`: Brand schema
- `sku` or `gtin`/`mpn`

**Recommended for GEO:**
- `aggregateRating`: AggregateRating
- `review`: Array of individual reviews
- `category`: Product category
- `material`, `weight`, `width`, `height` (where applicable)

### FAQPage
**Status as of 2024**: Google restricts FAQ rich results to government and health sites. However, the FAQPage schema still serves GEO purposes — AI platforms parse FAQ structured data for question-answer extraction. Implement it for AI readability even though rich results may not appear.

**Structure:**
- `@type`: "FAQPage"
- `mainEntity`: Array of Question schemas, each with `acceptedAnswer` containing an Answer schema

### SoftwareApplication (for SaaS)
**Required:**
- `name`, `description`
- `applicationCategory`: e.g., "BusinessApplication"
- `operatingSystem`: Supported platforms
- `offers`: Pricing

**Recommended for GEO:**
- `aggregateRating`: User ratings
- `featureList`: Array of features (strong citation signal)
- `screenshot`: Screenshots
- `softwareVersion`: Current version
- `releaseNotes`: Link to changelog

### WebSite + SearchAction (for sitelinks search box)
**Structure:**
```json
{
  "@type": "WebSite",
  "name": "Site Name",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

### Person (standalone — for personal brands, authors, thought leaders)
Use as a standalone schema on About/Bio pages. This builds the entity graph for individual expertise.

**Required:** `name`, `url`
**Recommended for GEO:** `sameAs`, `jobTitle`, `worksFor`, `knowsAbout`, `alumniOf`, `award`, `description`, `image`

### speakable Property (for voice/AI assistants)
The `speakable` property marks specific sections of content as particularly suitable for voice and AI assistant consumption. Add to Article or WebPage schemas.

```json
{
  "@type": "Article",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".article-summary", ".key-takeaway"]
  }
}
```
This signals to AI assistants which passages are the best candidates for citation or reading aloud.


## Step 4: Deprecated/Changed Schemas to Flag

| Schema | Status | Note |
|---|---|---|
| HowTo | Rich results deprecated Aug 2023 | Still useful for AI parsing, but do not promise rich results |
| FAQPage | Restricted to govt/health Aug 2023 | Still useful for AI parsing (see above) |
| SpecialAnnouncement | Deprecated 2023 | Was for COVID; remove if still present |
| CourseInfo | Replaced by Course updates 2024 | Use updated Course schema properties |
| VideoObject `contentUrl` | Changed behavior 2024 | Must point to actual video file, not page URL |
| Review snippet | Stricter enforcement 2024 | Self-serving reviews on product pages may not display |

Flag any deprecated schemas found and recommend replacements.


## Step 5: sameAs Strategy (CRITICAL for Entity Recognition)

The `sameAs` property is the single most important structured data property for GEO. It tells AI systems: "This entity on my website is the SAME entity as these profiles elsewhere." This creates the entity graph that AI platforms use to verify, trust, and cite sources.

### Recommended sameAs Links (in priority order)

1. **Wikipedia article** — highest authority entity link
2. **Wikidata item** — machine-readable entity identifier (e.g., `https://www.wikidata.org/wiki/Q12345`)
3. **LinkedIn** — company page or personal profile
4. **YouTube** — channel URL
5. **Twitter/X** — profile URL
6. **Facebook** — page URL
7. **Crunchbase** — company profile (for startups/tech)
8. **GitHub** — organization or personal profile (for tech)
9. **Google Scholar** — author profile (for researchers/academics)
10. **ORCID** — researcher identifier (for academics)
11. **Instagram** — profile URL
12. **Apple App Store / Google Play** — app listings (for software)
13. **BBB** — Better Business Bureau listing (for US businesses)
14. **Industry directories** — relevant vertical directories

### sameAs Audit Process
1. Collect all known web presences for the entity
2. Check that each URL resolves (not 404 or redirected)
3. Verify the Organization/Person schema includes ALL of them
4. Check that the information on each platform is consistent (name, description, founding date, etc.)
5. Flag any platforms where the entity should have a presence but does not


## Step 6: JSON-LD Generation

Based on the detected business type, generate ready-to-paste JSON-LD blocks. Always generate:

1. **Organization or Person** (depending on entity type) — always
2. **WebSite with SearchAction** — always for the homepage
3. **Business-type-specific** — Article for publishers, Product for e-commerce, LocalBusiness for local, SoftwareApplication for SaaS
4. **BreadcrumbList** — for any page deeper than homepage

### Generation Rules
- Use the `@graph` pattern to include multiple schemas in one JSON-LD block
- All URLs must be absolute (not relative)
- Include `@id` properties for cross-referencing between schemas
- Use ISO 8601 for all dates
- Include `speakable` on Article schemas with CSS selectors pointing to key content sections
- Place JSON-LD in `<head>` section — NOT injected via JavaScript

### Template: Organization with Full GEO Signals
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 600,
    "height": 60
  },
  "description": "Concise description of what the company does.",
  "foundingDate": "2020-01-15",
  "founder": {
    "@type": "Person",
    "name": "Founder Name",
    "sameAs": "https://www.linkedin.com/in/founder"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-555-5555",
    "contactType": "customer service",
    "email": "support@example.com"
  },
  "sameAs": [
    "https://en.wikipedia.org/wiki/Company_Name",
    "https://www.wikidata.org/wiki/Q12345",
    "https://www.linkedin.com/company/company-name",
    "https://www.youtube.com/@companyname",
    "https://twitter.com/companyname",
    "https://github.com/companyname",
    "https://www.crunchbase.com/organization/company-name"
  ],
  "knowsAbout": [
    "Topic 1",
    "Topic 2",
    "Topic 3"
  ]
}
```


## Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Organization/Person schema present and complete | 15 | 15 if full, 10 if basic, 0 if none |
| sameAs links (5+ platforms) | 15 | 3 per valid sameAs link, max 15 |
| Article schema with author details | 10 | 10 if full author schema, 5 if name only, 0 if none |
| Business-type-specific schema present | 10 | 10 if complete, 5 if partial, 0 if missing |
| WebSite + SearchAction | 5 | 5 if present, 0 if not |
| BreadcrumbList on inner pages | 5 | 5 if present, 0 if not |
| JSON-LD format (not Microdata/RDFa) | 5 | 5 if JSON-LD, 3 if mixed, 0 if only Microdata/RDFa |
| Server-rendered (not JS-injected) | 10 | 10 if in HTML source, 5 if JS but in head, 0 if dynamic JS |
| speakable property on articles | 5 | 5 if present, 0 if not |
| Valid JSON + valid Schema.org types | 10 | 10 if no errors, 5 if minor issues, 0 if major errors |
| knowsAbout property on Organization/Person | 5 | 5 if present with 3+ topics, 0 if missing |
| No deprecated schemas present | 5 | 5 if clean, 0 if deprecated schemas found |


## Output Format

Generate **GEO-SCHEMA-REPORT.md** with:

```markdown
# GEO Schema & Structured Data Report — [Domain]
Date: [Date]

## Schema Score: XX/100

## Detected Schemas
| Page | Schema Type | Format | Status | Issues |
|---|---|---|---|---|
| / | Organization | JSON-LD | Valid | Missing sameAs |
| /blog/post-1 | Article | JSON-LD | Valid | No author schema |

## Validation Results
[List each schema with pass/fail per property]

## Missing Recommended Schemas
[List schemas that should be present based on business type but are not]

## sameAs Audit
| Platform | URL | Status |
|---|---|---|
| Wikipedia | [URL or "Not found"] | Present/Missing |
| LinkedIn | [URL or "Not found"] | Present/Missing |
[Continue for all recommended platforms]

## Generated JSON-LD Code
[Ready-to-paste JSON-LD blocks for each missing or incomplete schema]

## Implementation Notes
- Where to place each JSON-LD block
- Server-rendering requirements
- Testing with Google Rich Results Test and Schema.org Validator
```


---


# GEO Technical SEO Audit

## Purpose

Technical SEO forms the foundation of both traditional search visibility and AI search citation. A technically broken site cannot be crawled, indexed, or cited by any platform. This skill audits 8 categories of technical health with specific attention to GEO requirements — most critically, **server-side rendering** (AI crawlers do not execute JavaScript) and **AI crawler access** (many sites inadvertently block AI crawlers in robots.txt).

## How to Use This Skill

1. Collect the target URL (homepage + 2-3 key inner pages)
2. Fetch each page using curl/WebFetch to get raw HTML and HTTP headers
3. Run through each of the 8 audit categories below
4. Score each category using the rubric
5. Generate GEO-TECHNICAL-AUDIT.md with results


## Category 1: Crawlability (15 points)

### 1.1 robots.txt Validity
- Fetch `https://[domain]/robots.txt`
- Check for syntactic validity: proper `User-agent`, `Allow`, `Disallow` directives
- Check for common errors: missing User-agent, wildcards blocking important paths, Disallow: / blocking entire site
- Verify XML sitemap is referenced: `Sitemap: https://[domain]/sitemap.xml`

### 1.2 AI Crawler Access (CRITICAL for GEO)
Check robots.txt for directives targeting these AI crawlers:

| Crawler | User-Agent | Platform |
|---|---|---|
| GPTBot | GPTBot | ChatGPT / OpenAI |
| Google-Extended | Google-Extended | Gemini / Google AI training |
| Googlebot | Googlebot | Google Search + AI Overviews |
| Bingbot | bingbot | Bing Copilot + ChatGPT (via Bing) |
| PerplexityBot | PerplexityBot | Perplexity AI |
| ClaudeBot | ClaudeBot | Anthropic Claude |
| Amazonbot | Amazonbot | Alexa / Amazon AI |
| CCBot | CCBot | Common Crawl (used by many AI models) |
| FacebookBot | FacebookExternalHit | Meta AI |
| Bytespider | Bytespider | TikTok / ByteDance AI |
| Applebot-Extended | Applebot-Extended | Apple Intelligence |

**Scoring for AI crawler access:**
- All major AI crawlers allowed: 5 points
- Some blocked but Googlebot + Bingbot allowed: 3 points
- GPTBot or PerplexityBot blocked: 1 point (significant GEO impact)
- Googlebot blocked: 0 points (fatal)

**Important nuance**: Blocking Google-Extended does NOT block Googlebot. Google-Extended only controls AI training data usage, not search indexing. However, blocking Google-Extended may reduce presence in AI Overviews. Recommend allowing Google-Extended unless there is a specific data licensing concern.

### 1.3 XML Sitemaps
- Fetch sitemap (check robots.txt for location, or try `/sitemap.xml`, `/sitemap_index.xml`)
- Validate XML syntax
- Check for `<lastmod>` dates (should be present and accurate)
- Count URLs — compare to expected number of indexable pages
- Check for sitemap index if large site (50,000+ URLs per sitemap max)
- Verify all sitemap URLs return 200 status codes (sample check)

### 1.4 Crawl Depth
- Homepage = depth 0. Check that all important pages are reachable within **3 clicks** (depth 3)
- Pages at depth 4+ receive significantly less crawl budget and are less likely to be cited by AI
- Check internal linking: are key content pages linked from the homepage or main navigation?

### 1.5 Noindex Management
- Check for `<meta name="robots" content="noindex">` on pages that SHOULD be indexed
- Check for `X-Robots-Tag: noindex` HTTP headers
- Common mistakes: noindex on paginated pages, category pages, or key landing pages

**Category Scoring:**
| Check | Points |
|---|---|
| robots.txt valid and complete | 3 |
| AI crawlers allowed | 5 |
| XML sitemap present and valid | 3 |
| Crawl depth within 3 clicks | 2 |
| No erroneous noindex directives | 2 |


## Category 2: Indexability (12 points)

### 2.1 Canonical Tags
- Every indexable page must have a `<link rel="canonical" href="...">` tag
- Canonical must point to itself (self-referencing) for the authoritative version
- Check for conflicting canonicals (canonical in HTML vs. HTTP header)
- Check for canonical chains (A canonicals to B, B canonicals to C — should be A to C)

### 2.2 Duplicate Content
- Check for www vs. non-www (both should resolve, one should redirect)
- Check for HTTP vs. HTTPS (HTTP should redirect to HTTPS)
- Check for trailing slash consistency (pick one pattern and redirect the other)
- Check for parameter-based duplicates (`?sort=price` creating duplicate pages)

### 2.3 Pagination
- If paginated content exists, check for `rel="next"` / `rel="prev"` (note: Google ignores these as of 2019, but Bing still uses them)
- Preferred: use `rel="canonical"` on paginated pages pointing to a view-all page or the first page
- Ensure paginated pages are not noindexed if they contain unique content

### 2.4 Hreflang (international sites)
- Check for `<link rel="alternate" hreflang="xx">` tags
- Validate: reciprocal hreflang (if page A points to page B, B must point back to A)
- Validate: x-default fallback exists
- Check for language/region code validity (ISO 639-1 / ISO 3166-1)

### 2.5 Index Bloat
- Estimate number of indexed pages (check sitemap count, use `site:domain.com` estimate)
- Compare indexed pages to actual valuable content pages
- Flag if indexed pages significantly exceed content pages (index bloat from thin/duplicate/parameter pages)

**Category Scoring:**
| Check | Points |
|---|---|
| Canonical tags correct on all pages | 3 |
| No duplicate content issues | 3 |
| Pagination handled correctly | 2 |
| Hreflang correct (if applicable) | 2 |
| No index bloat | 2 |


## Category 3: Security (10 points)

### 3.1 HTTPS Enforcement
- Site must load over HTTPS
- HTTP must redirect to HTTPS (301 redirect)
- No mixed content warnings (HTTP resources on HTTPS pages)
- SSL/TLS certificate must be valid and not expired

### 3.2 Security Headers
Check HTTP response headers for:

| Header | Required Value | Purpose |
|---|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Forces HTTPS |
| `Content-Security-Policy` | Appropriate policy | Prevents XSS |
| `X-Content-Type-Options` | `nosniff` | Prevents MIME sniffing |
| `X-Frame-Options` | `DENY` or `SAMEORIGIN` | Prevents clickjacking |
| `Referrer-Policy` | `strict-origin-when-cross-origin` or stricter | Controls referrer data |
| `Permissions-Policy` | Appropriate restrictions | Controls browser features |

**Category Scoring:**
| Check | Points |
|---|---|
| HTTPS enforced with valid cert | 4 |
| HSTS header present | 2 |
| X-Content-Type-Options | 1 |
| X-Frame-Options | 1 |
| Referrer-Policy | 1 |
| Content-Security-Policy | 1 |


## Category 4: URL Structure (8 points)

### 4.1 Clean URLs
- URLs should be human-readable: `/blog/seo-guide` not `/blog?id=12345`
- No session IDs in URLs
- Lowercase only (no mixed case)
- Hyphens for word separation (not underscores)
- No special characters or encoded spaces

### 4.2 Logical Hierarchy
- URL path should reflect site architecture: `/category/subcategory/page`
- Flat where appropriate — avoid unnecessarily deep nesting
- Consistent pattern across the site

### 4.3 Redirect Chains
- Check for redirect chains (A redirects to B redirects to C)
- Maximum 1 hop recommended (A redirects to C directly)
- Check for redirect loops
- All redirects should be 301 (permanent), not 302 (temporary), unless intentionally temporary

### 4.4 Parameter Handling
- URL parameters should not create duplicate indexable pages
- Use canonical tags or `robots.txt` Disallow for parameter variations
- Configure parameter handling in Google Search Console and Bing Webmaster Tools

**Category Scoring:**
| Check | Points |
|---|---|
| Clean, readable URLs | 2 |
| Logical hierarchy | 2 |
| No redirect chains (max 1 hop) | 2 |
| Parameter handling configured | 2 |


## Category 5: Mobile Optimization (10 points)

### Critical Context
As of **July 2024**, Google crawls ALL sites exclusively with mobile Googlebot. There is no desktop crawling. If your site does not work on mobile, it does not work for Google. Period.

### 5.1 Responsive Design
- Check for `<meta name="viewport" content="width=device-width, initial-scale=1">`
- Content must not require horizontal scrolling on mobile
- No fixed-width layouts wider than viewport

### 5.2 Tap Targets
- Interactive elements (buttons, links) must be at least 48x48 CSS pixels
- Minimum 8px spacing between tap targets
- Check that navigation is usable on mobile

### 5.3 Font Sizes
- Base font size should be at least 16px
- No text requiring zoom to read
- Sufficient contrast ratio (WCAG AA: 4.5:1 for normal text, 3:1 for large text)

### 5.4 Mobile Content Parity
- All content visible on desktop must also be visible on mobile
- No hidden content behind "read more" toggles that Googlebot cannot expand (though Google has improved at expanding these as of 2025)
- Images and media must load on mobile

**Category Scoring:**
| Check | Points |
|---|---|
| Viewport meta tag correct | 3 |
| Responsive layout (no horizontal scroll) | 3 |
| Tap targets appropriately sized | 2 |
| Font sizes legible | 2 |


## Category 6: Core Web Vitals (15 points)

### 2026 Metrics and Thresholds
Core Web Vitals use the **75th percentile** of real user data (field data) as the benchmark. Lab data is useful for debugging but field data determines the ranking signal.

| Metric | Good | Needs Improvement | Poor | Notes |
|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | < 2.5s | 2.5s - 4.0s | > 4.0s | Measures loading — time until largest visible element renders |
| **INP** (Interaction to Next Paint) | < 200ms | 200ms - 500ms | > 500ms | Replaced FID in March 2024. Measures ALL interactions, not just first |
| **CLS** (Cumulative Layout Shift) | < 0.1 | 0.1 - 0.25 | > 0.25 | Measures visual stability — unexpected layout movements |

### How to Assess Without CrUX Data
When real user data is unavailable, estimate from page characteristics:
- **LCP**: Check largest above-fold element. Is it an image (check size/format)? Is it text (check web font loading)? Server response time (TTFB)?
- **INP**: Check for heavy JavaScript on page. Long tasks (>50ms) block interactivity. Check for third-party scripts.
- **CLS**: Check for images without explicit width/height. Check for dynamically inserted content above the fold. Check for web fonts causing layout shift (FOUT/FOIT).

### Common LCP Fixes
1. Optimize hero images: WebP/AVIF format, correct sizing, preload with `<link rel="preload">`
2. Reduce server response time (TTFB < 800ms)
3. Eliminate render-blocking CSS/JS
4. Preconnect to critical third-party origins

### Common INP Fixes
1. Break up long tasks (>50ms) into smaller chunks using `requestIdleCallback` or `scheduler.yield()`
2. Reduce third-party JavaScript
3. Use `content-visibility: auto` for off-screen content
4. Debounce/throttle event handlers

### Common CLS Fixes
1. Always include `width` and `height` attributes on images and videos
2. Reserve space for ads and embeds with CSS `aspect-ratio` or explicit dimensions
3. Use `font-display: swap` with size-adjusted fallback fonts
4. Avoid inserting content above existing content after page load

**Category Scoring:**
| Check | Points |
|---|---|
| LCP < 2.5s | 5 |
| INP < 200ms | 5 |
| CLS < 0.1 | 5 |


## Category 7: Server-Side Rendering (15 points) — CRITICAL FOR GEO

### Why SSR Is Mandatory for AI Visibility
AI crawlers (GPTBot, PerplexityBot, ClaudeBot, etc.) do **NOT execute JavaScript**. They fetch the raw HTML and parse it. If your content is rendered client-side by React, Vue, Angular, or any other JavaScript framework, AI crawlers see an empty page.

Even Googlebot, which does execute JavaScript, deprioritizes JS-rendered content due to the additional crawl budget required. Google processes JS rendering in a separate "rendering queue" that can delay indexing by days or weeks.

### Detection Method
1. Fetch the page with curl (no JavaScript execution): `curl -s [URL]`
2. Compare the raw HTML to the rendered DOM (via browser)
3. If key content (headings, paragraphs, product info, article text) is MISSING from the curl output, the site relies on client-side rendering

### What to Check
- **Main content text**: Is the article body / product description / page content in the raw HTML?
- **Headings**: Are H1, H2, H3 tags present in raw HTML?
- **Navigation**: Is the main navigation server-rendered?
- **Structured data**: Is JSON-LD in the raw HTML or injected by JavaScript?
- **Meta tags**: Are title, description, canonical, OG tags in the raw HTML?
- **Internal links**: Are navigation and content links in the raw HTML? (Critical for crawlability)

### SSR Solutions to Recommend
| Framework | SSR Solution |
|---|---|
| React | Next.js (SSR/SSG), Remix, Gatsby (SSG) |
| Vue | Nuxt.js (SSR/SSG) |
| Angular | Angular Universal |
| Svelte | SvelteKit |
| Generic | Prerender.io (prerendering service), Rendertron |

### Scoring Detail
- All key content server-rendered: 15 points
- Main content server-rendered but some elements JS-only: 10 points
- Critical content requires JS (product info, article text): 5 points
- Entire page is client-rendered (empty body in raw HTML): 0 points

**Category Scoring:**
| Check | Points |
|---|---|
| Main content in raw HTML | 8 |
| Meta tags + structured data in raw HTML | 4 |
| Internal links in raw HTML | 3 |


## Category 8: Page Speed & Server Performance (15 points)

### 8.1 Time to First Byte (TTFB)
- Target: **< 800ms** (ideally < 200ms)
- Measure with curl: `curl -o /dev/null -s -w 'TTFB: %{time_starttransfer}s\n' [URL]`
- If TTFB > 800ms: check server location, caching, database queries, CDN usage

### 8.2 Resource Optimization
- Total page weight target: **< 2MB** (critical pages < 1MB)
- Check for uncompressed resources (gzip/brotli compression should be enabled)
- Check for unminified CSS and JavaScript
- Check for unused CSS/JS (can represent 50%+ of downloaded bytes on many sites)

### 8.3 Image Optimization
- Check image formats: WebP or AVIF preferred over JPEG/PNG
- Check for oversized images (images larger than display size)
- Check for lazy loading: images below fold should have `loading="lazy"`
- Check for explicit dimensions (width/height attributes prevent CLS)
- Above-fold images should NOT be lazy loaded (harms LCP)

### 8.4 Code Splitting and Lazy Loading
- JavaScript should be code-split so each page only loads what it needs
- Check for large JavaScript bundles (> 200KB compressed is a warning, > 500KB is critical)
- Third-party scripts should load asynchronously (`async` or `defer`)
- Check for render-blocking resources in `<head>`

### 8.5 Caching
- Check `Cache-Control` headers on static resources (images, CSS, JS)
- Static assets should have long cache times: `max-age=31536000` (1 year) with content-hashed filenames
- HTML pages should have shorter cache or `no-cache` with validation (`ETag` or `Last-Modified`)

### 8.6 CDN Usage
- Check if static resources are served from a CDN (different domain or CDN-specific headers)
- For global audience, CDN is critical for consistent performance
- Check for CDN-specific headers: `CF-Ray` (Cloudflare), `X-Cache` (AWS CloudFront), `X-Served-By` (Fastly)

**Category Scoring:**
| Check | Points |
|---|---|
| TTFB < 800ms | 3 |
| Page weight < 2MB | 2 |
| Images optimized (format, size, lazy) | 3 |
| JS bundles reasonable (< 200KB compressed) | 2 |
| Compression enabled (gzip/brotli) | 2 |
| Cache headers on static resources | 2 |
| CDN in use | 1 |


## IndexNow Protocol

### What It Is
IndexNow is an open protocol that allows websites to notify search engines instantly when content is created, updated, or deleted. Supported by Bing, Yandex, Seznam, and Naver. Google does NOT support IndexNow but monitors the protocol.

### Why It Matters for GEO
ChatGPT uses Bing's index. Bing Copilot uses Bing's index. Faster Bing indexing means faster AI visibility on two major platforms.

### Implementation Check
1. Check for IndexNow key file: `https://[domain]/.well-known/indexnow-key.txt` or similar
2. Check if CMS has IndexNow plugin (WordPress: IndexNow plugin; many modern CMS platforms support it natively)
3. If not implemented, recommend adding it with instructions


## Overall Scoring

| Category | Max Points | Weight |
|---|---|---|
| Crawlability | 15 | Core foundation |
| Indexability | 12 | Core foundation |
| Security | 10 | Trust signal |
| URL Structure | 8 | Crawl efficiency |
| Mobile Optimization | 10 | Google requirement |
| Core Web Vitals | 15 | Ranking signal |
| Server-Side Rendering | 15 | GEO critical |
| Page Speed & Server | 15 | Performance |
| **Total** | **100** | |

### Score Interpretation
- **90-100**: Excellent — technically sound for both traditional SEO and GEO
- **70-89**: Good — minor issues to address but fundamentally solid
- **50-69**: Needs Work — significant technical debt impacting visibility
- **30-49**: Poor — major issues blocking crawling, indexing, or AI visibility
- **0-29**: Critical — fundamental technical failures requiring immediate attention


## Output Format

Generate **GEO-TECHNICAL-AUDIT.md** with:

```markdown
# GEO Technical SEO Audit — [Domain]
Date: [Date]

## Technical Score: XX/100

## Score Breakdown
| Category | Score | Status |
|---|---|---|
| Crawlability | XX/15 | Pass/Warn/Fail |
| Indexability | XX/12 | Pass/Warn/Fail |
| Security | XX/10 | Pass/Warn/Fail |
| URL Structure | XX/8 | Pass/Warn/Fail |
| Mobile Optimization | XX/10 | Pass/Warn/Fail |
| Core Web Vitals | XX/15 | Pass/Warn/Fail |
| Server-Side Rendering | XX/15 | Pass/Warn/Fail |
| Page Speed & Server | XX/15 | Pass/Warn/Fail |

Status: Pass = 80%+ of category points, Warn = 50-79%, Fail = <50%

## AI Crawler Access
| Crawler | User-Agent | Status | Recommendation |
|---|---|---|---|
| GPTBot | GPTBot | Allowed/Blocked | [Action] |
| Googlebot | Googlebot | Allowed/Blocked | [Action] |
[Continue for all AI crawlers]

## Critical Issues (fix immediately)
[List with specific page URLs and what is wrong]

## Warnings (fix this month)
[List with details]

## Recommendations (optimize this quarter)
[List with details]

## Detailed Findings
[Per-category breakdown with evidence]
```


---


# SEO Audit

You are an expert in search engine optimization. Your goal is to identify SEO issues and provide actionable recommendations to improve organic search performance.

## Initial Assessment

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before auditing, understand:

1. **Site Context**
   - What type of site? (SaaS, e-commerce, blog, etc.)
   - What's the primary business goal for SEO?
   - What keywords/topics are priorities?

2. **Current State**
   - Any known issues or concerns?
   - Current organic traffic level?
   - Recent changes or migrations?

3. **Scope**
   - Full site audit or specific pages?
   - Technical + on-page, or one focus area?
   - Access to Search Console / analytics?


## Audit Framework

### ⚠️ Important: Schema Markup Detection Limitation

**`web_fetch` and `curl` cannot reliably detect structured data / schema markup.**

Many CMS plugins (AIOSEO, Yoast, RankMath) inject JSON-LD via client-side JavaScript — it won't appear in static HTML or `web_fetch` output (which strips `<script>` tags during conversion).

**To accurately check for schema markup, use one of these methods:**
1. **Browser tool** — render the page and run: `document.querySelectorAll('script[type="application/ld+json"]')`
2. **Google Rich Results Test** — https://search.google.com/test/rich-results
3. **Screaming Frog export** — if the client provides one, use it (SF renders JavaScript)

**Never report "no schema found" based solely on `web_fetch` or `curl`.** This has led to false audit findings in production.

### Priority Order
1. **Crawlability & Indexation** (can Google find and index it?)
2. **Technical Foundations** (is the site fast and functional?)
3. **On-Page Optimization** (is content optimized?)
4. **Content Quality** (does it deserve to rank?)
5. **Authority & Links** (does it have credibility?)


## Technical SEO Audit

### Crawlability

**Robots.txt**
- Check for unintentional blocks
- Verify important pages allowed
- Check sitemap reference

**XML Sitemap**
- Exists and accessible
- Submitted to Search Console
- Contains only canonical, indexable URLs
- Updated regularly
- Proper formatting

**Site Architecture**
- Important pages within 3 clicks of homepage
- Logical hierarchy
- Internal linking structure
- No orphan pages

**Crawl Budget Issues** (for large sites)
- Parameterized URLs under control
- Faceted navigation handled properly
- Infinite scroll with pagination fallback
- Session IDs not in URLs

### Indexation

**Index Status**
- site:domain.com check
- Search Console coverage report
- Compare indexed vs. expected

**Indexation Issues**
- Noindex tags on important pages
- Canonicals pointing wrong direction
- Redirect chains/loops
- Soft 404s
- Duplicate content without canonicals

**Canonicalization**
- All pages have canonical tags
- Self-referencing canonicals on unique pages
- HTTP → HTTPS canonicals
- www vs. non-www consistency
- Trailing slash consistency

### Site Speed & Core Web Vitals

**Core Web Vitals**
- LCP (Largest Contentful Paint): < 2.5s
- INP (Interaction to Next Paint): < 200ms
- CLS (Cumulative Layout Shift): < 0.1

**Speed Factors**
- Server response time (TTFB)
- Image optimization
- JavaScript execution
- CSS delivery
- Caching headers
- CDN usage
- Font loading

**Tools**
- PageSpeed Insights
- WebPageTest
- Chrome DevTools
- Search Console Core Web Vitals report

### Mobile-Friendliness

- Responsive design (not separate m. site)
- Tap target sizes
- Viewport configured
- No horizontal scroll
- Same content as desktop
- Mobile-first indexing readiness

### Security & HTTPS

- HTTPS across entire site
- Valid SSL certificate
- No mixed content
- HTTP → HTTPS redirects
- HSTS header (bonus)

### URL Structure

- Readable, descriptive URLs
- Keywords in URLs where natural
- Consistent structure
- No unnecessary parameters
- Lowercase and hyphen-separated


## On-Page SEO Audit

### Title Tags

**Check for:**
- Unique titles for each page
- Primary keyword near beginning
- 50-60 characters (visible in SERP)
- Compelling and click-worthy
- Brand name placement (end, usually)

**Common issues:**
- Duplicate titles
- Too long (truncated)
- Too short (wasted opportunity)
- Keyword stuffing
- Missing entirely

### Meta Descriptions

**Check for:**
- Unique descriptions per page
- 150-160 characters
- Includes primary keyword
- Clear value proposition
- Call to action

**Common issues:**
- Duplicate descriptions
- Auto-generated garbage
- Too long/short
- No compelling reason to click

### Heading Structure

**Check for:**
- One H1 per page
- H1 contains primary keyword
- Logical hierarchy (H1 → H2 → H3)
- Headings describe content
- Not just for styling

**Common issues:**
- Multiple H1s
- Skip levels (H1 → H3)
- Headings used for styling only
- No H1 on page

### Content Optimization

**Primary Page Content**
- Keyword in first 100 words
- Related keywords naturally used
- Sufficient depth/length for topic
- Answers search intent
- Better than competitors

**Thin Content Issues**
- Pages with little unique content
- Tag/category pages with no value
- Doorway pages
- Duplicate or near-duplicate content

### Image Optimization

**Check for:**
- Descriptive file names
- Alt text on all images
- Alt text describes image
- Compressed file sizes
- Modern formats (WebP)
- Lazy loading implemented
- Responsive images

### Internal Linking

**Check for:**
- Important pages well-linked
- Descriptive anchor text
- Logical link relationships
- No broken internal links
- Reasonable link count per page

**Common issues:**
- Orphan pages (no internal links)
- Over-optimized anchor text
- Important pages buried
- Excessive footer/sidebar links

### Keyword Targeting

**Per Page**
- Clear primary keyword target
- Title, H1, URL aligned
- Content satisfies search intent
- Not competing with other pages (cannibalization)

**Site-Wide**
- Keyword mapping document
- No major gaps in coverage
- No keyword cannibalization
- Logical topical clusters


## Content Quality Assessment

### E-E-A-T Signals

**Experience**
- First-hand experience demonstrated
- Original insights/data
- Real examples and case studies

**Expertise**
- Author credentials visible
- Accurate, detailed information
- Properly sourced claims

**Authoritativeness**
- Recognized in the space
- Cited by others
- Industry credentials

**Trustworthiness**
- Accurate information
- Transparent about business
- Contact information available
- Privacy policy, terms
- Secure site (HTTPS)

### Content Depth

- Comprehensive coverage of topic
- Answers follow-up questions
- Better than top-ranking competitors
- Updated and current

### User Engagement Signals

- Time on page
- Bounce rate in context
- Pages per session
- Return visits


## Common Issues by Site Type

### SaaS/Product Sites
- Product pages lack content depth
- Blog not integrated with product pages
- Missing comparison/alternative pages
- Feature pages thin on content
- No glossary/educational content

### E-commerce
- Thin category pages
- Duplicate product descriptions
- Missing product schema
- Faceted navigation creating duplicates
- Out-of-stock pages mishandled

### Content/Blog Sites
- Outdated content not refreshed
- Keyword cannibalization
- No topical clustering
- Poor internal linking
- Missing author pages

### Local Business
- Inconsistent NAP
- Missing local schema
- No Google Business Profile optimization
- Missing location pages
- No local content


## Output Format

### Audit Report Structure

**Executive Summary**
- Overall health assessment
- Top 3-5 priority issues
- Quick wins identified

**Technical SEO Findings**
For each issue:
- **Issue**: What's wrong
- **Impact**: SEO impact (High/Medium/Low)
- **Evidence**: How you found it
- **Fix**: Specific recommendation
- **Priority**: 1-5 or High/Medium/Low

**On-Page SEO Findings**
Same format as above

**Content Findings**
Same format as above

**Prioritized Action Plan**
1. Critical fixes (blocking indexation/ranking)
2. High-impact improvements
3. Quick wins (easy, immediate benefit)
4. Long-term recommendations


## References

- [AI Writing Detection](references/ai-writing-detection.md): Common AI writing patterns to avoid (em dashes, overused phrases, filler words)
- For AI search optimization (AEO, GEO, LLMO, AI Overviews), see the **ai-seo** skill


## Tools Referenced

**Free Tools**
- Google Search Console (essential)
- Google PageSpeed Insights
- Bing Webmaster Tools
- Rich Results Test (**use this for schema validation — it renders JavaScript**)
- Mobile-Friendly Test
- Schema Validator

> **Note on schema detection:** `web_fetch` strips `<script>` tags (including JSON-LD) and cannot detect JS-injected schema. Always use the browser tool, Rich Results Test, or Screaming Frog for schema checks. See the warning at the top of the Audit Framework section.

**Paid Tools** (if available)
- Screaming Frog
- Ahrefs / Semrush
- Sitebulb
- ContentKing


## Task-Specific Questions

1. What pages/keywords matter most?
2. Do you have Search Console access?
3. Any recent changes or migrations?
4. Who are your top organic competitors?
5. What's your current organic traffic baseline?


## Related Skills

- **ai-seo**: For optimizing content for AI search engines (AEO, GEO, LLMO)
- **programmatic-seo**: For building SEO pages at scale
- **schema-markup**: For implementing structured data
- **page-cro**: For optimizing pages for conversion (not just ranking)
- **analytics-tracking**: For measuring SEO performance

# AI Writing Detection

Words, phrases, and punctuation patterns commonly associated with AI-generated text. Avoid these to ensure writing sounds natural and human.

Sources: Grammarly (2025), Microsoft 365 Life Hacks (2025), GPTHuman (2025), Walter Writes (2025), Textero (2025), Plagiarism Today (2025), Rolling Stone (2025), MDPI Blog (2025)

---

## Contents
- Em Dashes: The Primary AI Tell
- Overused Verbs
- Overused Adjectives
- Overused Transitions and Connectors
- Phrases That Signal AI Writing (Opening Phrases, Transitional Phrases, Concluding Phrases, Structural Patterns)
- Filler Words and Empty Intensifiers
- Academic-Specific AI Tells
- How to Self-Check

## Em Dashes: The Primary AI Tell

**The em dash (—) has become one of the most reliable markers of AI-generated content.**

Em dashes are longer than hyphens (-) and are used for emphasis, interruptions, or parenthetical information. While they have legitimate uses in writing, AI models drastically overuse them.

### Why Em Dashes Signal AI Writing
- AI models were trained on edited books, academic papers, and style guides where em dashes appear frequently
- AI uses em dashes as a shortcut for sentence variety instead of commas, colons, or parentheses
- Most human writers rarely use em dashes because they don't exist as a standard keyboard key
- The overuse is so consistent that it has become the unofficial signature of ChatGPT writing

### What To Do Instead
| Instead of | Use |
|------------|-----|
| The results—which were surprising—showed... | The results, which were surprising, showed... |
| This approach—unlike traditional methods—allows... | This approach, unlike traditional methods, allows... |
| The study found—as expected—that... | The study found, as expected, that... |
| Communication skills—both written and verbal—are essential | Communication skills (both written and verbal) are essential |

### Guidelines
- Use commas for most parenthetical information
- Use colons to introduce explanations or lists
- Use parentheses for supplementary information
- Reserve em dashes for rare, deliberate emphasis only
- If you find yourself using more than one em dash per page, revise

---

## Overused Verbs

| Avoid | Use Instead |
|-------|-------------|
| delve (into) | explore, examine, investigate, look at |
| leverage | use, apply, draw on |
| optimise | improve, refine, enhance |
| utilise | use |
| facilitate | help, enable, support |
| foster | encourage, support, develop, nurture |
| bolster | strengthen, support, reinforce |
| underscore | emphasise, highlight, stress |
| unveil | reveal, show, introduce, present |
| navigate | manage, handle, work through |
| streamline | simplify, make more efficient |
| enhance | improve, strengthen |
| endeavour | try, attempt, effort |
| ascertain | find out, determine, establish |
| elucidate | explain, clarify, make clear |

---

## Overused Adjectives

| Avoid | Use Instead |
|-------|-------------|
| robust | strong, reliable, thorough, solid |
| comprehensive | complete, thorough, full, detailed |
| pivotal | key, critical, central, important |
| crucial | important, key, essential, critical |
| vital | important, essential, necessary |
| transformative | significant, important, major |
| cutting-edge | new, advanced, recent, modern |
| groundbreaking | new, original, significant |
| innovative | new, original, creative |
| seamless | smooth, easy, effortless |
| intricate | complex, detailed, complicated |
| nuanced | subtle, complex, detailed |
| multifaceted | complex, varied, diverse |
| holistic | complete, whole, comprehensive |

---

## Overused Transitions and Connectors

| Avoid | Use Instead |
|-------|-------------|
| furthermore | also, in addition, and |
| moreover | also, and, besides |
| notwithstanding | despite, even so, still |
| that being said | however, but, still |
| at its core | essentially, fundamentally, basically |
| to put it simply | in short, simply put |
| it is worth noting that | note that, importantly |
| in the realm of | in, within, regarding |
| in the landscape of | in, within |
| in today's [anything] | currently, now, today |

---

## Phrases That Signal AI Writing

### Opening Phrases to Avoid
- "In today's fast-paced world..."
- "In today's digital age..."
- "In an era of..."
- "In the ever-evolving landscape of..."
- "In the realm of..."
- "It's important to note that..."
- "Let's delve into..."
- "Imagine a world where..."

### Transitional Phrases to Avoid
- "That being said..."
- "With that in mind..."
- "It's worth mentioning that..."
- "At its core..."
- "To put it simply..."
- "In essence..."
- "This begs the question..."

### Concluding Phrases to Avoid
- "In conclusion..."
- "To sum up..."
- "By [doing X], you can [achieve Y]..."
- "In the final analysis..."
- "All things considered..."
- "At the end of the day..."

### Structural Patterns to Avoid
- "Whether you're a [X], [Y], or [Z]..." (listing three examples after "whether")
- "It's not just [X], it's also [Y]..."
- "Think of [X] as [elaborate metaphor]..."
- Starting sentences with "By" followed by a gerund: "By understanding X, you can Y..."

---

## Filler Words and Empty Intensifiers

These words often add nothing to meaning. Remove them or find specific alternatives:

- absolutely
- actually
- basically
- certainly
- clearly
- definitely
- essentially
- extremely
- fundamentally
- incredibly
- interestingly
- naturally
- obviously
- quite
- really
- significantly
- simply
- surely
- truly
- ultimately
- undoubtedly
- very

---

## Academic-Specific AI Tells

| Avoid | Use Instead |
|-------|-------------|
| shed light on | clarify, explain, reveal |
| pave the way for | enable, allow, make possible |
| a myriad of | many, numerous, various |
| a plethora of | many, numerous, several |
| paramount | very important, essential, critical |
| pertaining to | about, regarding, concerning |
| prior to | before |
| subsequent to | after |
| in light of | because of, given, considering |
| with respect to | about, regarding, for |
| in terms of | regarding, for, about |
| the fact that | that (or rewrite sentence) |

---

## How to Self-Check

1. Read your text aloud. If phrases sound unnatural in speech, revise them
2. Ask: "Would I say this in a conversation with a colleague?"
3. Check for repetitive sentence structures
4. Look for clusters of the words listed above
5. Ensure varied sentence lengths (not all similar length)
6. Verify each intensifier adds genuine meaning


---


# AI SEO

You are an expert in AI search optimization — the practice of making content discoverable, extractable, and citable by AI systems including Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and Copilot. Your goal is to help users get their content cited as a source in AI-generated answers.

## Before Starting

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Current AI Visibility
- Do you know if your brand appears in AI-generated answers today?
- Have you checked ChatGPT, Perplexity, or Google AI Overviews for your key queries?
- What queries matter most to your business?

### 2. Content & Domain
- What type of content do you produce? (Blog, docs, comparisons, product pages)
- What's your domain authority / traditional SEO strength?
- Do you have existing structured data (schema markup)?

### 3. Goals
- Get cited as a source in AI answers?
- Appear in Google AI Overviews for specific queries?
- Compete with specific brands already getting cited?
- Optimize existing content or create new AI-optimized content?

### 4. Competitive Landscape
- Who are your top competitors in AI search results?
- Are they being cited where you're not?


## How AI Search Works

### The AI Search Landscape

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **Claude** | Brave Search (when enabled) | Training data + Brave search results |

For a deep dive on how each platform selects sources and what to optimize per platform, see [references/platform-ranking-factors.md](references/platform-ranking-factors.md).

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

In traditional search, you need to rank on page 1. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks to websites by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Statistics and citations boost visibility by 40%+ across queries


## AI Visibility Audit

Before optimizing, assess your current AI search presence.

### Step 1: Check AI Answers for Your Key Queries

Test 10-20 of your most important queries across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors Cited? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:-----------------:|
| [query 1] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |
| [query 2] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |

**Query types to test:**
- "What is [your product category]?"
- "Best [product category] for [use case]"
- "[Your brand] vs [competitor]"
- "How to [problem your product solves]"
- "[Your product category] pricing"

### Step 2: Analyze Citation Patterns

When your competitors get cited and you don't, examine:
- **Content structure** — Is their content more extractable?
- **Authority signals** — Do they have more citations, stats, expert quotes?
- **Freshness** — Is their content more recently updated?
- **Schema markup** — Do they have structured data you're missing?
- **Third-party presence** — Are they cited via Wikipedia, Reddit, review sites?

### Step 3: Content Extractability Check

For each priority page, verify:

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks (work without surrounding context)? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |
| Heading structure matches query patterns? | |
| AI bots allowed in robots.txt? | |

### Step 4: AI Bot Access Check

Verify your robots.txt allows AI crawlers. Each AI platform has its own bot, and blocking it means that platform can't cite you:

- **GPTBot** and **ChatGPT-User** — OpenAI (ChatGPT)
- **PerplexityBot** — Perplexity
- **ClaudeBot** and **anthropic-ai** — Anthropic (Claude)
- **Google-Extended** — Google Gemini and AI Overviews
- **Bingbot** — Microsoft Copilot (via Bing)

Check your robots.txt for `Disallow` rules targeting any of these. If you find them blocked, you have a business decision to make: blocking prevents AI training on your content but also prevents citation. One middle ground is blocking training-only crawlers (like **CCBot** from Common Crawl) while allowing the search bots listed above.

See [references/platform-ranking-factors.md](references/platform-ranking-factors.md) for the full robots.txt configuration.


## Optimization Strategy

### The Three Pillars

```
1. Structure (make it extractable)
2. Authority (make it citable)
3. Presence (be where AI looks)
```

### Pillar 1: Structure — Make Content Extractable

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

For detailed templates for each block type, see [references/content-patterns.md](references/content-patterns.md).

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

### Pillar 2: Authority — Make Content Citable

AI systems prefer sources they can trust. Build citation-worthiness.

**The Princeton GEO research** (KDD 2024, studied across Perplexity.ai) ranked 9 optimization methods:

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase with citations.

**Statistics and data** (+37-40% citation boost)
- Include specific numbers with sources
- Cite original research, not summaries of research
- Add dates to all statistics
- Original data beats aggregated data

**Expert attribution** (+25-30% citation boost)
- Named authors with credentials
- Expert quotes with titles and organizations
- "According to [Source]" framing for claims
- Author bios with relevant expertise

**Freshness signals**
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)
- Current year references and recent statistics
- Remove or update outdated information

**E-E-A-T alignment**
- First-hand experience demonstrated
- Specific, detailed information (not generic)
- Transparent sourcing and methodology
- Clear author expertise for the topic

### Pillar 3: Presence — Be Where AI Looks

AI systems don't just cite your website — they cite where you appear.

**Third-party sources matter more than your own site:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Quora answers

**Actions:**
- Ensure your Wikipedia page is accurate and current
- Participate authentically in Reddit communities
- Get featured in industry roundups and comparison articles
- Maintain updated profiles on relevant review platforms
- Create YouTube content for key how-to queries
- Answer relevant Quora questions with depth

### Schema Markup for AI

Structured data helps AI systems understand your content. Key schemas:

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

Content with proper schema shows 30-40% higher AI visibility. For implementation, use the **schema-markup** skill.


## Content Types That Get Cited Most

Not all content is equally citable. Prioritize these formats:

| Content Type | Citation Share | Why AI Cites It |
|-------------|:------------:|----------------|
| **Comparison articles** | ~33% | Structured, balanced, high-intent |
| **Definitive guides** | ~15% | Comprehensive, authoritative |
| **Original research/data** | ~12% | Unique, citable statistics |
| **Best-of/listicles** | ~10% | Clear structure, entity-rich |
| **Product pages** | ~10% | Specific details AI can extract |
| **How-to guides** | ~8% | Step-by-step structure |
| **Opinion/analysis** | ~10% | Expert perspective, quotable |

**Underperformers for AI citation:**
- Generic blog posts without structure
- Thin product pages with marketing fluff
- Gated content (AI can't access it)
- Content without dates or author attribution
- PDF-only content (harder for AI to parse)


## Monitoring AI Visibility

### What to Track

| Metric | What It Measures | How to Check |
|--------|-----------------|-------------|
| AI Overview presence | Do AI Overviews appear for your queries? | Manual check or Semrush/Ahrefs |
| Brand citation rate | How often you're cited in AI answers | AI visibility tools (see below) |
| Share of AI voice | Your citations vs. competitors | Peec AI, Otterly, ZipTie |
| Citation sentiment | How AI describes your brand | Manual review + monitoring tools |
| Source attribution | Which of your pages get cited | Track referral traffic from AI sources |

### AI Visibility Monitoring Tools

| Tool | Coverage | Best For |
|------|----------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice tracking |
| **Peec AI** | ChatGPT, Gemini, Perplexity, Claude, Copilot+ | Multi-platform monitoring at scale |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment tracking |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword → AI visibility mapping |

### DIY Monitoring (No Tools)

Monthly manual check:
1. Pick your top 20 queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are you cited? Who is? What page?
4. Log in a spreadsheet, track month-over-month


## AI SEO for Different Content Types

### SaaS Product Pages

**Goal:** Get cited in "What is [category]?" and "Best [category]" queries.

**Optimize:**
- Clear product description in first paragraph (what it does, who it's for)
- Feature comparison tables (you vs. category, not just competitors)
- Specific metrics ("processes 10,000 transactions/sec" not "blazing fast")
- Customer count or social proof with numbers
- Pricing transparency (AI cites pages with visible pricing)
- FAQ section addressing common buyer questions

### Blog Content

**Goal:** Get cited as an authoritative source on topics in your space.

**Optimize:**
- One clear target query per post (match heading to query)
- Definition in first paragraph for "What is" queries
- Original data, research, or expert quotes
- "Last updated" date visible
- Author bio with relevant credentials
- Internal links to related product/feature pages

### Comparison/Alternative Pages

**Goal:** Get cited in "[X] vs [Y]" and "Best [X] alternatives" queries.

**Optimize:**
- Structured comparison tables (not just prose)
- Fair and balanced (AI penalizes obviously biased comparisons)
- Specific criteria with ratings or scores
- Updated pricing and feature data
- Cite the competitor-alternatives skill for building these pages

### Documentation / Help Content

**Goal:** Get cited in "How to [X] with [your product]" queries.

**Optimize:**
- Step-by-step format with numbered lists
- Code examples where relevant
- HowTo schema markup
- Screenshots with descriptive alt text
- Clear prerequisites and expected outcomes


## Common Mistakes

- **Ignoring AI search entirely** — ~45% of Google searches now show AI Overviews, and ChatGPT/Perplexity are growing fast
- **Treating AI SEO as separate from SEO** — Good traditional SEO is the foundation; AI SEO adds structure and authority on top
- **Writing for AI, not humans** — If content reads like it was written to game an algorithm, it won't get cited or convert
- **No freshness signals** — Undated content loses to dated content. Always show when content was last updated
- **Gating all content** — AI can't access gated content. Keep your most authoritative content open
- **Ignoring third-party presence** — You may get more AI citations from a Wikipedia mention than from your own blog
- **No structured data** — Schema markup gives AI systems structured context about your content
- **Keyword stuffing** — Unlike traditional SEO where it's just ineffective, keyword stuffing actively reduces AI visibility by 10% (Princeton GEO study)
- **Blocking AI bots** — If GPTBot, PerplexityBot, or ClaudeBot are blocked in robots.txt, those platforms can't cite you
- **Generic content without data** — "We're the best" won't get cited. "Our customers see 3x improvement in [metric]" will
- **Forgetting to monitor** — You can't improve what you don't measure. Check AI visibility monthly at minimum


## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md).

| Tool | Use For |
|------|---------|
| `semrush` | AI Overview tracking, keyword research, content gap analysis |
| `ahrefs` | Backlink analysis, content explorer, AI Overview data |
| `gsc` | Search Console performance data, query tracking |
| `ga4` | Referral traffic from AI sources |


## Task-Specific Questions

1. What are your top 10-20 most important queries?
2. Have you checked if AI answers exist for those queries today?
3. Do you have structured data (schema markup) on your site?
4. What content types do you publish? (Blog, docs, comparisons, etc.)
5. Are competitors being cited by AI where you're not?
6. Do you have a Wikipedia page or presence on review sites?


## Related Skills

- **seo-audit**: For traditional technical and on-page SEO audits
- **schema-markup**: For implementing structured data that helps AI understand your content
- **content-strategy**: For planning what content to create
- **competitor-alternatives**: For building comparison pages that get cited
- **programmatic-seo**: For building SEO pages at scale
- **copywriting**: For writing content that's both human-readable and AI-extractable

# AEO and GEO Content Patterns

Reusable content block patterns optimized for answer engines and AI citation.

---

## Contents
- Answer Engine Optimization (AEO) Patterns (Definition Block, Step-by-Step Block, Comparison Table Block, Pros and Cons Block, FAQ Block, Listicle Block)
- Generative Engine Optimization (GEO) Patterns (Statistic Citation Block, Expert Quote Block, Authoritative Claim Block, Self-Contained Answer Block, Evidence Sandwich Block)
- Domain-Specific GEO Tactics (Technology Content, Health/Medical Content, Financial Content, Legal Content, Business/Marketing Content)
- Voice Search Optimization (Question Formats for Voice, Voice-Optimized Answer Structure)

## Answer Engine Optimization (AEO) Patterns

These patterns help content appear in featured snippets, AI Overviews, voice search results, and answer boxes.

### Definition Block

Use for "What is [X]?" queries.

```markdown
## What is [Term]?

[Term] is [concise 1-sentence definition]. [Expanded 1-2 sentence explanation with key characteristics]. [Brief context on why it matters or how it's used].
```

**Example:**
```markdown
## What is Answer Engine Optimization?

Answer Engine Optimization (AEO) is the practice of structuring content so AI-powered systems can easily extract and present it as direct answers to user queries. Unlike traditional SEO that focuses on ranking in search results, AEO optimizes for featured snippets, AI Overviews, and voice assistant responses. This approach has become essential as over 60% of Google searches now end without a click.
```

### Step-by-Step Block

Use for "How to [X]" queries. Optimal for list snippets.

```markdown
## How to [Action/Goal]

[1-sentence overview of the process]

1. **[Step Name]**: [Clear action description in 1-2 sentences]
2. **[Step Name]**: [Clear action description in 1-2 sentences]
3. **[Step Name]**: [Clear action description in 1-2 sentences]
4. **[Step Name]**: [Clear action description in 1-2 sentences]
5. **[Step Name]**: [Clear action description in 1-2 sentences]

[Optional: Brief note on expected outcome or time estimate]
```

**Example:**
```markdown
## How to Optimize Content for Featured Snippets

Earning featured snippets requires strategic formatting and direct answers to search queries.

1. **Identify snippet opportunities**: Use tools like Semrush or Ahrefs to find keywords where competitors have snippets you could capture.
2. **Match the snippet format**: Analyze whether the current snippet is a paragraph, list, or table, and format your content accordingly.
3. **Answer the question directly**: Provide a clear, concise answer (40-60 words for paragraph snippets) immediately after the question heading.
4. **Add supporting context**: Expand on your answer with examples, data, and expert insights in the following paragraphs.
5. **Use proper heading structure**: Place your target question as an H2 or H3, with the answer immediately following.

Most featured snippets appear within 2-4 weeks of publishing well-optimized content.
```

### Comparison Table Block

Use for "[X] vs [Y]" queries. Optimal for table snippets.

```markdown
## [Option A] vs [Option B]: [Brief Descriptor]

| Feature | [Option A] | [Option B] |
|---------|------------|------------|
| [Criteria 1] | [Value/Description] | [Value/Description] |
| [Criteria 2] | [Value/Description] | [Value/Description] |
| [Criteria 3] | [Value/Description] | [Value/Description] |
| [Criteria 4] | [Value/Description] | [Value/Description] |
| Best For | [Use case] | [Use case] |

**Bottom line**: [1-2 sentence recommendation based on different needs]
```

### Pros and Cons Block

Use for evaluation queries: "Is [X] worth it?", "Should I [X]?"

```markdown
## Advantages and Disadvantages of [Topic]

[1-sentence overview of the evaluation context]

### Pros

- **[Benefit category]**: [Specific explanation]
- **[Benefit category]**: [Specific explanation]
- **[Benefit category]**: [Specific explanation]

### Cons

- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]

**Verdict**: [1-2 sentence balanced conclusion with recommendation]
```

### FAQ Block

Use for topic pages with multiple common questions. Essential for FAQ schema.

```markdown
## Frequently Asked Questions

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].
```

**Tips for FAQ questions:**
- Use natural question phrasing ("How do I..." not "How does one...")
- Include question words: what, how, why, when, where, who, which
- Match "People Also Ask" queries from search results
- Keep answers between 50-100 words

### Listicle Block

Use for "Best [X]", "Top [X]", "[Number] ways to [X]" queries.

```markdown
## [Number] Best [Items] for [Goal/Purpose]

[1-2 sentence intro establishing context and selection criteria]

### 1. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]

### 2. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]

### 3. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]
```

---

## Generative Engine Optimization (GEO) Patterns

These patterns optimize content for citation by AI assistants like ChatGPT, Claude, Perplexity, and Gemini.

### Statistic Citation Block

Statistics increase AI citation rates by 15-30%. Always include sources.

```markdown
[Claim statement]. According to [Source/Organization], [specific statistic with number and timeframe]. [Context for why this matters].
```

**Example:**
```markdown
Mobile optimization is no longer optional for SEO success. According to Google's 2024 Core Web Vitals report, 70% of web traffic now comes from mobile devices, and pages failing mobile usability standards see 24% higher bounce rates. This makes mobile-first indexing a critical ranking factor.
```

### Expert Quote Block

Named expert attribution adds credibility and increases citation likelihood.

```markdown
"[Direct quote from expert]," says [Expert Name], [Title/Role] at [Organization]. [1 sentence of context or interpretation].
```

**Example:**
```markdown
"The shift from keyword-driven search to intent-driven discovery represents the most significant change in SEO since mobile-first indexing," says Rand Fishkin, Co-founder of SparkToro. This perspective highlights why content strategies must evolve beyond traditional keyword optimization.
```

### Authoritative Claim Block

Structure claims for easy AI extraction with clear attribution.

```markdown
[Topic] [verb: is/has/requires/involves] [clear, specific claim]. [Source] [confirms/reports/found] that [supporting evidence]. This [explains/means/suggests] [implication or action].
```

**Example:**
```markdown
E-E-A-T is the cornerstone of Google's content quality evaluation. Google's Search Quality Rater Guidelines confirm that trust is the most critical factor, stating that "untrustworthy pages have low E-E-A-T no matter how experienced, expert, or authoritative they may seem." This means content creators must prioritize transparency and accuracy above all other optimization tactics.
```

### Self-Contained Answer Block

Create quotable, standalone statements that AI can extract directly.

```markdown
**[Topic/Question]**: [Complete, self-contained answer that makes sense without additional context. Include specific details, numbers, or examples in 2-3 sentences.]
```

**Example:**
```markdown
**Ideal blog post length for SEO**: The optimal length for SEO blog posts is 1,500-2,500 words for competitive topics. This range allows comprehensive topic coverage while maintaining reader engagement. HubSpot research shows long-form content earns 77% more backlinks than short articles, directly impacting search rankings.
```

### Evidence Sandwich Block

Structure claims with evidence for maximum credibility.

```markdown
[Opening claim statement].

Evidence supporting this includes:
- [Data point 1 with source]
- [Data point 2 with source]
- [Data point 3 with source]

[Concluding statement connecting evidence to actionable insight].
```

---

## Domain-Specific GEO Tactics

Different content domains benefit from different authority signals.

### Technology Content
- Emphasize technical precision and correct terminology
- Include version numbers and dates for software/tools
- Reference official documentation
- Add code examples where relevant

### Health/Medical Content
- Cite peer-reviewed studies with publication details
- Include expert credentials (MD, RN, etc.)
- Note study limitations and context
- Add "last reviewed" dates

### Financial Content
- Reference regulatory bodies (SEC, FTC, etc.)
- Include specific numbers with timeframes
- Note that information is educational, not advice
- Cite recognized financial institutions

### Legal Content
- Cite specific laws, statutes, and regulations
- Reference jurisdiction clearly
- Include professional disclaimers
- Note when professional consultation is advised

### Business/Marketing Content
- Include case studies with measurable results
- Reference industry research and reports
- Add percentage changes and timeframes
- Quote recognized thought leaders

---

## Voice Search Optimization

Voice queries are conversational and question-based. Optimize for these patterns:

### Question Formats for Voice
- "What is..."
- "How do I..."
- "Where can I find..."
- "Why does..."
- "When should I..."
- "Who is..."

### Voice-Optimized Answer Structure
- Lead with direct answer (under 30 words ideal)
- Use natural, conversational language
- Avoid jargon unless targeting expert audience
- Include local context where relevant
- Structure for single spoken response

# How Each AI Platform Picks Sources

Each AI search platform has its own search index, ranking logic, and content preferences. This guide covers what matters for getting cited on each one.

Sources cited throughout: Princeton GEO study (KDD 2024), SE Ranking domain authority study, ZipTie content-answer fit analysis.

---

## The Fundamentals

Every AI platform shares three baseline requirements:

1. **Your content must be in their index** — Each platform uses a different search backend (Google, Bing, Brave, or their own). If you're not indexed, you can't be cited.
2. **Your content must be crawlable** — AI bots need access via robots.txt. Block the bot, lose the citation.
3. **Your content must be extractable** — AI systems pull passages, not pages. Clear structure and self-contained paragraphs win.

Beyond these basics, each platform weights different signals. Here's what matters and where.

---

## Google AI Overviews

Google AI Overviews pull from Google's own index and lean heavily on E-E-A-T signals (Experience, Expertise, Authoritativeness, Trustworthiness). They appear in roughly 45% of Google searches.

**What makes Google AI Overviews different:** They already have your traditional SEO signals — backlinks, page authority, topical relevance. The additional AI layer adds a preference for content with cited sources and structured data. Research shows that including authoritative citations in your content correlates with a 132% visibility boost, and writing with an authoritative (not salesy) tone adds another 89%.

**Importantly, AI Overviews don't just recycle the traditional Top 10.** Only about 15% of AI Overview sources overlap with conventional organic results. Pages that wouldn't crack page 1 in traditional search can still get cited if they have strong structured data and clear, extractable answers.

**What to focus on:**
- Schema markup is the single biggest lever — Article, FAQPage, HowTo, and Product schemas give AI Overviews structured context to work with (30-40% visibility boost)
- Build topical authority through content clusters with strong internal linking
- Include named, sourced citations in your content (not just claims)
- Author bios with real credentials matter — E-E-A-T is weighted heavily
- Get into Google's Knowledge Graph where possible (an accurate Wikipedia entry helps)
- Target "how to" and "what is" query patterns — these trigger AI Overviews most often

---

## ChatGPT

ChatGPT's web search draws from a Bing-based index. It combines this with its training knowledge to generate answers, then cites the web sources it relied on.

**What makes ChatGPT different:** Domain authority matters more here than on other AI platforms. An SE Ranking analysis of 129,000 domains found that authority and credibility signals account for roughly 40% of what determines citation, with content quality at about 35% and platform trust at 25%. Sites with very high referring domain counts (350K+) average 8.4 citations per response, while sites with slightly lower trust scores (91-96 vs 97-100) drop from 8.4 to 6 citations.

**Freshness is a major differentiator.** Content updated within the last 30 days gets cited about 3.2x more often than older content. ChatGPT clearly favors recent information.

**The most important signal is content-answer fit** — a ZipTie analysis of 400,000 pages found that how well your content's style and structure matches ChatGPT's own response format accounts for about 55% of citation likelihood. This is far more important than domain authority (12%) or on-page structure (14%) alone. Write the way ChatGPT would answer the question, and you're more likely to be the source it cites.

**Where ChatGPT looks beyond your site:** Wikipedia accounts for 7.8% of all ChatGPT citations, Reddit for 1.8%, and Forbes for 1.1%. Brand official sites are cited frequently but third-party mentions carry significant weight.

**What to focus on:**
- Invest in backlinks and domain authority — it's the strongest baseline signal
- Update competitive content at least monthly
- Structure your content the way ChatGPT structures its answers (conversational, direct, well-organized)
- Include verifiable statistics with named sources
- Clean heading hierarchy (H1 > H2 > H3) with descriptive headings

---

## Perplexity

Perplexity always cites its sources with clickable links, making it the most transparent AI search platform. It combines its own index with Google's and runs results through multiple reranking passes — initial relevance retrieval, then traditional ranking factor scoring, then ML-based quality evaluation that can discard entire result sets if they don't meet quality thresholds.

**What makes Perplexity different:** It's the most "research-oriented" AI search engine, and its citation behavior reflects that. Perplexity maintains curated lists of authoritative domains (Amazon, GitHub, major academic sites) that get inherent ranking boosts. It uses a time-decay algorithm that evaluates new content quickly, giving fresh publishers a real shot at citation.

**Perplexity has unique content preferences:**
- **FAQ Schema (JSON-LD)** — Pages with FAQ structured data get cited noticeably more often
- **PDF documents** — Publicly accessible PDFs (whitepapers, research reports) are prioritized. If you have authoritative PDF content gated behind a form, consider making a version public.
- **Publishing velocity** — How frequently you publish matters more than keyword targeting
- **Self-contained paragraphs** — Perplexity prefers atomic, semantically complete paragraphs it can extract cleanly

**What to focus on:**
- Allow PerplexityBot in robots.txt
- Implement FAQPage schema on any page with Q&A content
- Host PDF resources publicly (whitepapers, guides, reports)
- Add Article schema with publication and modification timestamps
- Write in clear, self-contained paragraphs that work as standalone answers
- Build deep topical authority in your specific niche

---

## Microsoft Copilot

Copilot is embedded across Microsoft's ecosystem — Edge, Windows, Microsoft 365, and Bing Search. It relies entirely on Bing's index, so if Bing hasn't indexed your content, Copilot can't cite it.

**What makes Copilot different:** The Microsoft ecosystem connection creates unique optimization opportunities. Mentions and content on LinkedIn and GitHub provide ranking boosts that other platforms don't offer. Copilot also puts more weight on page speed — sub-2-second load times are a clear threshold.

**What to focus on:**
- Submit your site to Bing Webmaster Tools (many sites only submit to Google Search Console)
- Use IndexNow protocol for faster indexing of new and updated content
- Optimize page speed to under 2 seconds
- Write clear entity definitions — when your content defines a term or concept, make the definition explicit and extractable
- Build presence on LinkedIn (publish articles, maintain company page) and GitHub if relevant
- Ensure Bingbot has full crawl access

---

## Claude

Claude uses Brave Search as its search backend when web search is enabled — not Google, not Bing. This is a completely different index, which means your Brave Search visibility directly determines whether Claude can find and cite you.

**What makes Claude different:** Claude is extremely selective about what it cites. While it processes enormous amounts of content, its citation rate is very low — it's looking for the most factually accurate, well-sourced content on a given topic. Data-rich content with specific numbers and clear attribution performs significantly better than general-purpose content.

**What to focus on:**
- Verify your content appears in Brave Search results (search for your brand and key terms at search.brave.com)
- Allow ClaudeBot and anthropic-ai user agents in robots.txt
- Maximize factual density — specific numbers, named sources, dated statistics
- Use clear, extractable structure with descriptive headings
- Cite authoritative sources within your content
- Aim to be the most factually accurate source on your topic — Claude rewards precision

---

## Allowing AI Bots in robots.txt

If your robots.txt blocks an AI bot, that platform can't cite your content. Here are the user agents to allow:

```
User-agent: GPTBot           # OpenAI — powers ChatGPT search
User-agent: ChatGPT-User     # ChatGPT browsing mode
User-agent: PerplexityBot    # Perplexity AI search
User-agent: ClaudeBot        # Anthropic Claude
User-agent: anthropic-ai     # Anthropic Claude (alternate)
User-agent: Google-Extended   # Google Gemini and AI Overviews
User-agent: Bingbot          # Microsoft Copilot (via Bing)
Allow: /
```

**Training vs. search:** Some AI bots are used for both model training and search citation. If you want to be cited but don't want your content used for training, your options are limited — GPTBot handles both for OpenAI. However, you can safely block **CCBot** (Common Crawl) without affecting any AI search citations, since it's only used for training dataset collection.

---

## Where to Start

If you're optimizing for AI search for the first time, focus your effort where your audience actually is:

**Start with Google AI Overviews** — They reach the most users (45%+ of Google searches) and you likely already have Google SEO foundations in place. Add schema markup, include cited sources in your content, and strengthen E-E-A-T signals.

**Then address ChatGPT** — It's the most-used standalone AI search tool for tech and business audiences. Focus on freshness (update content monthly), domain authority, and matching your content structure to how ChatGPT formats its responses.

**Then expand to Perplexity** — Especially valuable if your audience includes researchers, early adopters, or tech professionals. Add FAQ schema, publish PDF resources, and write in clear, self-contained paragraphs.

**Copilot and Claude are lower priority** unless your audience skews enterprise/Microsoft (Copilot) or developer/analyst (Claude). But the fundamentals — structured content, cited sources, schema markup — help across all platforms.

**Actions that help everywhere:**
1. Allow all AI bots in robots.txt
2. Implement schema markup (FAQPage, Article, Organization at minimum)
3. Include statistics with named sources in your content
4. Update content regularly — monthly for competitive topics
5. Use clear heading structure (H1 > H2 > H3)
6. Keep page load time under 2 seconds
7. Add author bios with credentials


---


# Schema Markup

You are an expert in structured data and schema markup. Your goal is to implement schema.org markup that helps search engines understand content and enables rich results in search.

## Initial Assessment

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before implementing schema, understand:

1. **Page Type** - What kind of page? What's the primary content? What rich results are possible?

2. **Current State** - Any existing schema? Errors in implementation? Which rich results already appearing?

3. **Goals** - Which rich results are you targeting? What's the business value?


## Core Principles

### 1. Accuracy First
- Schema must accurately represent page content
- Don't markup content that doesn't exist
- Keep updated when content changes

### 2. Use JSON-LD
- Google recommends JSON-LD format
- Easier to implement and maintain
- Place in `<head>` or end of `<body>`

### 3. Follow Google's Guidelines
- Only use markup Google supports
- Avoid spam tactics
- Review eligibility requirements

### 4. Validate Everything
- Test before deploying
- Monitor Search Console
- Fix errors promptly


## Common Schema Types

| Type | Use For | Required Properties |
|------|---------|-------------------|
| Organization | Company homepage/about | name, url |
| WebSite | Homepage (search box) | name, url |
| Article | Blog posts, news | headline, image, datePublished, author |
| Product | Product pages | name, image, offers |
| SoftwareApplication | SaaS/app pages | name, offers |
| FAQPage | FAQ content | mainEntity (Q&A array) |
| HowTo | Tutorials | name, step |
| BreadcrumbList | Any page with breadcrumbs | itemListElement |
| LocalBusiness | Local business pages | name, address |
| Event | Events, webinars | name, startDate, location |

**For complete JSON-LD examples**: See [references/schema-examples.md](references/schema-examples.md)


## Quick Reference

### Organization (Company Page)
Required: name, url
Recommended: logo, sameAs (social profiles), contactPoint

### Article/BlogPosting
Required: headline, image, datePublished, author
Recommended: dateModified, publisher, description

### Product
Required: name, image, offers (price + availability)
Recommended: sku, brand, aggregateRating, review

### FAQPage
Required: mainEntity (array of Question/Answer pairs)

### BreadcrumbList
Required: itemListElement (array with position, name, item)


## Multiple Schema Types

You can combine multiple schema types on one page using `@graph`:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", ... },
    { "@type": "WebSite", ... },
    { "@type": "BreadcrumbList", ... }
  ]
}
```


## Validation and Testing

### Tools
- **Google Rich Results Test**: https://search.google.com/test/rich-results
- **Schema.org Validator**: https://validator.schema.org/
- **Search Console**: Enhancements reports

### Common Errors

**Missing required properties** - Check Google's documentation for required fields

**Invalid values** - Dates must be ISO 8601, URLs fully qualified, enumerations exact

**Mismatch with page content** - Schema doesn't match visible content


## Implementation

### Static Sites
- Add JSON-LD directly in HTML template
- Use includes/partials for reusable schema

### Dynamic Sites (React, Next.js)
- Component that renders schema
- Server-side rendered for SEO
- Serialize data to JSON-LD

### CMS / WordPress
- Plugins (Yoast, Rank Math, Schema Pro)
- Theme modifications
- Custom fields to structured data


## Output Format

### Schema Implementation
```json
// Full JSON-LD code block
{
  "@context": "https://schema.org",
  "@type": "...",
  // Complete markup
}
```

### Testing Checklist
- [ ] Validates in Rich Results Test
- [ ] No errors or warnings
- [ ] Matches page content
- [ ] All required properties included


## Task-Specific Questions

1. What type of page is this?
2. What rich results are you hoping to achieve?
3. What data is available to populate the schema?
4. Is there existing schema on the page?
5. What's your tech stack?


## Related Skills

- **seo-audit**: For overall SEO including schema review
- **ai-seo**: For AI search optimization (schema helps AI understand content)
- **programmatic-seo**: For templated schema at scale

# Schema Markup Examples

Complete JSON-LD examples for common schema types.

## Contents
- Organization
- WebSite (with SearchAction)
- Article / BlogPosting
- Product
- SoftwareApplication
- FAQPage
- HowTo
- BreadcrumbList
- LocalBusiness
- Event
- Multiple Schema Types
- Implementation Example (Next.js)

## Organization

For company/brand homepage or about page.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Company",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://twitter.com/example",
    "https://linkedin.com/company/example",
    "https://facebook.com/example"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-555-5555",
    "contactType": "customer service"
  }
}
```

---

## WebSite (with SearchAction)

For homepage, enables sitelinks search box.

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Example",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

## Article / BlogPosting

For blog posts and news articles.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Implement Schema Markup",
  "image": "https://example.com/image.jpg",
  "datePublished": "2024-01-15T08:00:00+00:00",
  "dateModified": "2024-01-20T10:00:00+00:00",
  "author": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://example.com/authors/jane"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Example Company",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "description": "A complete guide to implementing schema markup...",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/schema-guide"
  }
}
```

---

## Product

For product pages (e-commerce or SaaS).

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Premium Widget",
  "image": "https://example.com/widget.jpg",
  "description": "Our best-selling widget for professionals",
  "sku": "WIDGET-001",
  "brand": {
    "@type": "Brand",
    "name": "Example Co"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/products/widget",
    "priceCurrency": "USD",
    "price": "99.99",
    "availability": "https://schema.org/InStock",
    "priceValidUntil": "2024-12-31"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

---

## SoftwareApplication

For SaaS product pages and app landing pages.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Example App",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web, iOS, Android",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "ratingCount": "1250"
  }
}
```

---

## FAQPage

For pages with frequently asked questions.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is schema markup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Schema markup is a structured data vocabulary that helps search engines understand your content..."
      }
    },
    {
      "@type": "Question",
      "name": "How do I implement schema?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The recommended approach is to use JSON-LD format, placing the script in your page's head..."
      }
    }
  ]
}
```

---

## HowTo

For instructional content and tutorials.

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Add Schema Markup to Your Website",
  "description": "A step-by-step guide to implementing JSON-LD schema",
  "totalTime": "PT15M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Choose your schema type",
      "text": "Identify the appropriate schema type for your page content...",
      "url": "https://example.com/guide#step1"
    },
    {
      "@type": "HowToStep",
      "name": "Write the JSON-LD",
      "text": "Create the JSON-LD markup following schema.org specifications...",
      "url": "https://example.com/guide#step2"
    },
    {
      "@type": "HowToStep",
      "name": "Add to your page",
      "text": "Insert the script tag in your page's head section...",
      "url": "https://example.com/guide#step3"
    }
  ]
}
```

---

## BreadcrumbList

For any page with breadcrumb navigation.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://example.com/blog"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "SEO Guide",
      "item": "https://example.com/blog/seo-guide"
    }
  ]
}
```

---

## LocalBusiness

For local business location pages.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Example Coffee Shop",
  "image": "https://example.com/shop.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street",
    "addressLocality": "San Francisco",
    "addressRegion": "CA",
    "postalCode": "94102",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "37.7749",
    "longitude": "-122.4194"
  },
  "telephone": "+1-555-555-5555",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "08:00",
      "closes": "18:00"
    }
  ],
  "priceRange": "$$"
}
```

---

## Event

For event pages, webinars, conferences.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Annual Marketing Conference",
  "startDate": "2024-06-15T09:00:00-07:00",
  "endDate": "2024-06-15T17:00:00-07:00",
  "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "VirtualLocation",
    "url": "https://example.com/conference"
  },
  "image": "https://example.com/conference.jpg",
  "description": "Join us for our annual marketing conference...",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/conference/tickets",
    "price": "199",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "validFrom": "2024-01-01"
  },
  "performer": {
    "@type": "Organization",
    "name": "Example Company"
  },
  "organizer": {
    "@type": "Organization",
    "name": "Example Company",
    "url": "https://example.com"
  }
}
```

---

## Multiple Schema Types

Combine multiple schema types using @graph.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Company",
      "url": "https://example.com"
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com",
      "name": "Example",
      "publisher": {
        "@id": "https://example.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [...]
    }
  ]
}
```

---

## Implementation Example (Next.js)

```jsx
export default function ProductPage({ product }) {
  const schema = {
    "@context": "https://schema.org",
    "@type": "Product",
    name: product.name,
    // ... other properties
  };

  return (
    <>
      <Head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
        />
      </Head>
      {/* Page content */}
    </>
  );
}
```


---


# Programmatic SEO

You are an expert in programmatic SEO—building SEO-optimized pages at scale using templates and data. Your goal is to create pages that rank, provide value, and avoid thin content penalties.

## Initial Assessment

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before designing a programmatic SEO strategy, understand:

1. **Business Context**
   - What's the product/service?
   - Who is the target audience?
   - What's the conversion goal for these pages?

2. **Opportunity Assessment**
   - What search patterns exist?
   - How many potential pages?
   - What's the search volume distribution?

3. **Competitive Landscape**
   - Who ranks for these terms now?
   - What do their pages look like?
   - Can you realistically compete?


## Core Principles

### 1. Unique Value Per Page
- Every page must provide value specific to that page
- Not just swapped variables in a template
- Maximize unique content—the more differentiated, the better

### 2. Proprietary Data Wins
Hierarchy of data defensibility:
1. Proprietary (you created it)
2. Product-derived (from your users)
3. User-generated (your community)
4. Licensed (exclusive access)
5. Public (anyone can use—weakest)

### 3. Clean URL Structure
**Always use subfolders, not subdomains**:
- Good: `yoursite.com/templates/resume/`
- Bad: `templates.yoursite.com/resume/`

### 4. Genuine Search Intent Match
Pages must actually answer what people are searching for.

### 5. Quality Over Quantity
Better to have 100 great pages than 10,000 thin ones.

### 6. Avoid Google Penalties
- No doorway pages
- No keyword stuffing
- No duplicate content
- Genuine utility for users


## The 12 Playbooks (Overview)

| Playbook | Pattern | Example |
|----------|---------|---------|
| Templates | "[Type] template" | "resume template" |
| Curation | "best [category]" | "best website builders" |
| Conversions | "[X] to [Y]" | "$10 USD to GBP" |
| Comparisons | "[X] vs [Y]" | "webflow vs wordpress" |
| Examples | "[type] examples" | "landing page examples" |
| Locations | "[service] in [location]" | "dentists in austin" |
| Personas | "[product] for [audience]" | "crm for real estate" |
| Integrations | "[product A] [product B] integration" | "slack asana integration" |
| Glossary | "what is [term]" | "what is pSEO" |
| Translations | Content in multiple languages | Localized content |
| Directory | "[category] tools" | "ai copywriting tools" |
| Profiles | "[entity name]" | "stripe ceo" |

**For detailed playbook implementation**: See [references/playbooks.md](references/playbooks.md)


## Choosing Your Playbook

| If you have... | Consider... |
|----------------|-------------|
| Proprietary data | Directories, Profiles |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility product | Conversions |
| Content/expertise | Glossary, Curation |
| Competitor landscape | Comparisons |

You can layer multiple playbooks (e.g., "Best coworking spaces in San Diego").


## Implementation Framework

### 1. Keyword Pattern Research

**Identify the pattern:**
- What's the repeating structure?
- What are the variables?
- How many unique combinations exist?

**Validate demand:**
- Aggregate search volume
- Volume distribution (head vs. long tail)
- Trend direction

### 2. Data Requirements

**Identify data sources:**
- What data populates each page?
- Is it first-party, scraped, licensed, public?
- How is it updated?

### 3. Template Design

**Page structure:**
- Header with target keyword
- Unique intro (not just variables swapped)
- Data-driven sections
- Related pages / internal links
- CTAs appropriate to intent

**Ensuring uniqueness:**
- Each page needs unique value
- Conditional content based on data
- Original insights/analysis per page

### 4. Internal Linking Architecture

**Hub and spoke model:**
- Hub: Main category page
- Spokes: Individual programmatic pages
- Cross-links between related spokes

**Avoid orphan pages:**
- Every page reachable from main site
- XML sitemap for all pages
- Breadcrumbs with structured data

### 5. Indexation Strategy

- Prioritize high-volume patterns
- Noindex very thin variations
- Manage crawl budget thoughtfully
- Separate sitemaps by page type


## Quality Checks

### Pre-Launch Checklist

**Content quality:**
- [ ] Each page provides unique value
- [ ] Answers search intent
- [ ] Readable and useful

**Technical SEO:**
- [ ] Unique titles and meta descriptions
- [ ] Proper heading structure
- [ ] Schema markup implemented
- [ ] Page speed acceptable

**Internal linking:**
- [ ] Connected to site architecture
- [ ] Related pages linked
- [ ] No orphan pages

**Indexation:**
- [ ] In XML sitemap
- [ ] Crawlable
- [ ] No conflicting noindex

### Post-Launch Monitoring

Track: Indexation rate, Rankings, Traffic, Engagement, Conversion

Watch for: Thin content warnings, Ranking drops, Manual actions, Crawl errors


## Common Mistakes

- **Thin content**: Just swapping city names in identical content
- **Keyword cannibalization**: Multiple pages targeting same keyword
- **Over-generation**: Creating pages with no search demand
- **Poor data quality**: Outdated or incorrect information
- **Ignoring UX**: Pages exist for Google, not users


## Output Format

### Strategy Document
- Opportunity analysis
- Implementation plan
- Content guidelines

### Page Template
- URL structure
- Title/meta templates
- Content outline
- Schema markup


## Task-Specific Questions

1. What keyword patterns are you targeting?
2. What data do you have (or can acquire)?
3. How many pages are you planning?
4. What does your site authority look like?
5. Who currently ranks for these terms?
6. What's your technical stack?


## Related Skills

- **seo-audit**: For auditing programmatic pages after launch
- **schema-markup**: For adding structured data
- **competitor-alternatives**: For comparison page frameworks

# The 12 Programmatic SEO Playbooks

Beyond mixing and matching data point permutations, these are the proven playbooks for programmatic SEO.

## Contents
- 1. Templates
- 2. Curation
- 3. Conversions
- 4. Comparisons
- 5. Examples
- 6. Locations
- 7. Personas
- 8. Integrations
- 9. Glossary
- 10. Translations
- 11. Directory
- 12. Profiles
- Choosing Your Playbook (Match to Your Assets, Combine Playbooks)

## 1. Templates

**Pattern**: "[Type] template" or "free [type] template"
**Example searches**: "resume template", "invoice template", "pitch deck template"

**What it is**: Downloadable or interactive templates users can use directly.

**Why it works**:
- High intent—people need it now
- Shareable/linkable assets
- Natural for product-led companies

**Value requirements**:
- Actually usable templates (not just previews)
- Multiple variations per type
- Quality comparable to paid options
- Easy download/use flow

**URL structure**: `/templates/[type]/` or `/templates/[category]/[type]/`

---

## 2. Curation

**Pattern**: "best [category]" or "top [number] [things]"
**Example searches**: "best website builders", "top 10 crm software", "best free design tools"

**What it is**: Curated lists ranking or recommending options in a category.

**Why it works**:
- Comparison shoppers searching for guidance
- High commercial intent
- Evergreen with updates

**Value requirements**:
- Genuine evaluation criteria
- Real testing or expertise
- Regular updates (date visible)
- Not just affiliate-driven rankings

**URL structure**: `/best/[category]/` or `/[category]/best/`

---

## 3. Conversions

**Pattern**: "[X] to [Y]" or "[amount] [unit] in [unit]"
**Example searches**: "$10 USD to GBP", "100 kg to lbs", "pdf to word"

**What it is**: Tools or pages that convert between formats, units, or currencies.

**Why it works**:
- Instant utility
- Extremely high search volume
- Repeat usage potential

**Value requirements**:
- Accurate, real-time data
- Fast, functional tool
- Related conversions suggested
- Mobile-friendly interface

**URL structure**: `/convert/[from]-to-[to]/` or `/[from]-to-[to]-converter/`

---

## 4. Comparisons

**Pattern**: "[X] vs [Y]" or "[X] alternative"
**Example searches**: "webflow vs wordpress", "notion vs coda", "figma alternatives"

**What it is**: Head-to-head comparisons between products, tools, or options.

**Why it works**:
- High purchase intent
- Clear search pattern
- Scales with number of competitors

**Value requirements**:
- Honest, balanced analysis
- Actual feature comparison data
- Clear recommendation by use case
- Updated when products change

**URL structure**: `/compare/[x]-vs-[y]/` or `/[x]-vs-[y]/`

*See also: competitor-alternatives skill for detailed frameworks*

---

## 5. Examples

**Pattern**: "[type] examples" or "[category] inspiration"
**Example searches**: "saas landing page examples", "email subject line examples", "portfolio website examples"

**What it is**: Galleries or collections of real-world examples for inspiration.

**Why it works**:
- Research phase traffic
- Highly shareable
- Natural for design/creative tools

**Value requirements**:
- Real, high-quality examples
- Screenshots or embeds
- Categorization/filtering
- Analysis of why they work

**URL structure**: `/examples/[type]/` or `/[type]-examples/`

---

## 6. Locations

**Pattern**: "[service/thing] in [location]"
**Example searches**: "coworking spaces in san diego", "dentists in austin", "best restaurants in brooklyn"

**What it is**: Location-specific pages for services, businesses, or information.

**Why it works**:
- Local intent is massive
- Scales with geography
- Natural for marketplaces/directories

**Value requirements**:
- Actual local data (not just city name swapped)
- Local providers/options listed
- Location-specific insights (pricing, regulations)
- Map integration helpful

**URL structure**: `/[service]/[city]/` or `/locations/[city]/[service]/`

---

## 7. Personas

**Pattern**: "[product] for [audience]" or "[solution] for [role/industry]"
**Example searches**: "payroll software for agencies", "crm for real estate", "project management for freelancers"

**What it is**: Tailored landing pages addressing specific audience segments.

**Why it works**:
- Speaks directly to searcher's context
- Higher conversion than generic pages
- Scales with personas

**Value requirements**:
- Genuine persona-specific content
- Relevant features highlighted
- Testimonials from that segment
- Use cases specific to audience

**URL structure**: `/for/[persona]/` or `/solutions/[industry]/`

---

## 8. Integrations

**Pattern**: "[your product] [other product] integration" or "[product] + [product]"
**Example searches**: "slack asana integration", "zapier airtable", "hubspot salesforce sync"

**What it is**: Pages explaining how your product works with other tools.

**Why it works**:
- Captures users of other products
- High intent (they want the solution)
- Scales with integration ecosystem

**Value requirements**:
- Real integration details
- Setup instructions
- Use cases for the combination
- Working integration (not vaporware)

**URL structure**: `/integrations/[product]/` or `/connect/[product]/`

---

## 9. Glossary

**Pattern**: "what is [term]" or "[term] definition" or "[term] meaning"
**Example searches**: "what is pSEO", "api definition", "what does crm stand for"

**What it is**: Educational definitions of industry terms and concepts.

**Why it works**:
- Top-of-funnel awareness
- Establishes expertise
- Natural internal linking opportunities

**Value requirements**:
- Clear, accurate definitions
- Examples and context
- Related terms linked
- More depth than a dictionary

**URL structure**: `/glossary/[term]/` or `/learn/[term]/`

---

## 10. Translations

**Pattern**: Same content in multiple languages
**Example searches**: "qué es pSEO", "was ist SEO", "マーケティングとは"

**What it is**: Your content translated and localized for other language markets.

**Why it works**:
- Opens entirely new markets
- Lower competition in many languages
- Multiplies your content reach

**Value requirements**:
- Quality translation (not just Google Translate)
- Cultural localization
- hreflang tags properly implemented
- Native speaker review

**URL structure**: `/[lang]/[page]/` or `yoursite.com/es/`, `/de/`, etc.

---

## 11. Directory

**Pattern**: "[category] tools" or "[type] software" or "[category] companies"
**Example searches**: "ai copywriting tools", "email marketing software", "crm companies"

**What it is**: Comprehensive directories listing options in a category.

**Why it works**:
- Research phase capture
- Link building magnet
- Natural for aggregators/reviewers

**Value requirements**:
- Comprehensive coverage
- Useful filtering/sorting
- Details per listing (not just names)
- Regular updates

**URL structure**: `/directory/[category]/` or `/[category]-directory/`

---

## 12. Profiles

**Pattern**: "[person/company name]" or "[entity] + [attribute]"
**Example searches**: "stripe ceo", "airbnb founding story", "elon musk companies"

**What it is**: Profile pages about notable people, companies, or entities.

**Why it works**:
- Informational intent traffic
- Builds topical authority
- Natural for B2B, news, research

**Value requirements**:
- Accurate, sourced information
- Regularly updated
- Unique insights or aggregation
- Not just Wikipedia rehash

**URL structure**: `/people/[name]/` or `/companies/[name]/`

---

## Choosing Your Playbook

### Match to Your Assets

| If you have... | Consider... |
|----------------|-------------|
| Proprietary data | Stats, Directories, Profiles |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility product | Conversions |
| Content/expertise | Glossary, Curation |
| International potential | Translations |
| Competitor landscape | Comparisons |

### Combine Playbooks

You can layer multiple playbooks:
- **Locations + Personas**: "Marketing agencies for startups in Austin"
- **Curation + Locations**: "Best coworking spaces in San Diego"
- **Integrations + Personas**: "Slack for sales teams"
- **Glossary + Translations**: Multi-language educational content

