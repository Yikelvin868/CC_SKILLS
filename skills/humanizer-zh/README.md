# humanizer-zh

中文版去 AI 味 skill，针对 Claude Code。

## 与原版的关系

衍生自 [blader/humanizer](https://github.com/blader/humanizer)（MIT）的设计——
保留了它的双轮自检 + 灵魂注入 + 风格校准三大流程，但 **28 个检测模式
全部按中文场景重写**，不是翻译。

英文 humanizer 检测的"em dash 滥用、testament/landscape 等 AI 词、
Title Case 标题"等模式对中文文本基本无效；中文 AI 味是另一套——
"赋能/闭环/抓手/打造/夯实/聚焦"互联网黑话、"切实/扎实/统筹"
公文体侵蚀、"未来可期/砥砺前行"万能升华、"一是二是三是"
强行三段式等。

## 安装

已装在 `~/.claude/skills/humanizer-zh/`。`/restart` Claude Code 后生效。

## 使用

```
/humanizer-zh

[把要改的中文段落贴这里]
```

或自然语言触发：

```
帮我把这段去 AI 味：
[正文]
```

带写作样本（推荐）：

```
参考我的写作风格：
[贴你以前写过的 2-3 段]

把下面这段改成像我写的：
[正文]
```

## 适用场景

- ✅ 中文 BP、公司介绍、融资材料
- ✅ 公众号文章、知乎回答
- ✅ 中文技术文档、内部周报
- ✅ 中文邮件、商务沟通
- ❌ 英文文本 → 用原版 [blader/humanizer](https://github.com/blader/humanizer)

## License

MIT，沿用上游。
