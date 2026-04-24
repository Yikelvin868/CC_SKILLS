---
name: frontend-slides
description: 用代码生成精美的HTML网页版幻灯片/PPT。支持从零创建或将PPTX转换为网页。当用户想做演示文稿、投资人PPT、产品介绍、技术分享等幻灯片时使用。生成的是单文件HTML，比PowerPoint更漂亮、更动感。
---

# Frontend Slides Skill（太極龍版）

基于 @zarazhangrui 的 frontend-slides 项目，用Claude Code生成零依赖的HTML幻灯片。

## 核心特点
- **零依赖**：单个HTML文件，内联CSS/JS，永久可用
- **视觉探索**：先生成3种风格预览，看而选择
- **反AI滥用风格**：杜绝紫色渐变+白底的俗气模板
- **动画丰富**：滚动触发、键盘导航、触控支持
- **PPTX转换**：可将现有PPT转为漂亮网页

## 使用方法

### 方式1：通过Claude Code（推荐，效果最好）

```bash
# 启动Claude Code，加载skill
claude --dangerously-skip-permissions
# 然后输入：/frontend-slides
```

Claude Code会：
1. 询问演示目的、内容
2. 询问想要的感觉（震撼/活力/专业/平静）
3. 生成3套风格预览让你挑选
4. 生成完整幻灯片

### 方式2：直接描述需求

告诉太極龍：
- 演示主题和目的
- 大概几页
- 偏好风格（可选）

太極龍直接生成HTML文件。

## 可用风格（12种）

| 风格名 | 适合场景 |
|--------|---------|
| Bold Signal | 投资人路演、主旨演讲 |
| Electric Studio | 商业提案、机构演示 |
| Dark Botanical | 高端品牌、精品发布 |
| Neon Cyber | 科技创业、黑客风 |
| Terminal Green | 开发者工具、API介绍 |
| Swiss Modern | 企业数据、简洁报告 |
| Notebook Tabs | 调研报告、产品评测 |
| Pastel Geometry | 产品概述、友好展示 |
| Vintage Editorial | 个人品牌、故事叙述 |
| Paper & Ink | 学术、思考型内容 |
| Creative Voltage | 创意机构、活力展示 |
| Split Pastel | 现代创意机构 |

## 输出文件
- 保存至：`/Users/kaijunyi/Downloads/太极龙工作间/`
- 格式：`[主题]_slides_[日期].html`
- 同时备份到：`~/.openclaw/workspace/slides/`

## 技能文件路径
- `~/.claude/skills/frontend-slides/SKILL.md`（Claude Code使用）
- `~/.claude/skills/frontend-slides/STYLE_PRESETS.md`（样式参考）
