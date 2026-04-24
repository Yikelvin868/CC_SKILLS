# 虹识技术 VI 规范 Skill

## 概述

本 Skill 定义虹识技术（HOMSH）的品牌视觉识别规范，用于生成符合公司 VI 标准的文档、报告、演示文稿和网页内容。

## 触发条件

当用户请求生成以下内容时自动应用：
- 虹识技术相关文档（提案、报告、技术文档）
- 带有 HOMSH 品牌标识的任何输出
- 用户明确要求应用虹识 VI 规范

触发关键词：虹识、HOMSH、虹识技术、Hongshi、虹膜识别

---

## 品牌配色体系

### 主色

| 名称 | 色值 | 用途 |
|------|------|------|
| 品牌红 | `#E60012` | 标题、强调、重要信息、品牌标识 |
| 深黑 | `#231F20` | 正文、次要标题、主要文字 |
| 纯白 | `#FFFFFF` | 背景、反白文字 |

### 辅助色

| 名称 | 色值 | 用途 |
|------|------|------|
| 中灰 | `#666666` | 注释、说明文字、次要信息 |
| 浅灰 | `#F5F5F5` | 代码块背景、表格交替行 |
| 边框灰 | `#E0E0E0` | 分隔线、表格边框 |

### CSS 变量定义

```css
:root {
  /* 主色 */
  --homsh-red: #E60012;
  --homsh-black: #231F20;
  --homsh-white: #FFFFFF;

  /* 辅助色 */
  --homsh-gray: #666666;
  --homsh-light-gray: #F5F5F5;
  --homsh-border: #E0E0E0;
}
```

---

## 字体规范

### 中文字体优先级

```css
font-family: "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
```

1. **思源黑体** (Source Han Sans SC) - 首选
2. **苹方** (PingFang SC) - macOS 回退
3. **微软雅黑** (Microsoft YaHei) - Windows 回退
4. **Noto Sans CJK** - Linux/通用回退

### 英文/数字字体

```css
font-family: "Inter", "SF Pro Display", "Segoe UI", -apple-system, sans-serif;
```

### 代码字体

```css
font-family: "JetBrains Mono", "Fira Code", "SF Mono", "Consolas", monospace;
```

---

## 文档排版规范

### 标题层级

| 层级 | 样式 | 示例 |
|------|------|------|
| H1 | 品牌红 `#E60012`，24-28px，加粗 | 文档主标题 |
| H2 | 深黑 `#231F20`，20-22px，加粗 | 章节标题 |
| H3 | 深黑 `#231F20`，16-18px，加粗 | 小节标题 |
| 正文 | 深黑 `#231F20`，14-16px，常规 | 段落内容 |

### 强调样式

- **重要强调**：品牌红 `#E60012` + 加粗
- **次要强调**：深黑 `#231F20` + 加粗
- **链接文字**：品牌红 `#E60012` + 下划线
- **引用文字**：中灰 `#666666` + 左边框品牌红

### 表格样式

```css
/* 表头 */
th {
  background-color: #E60012;
  color: #FFFFFF;
  font-weight: bold;
}

/* 表格行 */
tr:nth-child(even) {
  background-color: #F5F5F5;
}

/* 边框 */
table, th, td {
  border: 1px solid #E0E0E0;
}
```

### 代码块样式

```css
pre, code {
  background-color: #F5F5F5;
  border: 1px solid #E0E0E0;
  border-radius: 4px;
  font-family: "JetBrains Mono", monospace;
}
```

---

## 输出格式规范

### HTML 输出

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    :root {
      --homsh-red: #E60012;
      --homsh-black: #231F20;
    }
    body {
      font-family: "Source Han Sans SC", "PingFang SC", sans-serif;
      color: var(--homsh-black);
      line-height: 1.6;
    }
    h1 { color: var(--homsh-red); }
    h2, h3 { color: var(--homsh-black); }
    a { color: var(--homsh-red); }
    .highlight { color: var(--homsh-red); font-weight: bold; }
  </style>
</head>
<body>
  <!-- 内容 -->
</body>
</html>
```

### PDF 输出 (reportlab)

```python
from reportlab.lib.colors import HexColor

HOMSH_RED = HexColor('#E60012')
HOMSH_BLACK = HexColor('#231F20')
HOMSH_GRAY = HexColor('#666666')

# 标题样式
title_style = ParagraphStyle(
    'Title',
    fontName='SourceHanSansSC',
    fontSize=24,
    textColor=HOMSH_RED,
    spaceAfter=20
)

# 正文样式
body_style = ParagraphStyle(
    'Body',
    fontName='SourceHanSansSC',
    fontSize=12,
    textColor=HOMSH_BLACK,
    leading=18
)
```

### PPTX 输出

- 标题幻灯片：品牌红背景 + 白色文字
- 内容幻灯片：白色背景 + 深黑文字 + 品牌红强调
- 页脚：品牌红细线 + 公司名称

### DOCX 输出

- 标题1：品牌红、加粗、24pt
- 标题2：深黑、加粗、18pt
- 正文：深黑、常规、12pt
- 页眉：公司 Logo + 文档标题
- 页脚：页码 + 品牌红细线

---

## 公司信息

### 名称

- 中文全称：**虹识技术**
- 英文全称：**Hongshi Technologies**
- 品牌简称：**HOMSH**

### 业务领域

- 虹膜识别技术
- 生物特征识别设备
- 安防解决方案

### 品牌标语

「虹膜识别，安全可靠」

---

## 使用示例

### 示例1：生成技术文档

用户请求：「生成 FitEye 产品技术文档」

应用规范：
- 文档标题使用品牌红
- 技术参数表格使用标准表格样式
- 代码示例使用代码块样式

### 示例2：生成绩效报告

用户请求：「生成员工周评报告 PDF」

应用规范：
- 报告标题：品牌红
- 评分等级 A/B：品牌红显示
- 评分等级 D：品牌红警示
- 表格表头：品牌红背景

### 示例3：生成演示文稿

用户请求：「生成投资提案 PPT」

应用规范：
- 封面：品牌红背景 + 白色标题
- 内容页：白色背景 + 深黑正文
- 数据图表：品牌红为主色调

---

## 禁止事项

1. **禁止**使用品牌红以外的红色（如 #FF0000）
2. **禁止**在深色背景上使用深黑文字
3. **禁止**使用渐变色替代纯色
4. **禁止**在非强调场景滥用品牌红
5. **禁止**使用非规范字体

---

*版本：1.0 | 更新日期：2026年1月*
