---
name: product-launch
description: 一天内从零构建完整的产品线上销售系统：建站、支付、SEO、广告、AI客服全链路
user_invocable: true
---

# Product Launch — 一天建成全球销售系统

## 技能概述

将一个成熟的硬件/软件产品，在一天内搭建成可接单收款的全球线上销售系统。覆盖建站、支付、获客、客服全链路，全程 AI 驱动，一人可操作。

灵感来源：Medvi 模式（一人公司 $4 亿营收）

## 适用场景

- 新产品上线需要快速搭建销售渠道
- 已有产品但缺乏线上获客能力
- 想验证市场需求，最小成本试错
- B2B 硬件/模组/配件类产品全球销售

## 执行流程（按顺序）

### Phase 1: 资料准备（30 分钟）
```
输入：产品名称、规格、图片、定价
工具：Claude（文案）、现有产品资料
输出：产品描述、特性列表、规格表、分类定价
```

### Phase 2: 建站（2 小时）
```
技术栈：Next.js + Tailwind CSS + Cloudflare Pages
步骤：
1. npx create-next-app（TypeScript + Tailwind）
2. 创建产品数据（src/lib/products.ts）— 类型化、可扩展
3. 首页（Hero + 产品卡片 + 应用场景 + 信任背书 + CTA）
4. 产品详情页（图片画廊 + 规格表 + 阶梯定价 + JSON-LD）
5. 定价页（阶梯定价 + FAQ）
6. 联系页（Web3Forms 表单 → 邮箱）
7. Datasheet 页（可打印，@media print 优化）
8. 部署：next.config.ts 设 output:"export" → wrangler pages deploy out
9. 绑定子域名（Cloudflare DNS CNAME → xxx.pages.dev）
```

### Phase 3: 支付系统（30 分钟）
```
工具：Stripe Payment Links
步骤：
1. Stripe API 创建 Product → Price → Payment Link
2. Payment Link 支持数量调整（1-100）+ 收货地址
3. 产品页 Buy Now 按钮 → 跳转 Stripe 托管结账页
4. 大单走 Request Quote → 联系表单
关键参数：
- adjustable_quantity: enabled, min 1, max 100
- shipping_address_collection: 目标国家列表
- after_completion: redirect 回网站
```

### Phase 4: 客户触达（30 分钟）
```
组件：
1. WhatsApp 浮窗按钮 — 固定右下角，链接 wa.me/号码
2. Web3Forms 联系表单 — 询盘发到 sales 邮箱
3. AI 客服聊天组件 — 连接 Ollama API（通过 Cloudflare Tunnel）
   - 系统提示词包含完整产品规格和定价
   - 流式响应（streaming）
   - 使用轻量模型（gemma4:e4b）降低延迟
```

### Phase 5: SEO / GEO（1 小时）
```
基础 SEO：
1. 每页 title + description + OpenGraph + Twitter Card
2. JSON-LD Product schema（产品页）+ Article schema（博客）
3. sitemap.xml + robots.txt（静态文件）
4. Google Search Console 提交 sitemap

博客内容（5 篇起步）：
1. 产品对比文章（"X vs Y"）— 吸引选型客户
2. 集成指南（"How to integrate"）— 吸引技术决策者
3. 买家指南（"Best X for Y in 2026"）— 抢排名
4. 垂直行业指南 — 展示专业度
5. 区域市场分析 — 瞄准目标市场

GEO（生成引擎优化）：
- 结构化 FAQ（LLM 偏爱引用）
- 数据+引用（LLM 优先选择有数据的内容）
- Reddit/YouTube 发布（ChatGPT/Perplexity 重度索引源）
- 安装 Tailwind Typography 插件确保博客排版正确
```

### Phase 6: 付费广告（30 分钟）
```
Google Ads 配置：
1. Campaign 1 — 高购买意向关键词（$40/天）
2. Campaign 2 — 对比/研究型关键词（$20/天）
3. Campaign 3 — 区域/行业关键词（$15/天）

广告文案模板：
- H1: [品牌] [产品类型]
- H2: [核心卖点1] | [核心卖点2]
- H3: From $[价格] | [行动号召]
- D1: [产品描述，包含关键规格]
- D2: [信任元素 + 购买引导]

Sitelinks: 主力产品、第二产品、定价页、联系页
Google Tag: gtag.js + config 嵌入 layout.tsx
```

### Phase 7: 分析追踪（15 分钟）
```
1. Cloudflare Web Analytics — 免费，无 cookie
2. Google Tag (AW-ID) — 广告转化追踪
3. Google Search Console — 搜索表现监控
```

## 技术架构

```
用户浏览器
  ├── modules.xxx.com (Cloudflare Pages, 静态站)
  │     ├── 产品页 → Stripe Payment Link (支付)
  │     ├── 联系表单 → Web3Forms → 邮箱
  │     ├── AI 聊天 → api.xxx.com → Ollama (本地模型)
  │     └── WhatsApp → wa.me/号码
  │
  ├── Cloudflare Tunnel (gemma4)
  │     ├── ai.xxx.com → Open WebUI (:3000)
  │     └── api.xxx.com → Ollama API (:11434)
  │
  └── 追踪
        ├── Cloudflare Web Analytics
        └── Google Tag (Ads 转化)
```

## 关键文件清单

```
项目根目录/
├── src/
│   ├── lib/
│   │   ├── products.ts          # 产品数据（类型化，可扩展）
│   │   └── blog.ts              # 博客文章数据
│   ├── app/
│   │   ├── layout.tsx           # 全局布局 + Analytics + Google Tag
│   │   ├── page.tsx             # 首页
│   │   ├── products/
│   │   │   ├── page.tsx         # 产品列表
│   │   │   └── [id]/page.tsx    # 产品详情（JSON-LD）
│   │   ├── pricing/page.tsx     # 阶梯定价
│   │   ├── contact/
│   │   │   ├── page.tsx         # 联系页
│   │   │   └── ContactForm.tsx  # Web3Forms 表单
│   │   ├── blog/
│   │   │   ├── page.tsx         # 博客列表
│   │   │   └── [slug]/page.tsx  # 文章详情（JSON-LD）
│   │   └── datasheets/
│   │       └── [id]/page.tsx    # 可打印 Datasheet
│   └── components/
│       ├── Header.tsx           # 导航栏
│       ├── Footer.tsx           # 页脚
│       ├── ProductCard.tsx      # 产品卡片
│       ├── ImageGallery.tsx     # 图片画廊
│       ├── WhatsAppButton.tsx   # WhatsApp 浮窗
│       └── ChatWidget.tsx       # AI 客服聊天
├── public/
│   ├── images/                  # 产品图片
│   ├── sitemap.xml              # 站点地图
│   └── robots.txt               # 爬虫规则
├── next.config.ts               # output: "export"
└── .env.local                   # Stripe keys（不提交 git）
```

## 部署命令

```bash
# 构建 + 部署
pnpm build && wrangler pages deploy out --project-name=项目名 --commit-dirty=true

# 提交代码
git add -A && git commit -m "描述" && git push
```

## Cloudflare Tunnel 管理

```bash
# 启动隧道
cloudflared tunnel run 隧道名

# 配置文件：~/.cloudflared/config.yml
# 添加新子域名：cloudflared tunnel route dns 隧道名 子域名

# 启动脚本：~/start-gemma-webui.sh
# 停止脚本：~/stop-gemma-webui.sh
```

## 成本结构（月度）

| 项目 | 费用 |
|------|------|
| Cloudflare Pages | 免费 |
| Cloudflare Analytics | 免费 |
| Web3Forms | 免费 |
| Stripe | 4.5%/笔（成交时才收） |
| Google Ads | ~$2,250（可调） |
| Claude API（内容生成） | ~$150 |
| Ollama（本地模型） | 电费 |
| **总计固定成本** | **~$500/月（不含广告）** |

## 添加新产品的步骤

1. 准备产品图片放入 `public/images/新产品ID/`
2. 在 `src/lib/products.ts` 添加产品数据
3. Stripe API 创建 Product → Price → Payment Link
4. 将 Payment Link URL 写入产品数据的 `stripePaymentLink` 字段
5. 更新 `public/sitemap.xml` 添加新页面
6. `pnpm build && wrangler pages deploy out`
7. Google Search Console 重新提交 sitemap

## 实战案例

2026-04-04 为虹识技术（HOMSH）虹膜识别模组搭建：
- 网站：modules.homshtech.com
- 产品：MD31（USB 模组 $235-299）、MI30（FPC 模组 $235-299）
- 从零到全功能上线：约 10 小时
- 包含：产品页、支付、5篇博客、AI客服、Google Ads、转化追踪
