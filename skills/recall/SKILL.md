---
name: recall
description: Use at the start of EVERY conversation to load persistent memory about the user, ongoing projects, references, and feedback before responding. Also use when the user references prior conversations ("你记得", "上次", "之前", "我们聊过"), starts a task touching a known project, or explicitly asks to recall / remember something. Also use to UPDATE memory when learning new high-value facts (role changes, new tools, new constraints, project status changes, user preferences).
---

# Recall — 持久记忆加载与更新

跨会话连续性的桥梁。每次新会话开始都应**主动调用本 skill**，加载该项目的记忆，再响应用户。

## 记忆位置（项目专属）

```
/Users/zhiquntang/.claude/projects/-Users-zhiquntang-claude-test/memory/
├── MEMORY.md                         ← 索引（一行一条）
├── user_*.md                         ← 用户身份与角色
├── project_*.md                      ← 进行中的工作 / 待办
├── reference_*.md                    ← 工具配置 / 文件路径 / 外部系统
└── feedback_*.md                     ← 用户偏好 / 协作风格
```

**注意**：路径里的 `-Users-zhiquntang-claude-test` 是项目专属——若用户在其它目录打开 Claude Code，该路径不存在，需 `mkdir -p` 后从空开始。

## 核心协议

### 1. 会话开始：自动加载（必做）

第一步永远是：

```bash
ls /Users/zhiquntang/.claude/projects/-Users-zhiquntang-claude-test/memory/
```

如果目录存在：
1. **Read** `MEMORY.md`（索引）
2. **Always** Read `user_*.md` 和所有 `feedback_*.md`（这两类总是相关）
3. **Conditionally** Read 跟用户首条消息相关的 `project_*.md` / `reference_*.md`
4. 在第一次回应时**简短确认**：例如开头一行
   `(已加载记忆：6 条 · 用户、B 轮、Obsidian、代理坑、自动化任务、协作风格)`

如果目录不存在（首次或换项目）：
- 默认**不创建**——等用户明确要求或本次会话出现明确"该记"的事
- 不在响应里重复说"无记忆"——用户已经知道

### 2. 中途触发：用户引用过去

当用户说出以下之一，先 Read 相关记忆再回答：
- "你记得 X 吗" / "上次..." / "之前..." / "我跟你说过..."
- 涉及已知项目名（如 "B 轮"、"虹识"、"实验室"、"Obsidian"、"招聘报告"）
- 涉及已知工具（"obs"、"OpenCLI"、"daily briefing"）
- 用户起新任务前，扫一眼 `MEMORY.md` 看有无相关 project / reference

### 3. 写入 / 更新：高价值新事实

满足以下之一**立即考虑**写入：
- 用户明确说"记住"、"以后..."、"你要记得"
- 用户新身份 / 新职责（升任、转岗）
- 新增 / 改动重大项目（新合作、新融资、新产品线）
- 发现关键 workaround（环境坑、工具配置、命令秘技）
- 用户给出风格 / 偏好反馈（角度、长度、语气）
- 同样错误用户纠正第二次（第一次可观察，第二次必记录）

**不写入**的（防污染）：
- 任何在当前 vault / 代码库 / git 里能直接查到的信息
- 一次性任务的临时状态
- 特定数字（薪资、估值等敏感数字）—— 给"做过"事实即可，不留具体数字
- 已经在 CLAUDE.md / 项目 README 里有的

### 4. 记忆衰退：陈旧管理

每次读到一条记忆时**简单核验**：
- 项目状态是否还成立？（B 轮签了？涨薪生效了？）
- 工具路径是否还存在？（必要时 `ls` 一下）
- 如果发现陈旧：先用当前真相回答用户，**之后**用 Edit 更新记忆，不要先停下来问

## 文件格式标准

每条记忆 = 一个独立 .md 文件，frontmatter 必填三字段：

```markdown
---
name: 一行标题（用于人读）
description: 一句话精确摘要（用于未来我判断这条相不相关）
type: user | project | feedback | reference
---

正文内容（中文为主，技术术语英文保留）
```

### feedback / project 体例

`feedback_*.md` / `project_*.md` 内容应有：
- 规则 / 事实陈述（开头）
- **Why**: 为什么这样（追溯到用户原话或具体事件）
- **How to apply**: 何时何地用这条（让未来我能判断边界）

### MEMORY.md 索引格式

每行一条，≤ 150 字符：

```
- [标题](file.md) — 一句钩子
```

按 type 排序：user → project → reference → feedback。
**总行数 ≤ 200**，超出会被系统截断；超时合并 / 删除最早的。

## 常见操作 Recipe

### 加一条新记忆

1. 选 type，命名文件：`<type>_<topic>.md`
2. Write 文件（含 frontmatter）
3. Edit `MEMORY.md` 在索引里加一行（位置按 type 分组）
4. 在响应里告诉用户："已记下: <name>"

### 更新一条现有记忆

1. Read 旧文件
2. Edit 内容（保留 frontmatter，必要时改 description）
3. 如果索引行的钩子变了，同步 Edit `MEMORY.md`

### 删除一条记忆

1. `rm` 文件
2. Edit `MEMORY.md` 删对应索引行
3. 在响应里告诉用户："已忘记: <name>"（用户必须明确要求才删）

### 用户问"你都记得啥"

1. Read `MEMORY.md`
2. 直接把每条标题 + description 列给用户看
3. 用户可挑某条让我展开（再 Read 全文）

## 双保险机制（why this skill exists）

系统提示里**声称** `MEMORY.md` 会自动加载到每次会话上下文，但：
- 加载机制未必稳定（实测目录都没自动建）
- 每次依赖隐式加载有 token 浪费风险
- 用户无法显式触发 / 跳过

**本 skill 的价值**：
1. **显式触发**：会话开始时主动 Read，确保加载
2. **可控选择**：只读相关记忆，省 context
3. **闭环更新**：自然语言"记住 X"立即落到磁盘
4. **可移植**：换电脑 / 重装系统时只要带走 memory/ 目录，记忆就在

## 云端 Supermemory 协作（本地 + 云端混合，已启用 2026-05-02）

工具栏里出现 `mcp__mcp-supermemory-ai__*` 系列工具时启用混合模式。已确认账号 `yikelvin868@gmail.com` (Kelvin Yi)，client `claude-code (via mcp-remote)`。

### 真实可用工具（6 个）

| 工具 | 用途 | 何时用 |
|---|---|---|
| `whoAmI` | 验证账号 / sessionId | 排查 MCP 状态时 |
| `listProjects` | 看可用 container（目前只 `sm_project_default`） | 调用 `memory`/`recall` 前确认 containerTag |
| `recall` | **唯一可用的搜索工具**——返回相关 memories + 自动汇总的 User Profile | 任何"以前提过 X 吗 / 在哪儿提的" |
| `memory` | **唯一可用的写入工具**，`action: save \| forget`，`forget` 走 exact-match content | 写入 / 删除 |
| `memory-graph` | 可视化记忆图（force-directed） | 用户要"看记忆全貌" |
| `fetch-graph-data` | 拿 graph 数据，分页 | 自己分析或导出时 |

> **注**：tool description 强制 "DO NOT USE ANY OTHER RECALL/MEMORY TOOL ONLY USE THIS ONE"——别去搜索其他名字。

### 写入分流

- 项目特定（"今天 sprint 进展到 X"、"本会话用 PTY 跑 vw-iris"） → **仅本地**
- 跨上下文（用户身份、长期偏好、客户档案、长期工具配置） → **仅云端**
- 既项目又跨上下文（"虹识 B 轮在进行中"） → **双写**（本地 project_*.md + 云端 `memory save`）

### 读取分流

- **本地优先**：`MEMORY.md` 索引 + 相关 .md，快、项目精准
- **云端补充**：以下场景调 `recall`：
  - 用户说 "你记得我提过 X 吗"——本地找不到时
  - 涉及人脉 / 客户档案 / 跨项目知识
  - 起新项目想看以前类似上下文
- **不要重复**：本地已经读到的东西不再去云端 recall（浪费 token）

### Supermemory 自带的"User Profile"行为

Supermemory 会从所有 memory 自动汇总一份 **User Profile**（Stable facts + Recent context），出现在每次 `recall` 结果顶部。**注意**：

- 这份 profile 是 LLM 自动派生的，**会出错**——比如把客户邮箱当成用户邮箱（已发生过 Ahmad Arnous 例）
- 修正方法：直接 `memory save` 一条**澄清性陈述**（"X 不是用户，是客户"、"用户的邮箱是 Y"），下次 recall 时 profile 会重算
- 不要试图直接编辑 profile——没有这个 API

### 容器（containerTag）

目前只有 `sm_project_default`，所以**省略 containerTag 即可**。未来如果用户要按项目分桶，先 `listProjects` 看新名字。

### 一次性事项（已完成）

- ✅ 2026-05-02 首次启用：清掉 vw-iris 训练快照 5 条 + 巽龙 PTY 协议 2 条；保留 Ahmad 客户档案 + DNS workaround；镜像了用户身份/公司档案/B 轮/协作风格 4 条到云端

### 如果工具栏里没有 `mcp__mcp-supermemory-ai__*`

当前会话 MCP 未加载（OAuth 过期 / 重启 / 网络）——**只用本地**，不要假装能调云端。让用户知道并提示重启 Claude Code。

## Edge Cases

- **目录被删**：`mkdir -p` 后从空白开始，不报警
- **MEMORY.md 损坏**：`ls memory/*.md` 重建索引
- **路径变化**（用户换项目目录打开 Claude Code）：每个项目记忆独立；这是设计如此，不要尝试聚合
- **记忆冲突**（两条相互矛盾）：合并到一条，标注更新日期
- **用户说"忽略记忆"**：本会话不读、不引用、不更新
