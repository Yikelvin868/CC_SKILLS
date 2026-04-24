# 微信公众号文章导出技能

## 概述

批量下载微信公众号文章，支持多种导出格式。

## 使用方式

### 1. 在线网站（推荐）

```bash
open "https://down.mptext.top"
```

### 2. 本地 Docker 部署

```bash
docker run -d -p 3000:3000 ghcr.io/wechat-article/wechat-article-exporter:latest
open "http://localhost:3000"
```

### 3. 本地开发运行

```bash
cd ~/Desktop/学习/程序设计/wechat-article-exporter
corepack enable && corepack prepare yarn@1.22.22 --activate
yarn install
yarn dev
# 访问 http://localhost:3000
```

## 支持的导出格式

| 格式 | 说明 |
|------|------|
| HTML | 100% 还原文章排版样式，打包图片和样式 |
| Markdown | 纯文本格式，适合二次编辑 |
| DOCX | Word 文档格式 |
| Excel | 表格格式，含文章元数据 |
| JSON | 原始数据格式 |
| TXT | 纯文本 |

## 使用步骤

1. 打开网站后，用微信扫码登录公众号后台
2. 搜索目标公众号
3. 选择要下载的文章（可按时间、作者、标题过滤）
4. 选择导出格式并下载

## 高级功能

- 导出阅读量、评论数据（需要抓包获取 credentials）
- 合集批量下载
- 图片/视频分享消息支持

## 相关链接

- 在线网站: https://down.mptext.top
- 文档站点: https://docs.mptext.top
- GitHub: https://github.com/wechat-article/wechat-article-exporter
- 本地项目: ~/Desktop/学习/程序设计/wechat-article-exporter/
