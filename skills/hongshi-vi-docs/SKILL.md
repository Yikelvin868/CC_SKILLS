---
name: hongshi-vi-docs
description: 为虹识技术（Hongshi Technologies / HOMSH）生成符合VI规范的品牌文档。支持PPT演示文稿(.pptx)、Word文档(.docx)、PDF报告。当用户请求创建虹识技术的投资提案、产品介绍、技术文档、公司介绍等任何需要体现虹识品牌形象的文档时使用此技能。触发词：虹识、HOMSH、虹识技术、虹膜识别。
---

# 虹识技术 VI 文档生成

为虹识技术生成符合品牌VI规范的专业文档。

## 核心设计理念

**三大特质**：克制、力量感、秩序感

- **克制**：大面积留白、纯色运用、拒绝视觉噪音
- **力量感**：品牌红与深黑的高对比组合
- **秩序感**：严格网格、精确比例、一致对齐

**品牌认知**：生物识别·可信身份

## 品牌色彩（必须严格使用）

| 用途 | HEX | RGB |
|------|-----|-----|
| 品牌红（主色） | #E60012 | 230, 0, 18 |
| 深黑 | #231F20 | 35, 31, 32 |
| 中性灰 | #808080 | 128, 128, 128 |
| 白色 | #FFFFFF | 255, 255, 255 |

## 字体规范

- **中文**：思源黑体 (Source Han Sans)
  - Heavy: 封面/大标题
  - Medium: 小标题
  - Light/Regular: 正文
- **英文**：Source Sans Pro 或其他无衬线几何字体

## 背景组合规则

✅ **允许**：
- 纯红底 + 白字
- 纯黑底 + 白字/红字
- 浅灰/白底 + 黑字/灰字

❌ **禁止**：渐变、蓝色科幻风、多色混合

## 工作流程

### 1. 确认文档类型

询问用户需要的格式（默认PPT）：
- **PPT (.pptx)**: 投资提案、产品演示、技术介绍
- **Word (.docx)**: 正式报告、技术文档、合同
- **PDF**: 最终交付、打印材料

### 2. 读取完整VI规范

```bash
view references/vi-spec.md
```

### 3. 按格式生成

#### PPT演示文稿

读取并遵循 `/mnt/skills/public/pptx/SKILL.md` 的html2pptx工作流。

**关键样式设置**：
```css
:root {
  --hongshi-red: #E60012;
  --hongshi-black: #231F20;
  --hongshi-gray: #808080;
  --hongshi-white: #FFFFFF;
  --font-cn: "Source Han Sans SC", "Noto Sans SC", sans-serif;
  --font-en: "Source Sans Pro", sans-serif;
}
```

**页面类型**：
- 封面页：纯红或纯黑背景，LOGO居中/上中，标题≤2行
- 内容页：白/灰背景，LOGO置于右下角
- 结束页：LOGO居中，可配Slogan，网址 www.homsh.cn

**LOGO使用**：
```javascript
// 使用技能内的LOGO文件
const logoPath = "assets/logo2.png";
```

#### Word文档

读取并遵循 `/mnt/skills/public/docx/SKILL.md` 的工作流。

**样式配置**：
```javascript
styles: {
  default: { 
    document: { 
      run: { font: "Source Han Sans SC", size: 24 } 
    } 
  },
  paragraphStyles: [
    { id: "Heading1", run: { size: 36, bold: true, color: "E60012" } },
    { id: "Heading2", run: { size: 28, bold: true, color: "231F20" } }
  ]
}
```

#### PDF报告

读取 `/mnt/skills/public/pdf/SKILL.md`。推荐先生成Word/PPT，再转换为PDF：
```bash
soffice --headless --convert-to pdf document.docx
```

### 4. 视觉验证

生成后必须转换为图片检查：
```bash
soffice --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

检查要点：
- LOGO位置和安全空间是否正确
- 色彩是否严格符合品牌色
- 是否有渐变、蓝色等禁止元素
- 文字对比度和可读性

## 设计禁区

生成任何虹识文档时，绝对禁止：

- ❌ 蓝色科技风格
- ❌ 渐变背景或元素
- ❌ 卡通/插画风格
- ❌ 花哨图标
- ❌ 多字体混用
- ❌ 过度动画效果
- ❌ 圆角卡片风格

## 资源文件

- `assets/logo2.png` - 虹识技术标准LOGO（红色虹膜图标+HOMSH+虹识技术）
- `references/vi-spec.md` - 完整VI规范参考

## 公司信息

- 公司名称：武汉虹识技术有限公司 / Wuhan Hongshi Technology Co., Ltd.
- 英文品牌：HOMSH / HOMSH TECHNOLOGY
- 官网：www.homsh.cn
- 核心技术：虹膜识别、PhaseIris算法、OVAI人工智能
- 品牌主张：虹膜识别·洞察本质
