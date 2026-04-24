---
name: ai-marketing
description: AI-powered marketing automation suite — Content quality scoring (Expert Panel), cold outbound optimization, and SEO intelligence. Use for: LinkedIn post scoring, email campaign optimization, competitor keyword research, content quality gates.
metadata: {"openclaw":{"emoji":"📊","always":false}}
---

# AI Marketing Skills

3 个营销自动化技能，来自 Single Brain 团队（数百万美元营收验证）：

## 1. Content Ops — 内容质量打分

**触发词：**
- "expert panel this"
- "score this post"
- "quality check"
- "rate this content"
- "给这篇帖子打分"

**用途：**
- LinkedIn 帖子发布前质量检查
- 邮件文案优化
- 落地页转化率评分

**工作流：**
1. 自动组装 7-10 名领域专家（包含 AI 检测器 1.5x 权重）
2. 递归迭代直到所有评分 ≥90（最多 3 轮）
3. 输出改进建议 + 最终版本

**详细文档：** `content-ops-SKILL.md`

---

## 2. Outbound Engine — 冷邮件自动化

**触发词：**
- "optimize cold email"
- "outbound campaign"
- "generate outreach sequence"
- "冷邮件优化"

**用途：**
- ICP 定义 → 线索挖掘 → 邮件序列生成
- 竞品监控（自动抓取竞品动态）
- 个性化邮件生成

**工作流：**
1. 定义理想客户画像（ICP）
2. 从目标市场挖掘线索
3. 生成多轮跟进邮件序列
4. 自动个性化（公司名、痛点、近期动态）

**详细文档：** `outbound-engine-SKILL.md`

---

## 3. SEO Ops — SEO 情报挖掘

**触发词：**
- "find competitor keywords"
- "SEO gap analysis"
- "content attack brief"
- "找竞品关键词"

**用途：**
- 竞品关键词分析（人脸识别、指纹识别厂商）
- Google Search Console 数据优化
- 趋势侦查（行业热点关键词）

**工作流：**
1. 输入竞品域名列表
2. 抓取他们排名的关键词
3. 找到你还没覆盖的空白点
4. 生成内容攻击简报（Content Attack Brief）

**详细文档：** `seo-ops-SKILL.md`

---

## 依赖

所有 Python 依赖已安装：
- anthropic（Claude API）
- feedparser（RSS 解析）
- requests（HTTP 请求）
- google-api-python-client（GSC API）
- google-auth（Google 认证）

---

## 快速开始

### Content Ops 示例

```bash
# 给 LinkedIn 帖子打分
python3 content-ops/scripts/expert_panel.py \
  --content "your_post.md" \
  --type "linkedin" \
  --offer "iris recognition biometric security"
```

### Outbound Engine 示例

```bash
# 生成冷邮件序列
python3 outbound-engine/scripts/cold_outbound_optimizer.py \
  --icp "biometric integrators in Middle East" \
  --offer "iris recognition module" \
  --sequence-length 3
```

### SEO Ops 示例

```bash
# 竞品关键词分析
python3 seo-ops/scripts/content_attack_brief.py \
  --competitors "faceid.com,fingerprint-tech.com" \
  --domain "homshtech.com"
```

---

## 配置

某些功能需要 API Key：

- **Content Ops**：`ANTHROPIC_API_KEY`（Claude）
- **SEO Ops**：Google Search Console 凭证（`credentials.json`）

---

## 注意事项

1. **Content Ops 不要过度依赖**：专家打分是辅助工具，不是替代人类判断
2. **Outbound Engine 合规使用**：遵守 GDPR/CAN-SPAM 等法规
3. **SEO Ops 数据时效**：关键词排名实时变化，定期更新

---

*安装时间：2026-03-31*  
*仓库：https://github.com/ericosiu/ai-marketing-skills*
