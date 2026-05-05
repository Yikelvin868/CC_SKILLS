---
name: obs-dispatch
description: |
  Obsidian 到 Day One 的实时任务投递系统。用户在 Obsidian 任意笔记里写
  `<日期> <内容> #DL`，保存后系统通过 fswatch 监听 + Python 解析 + Day One CLI
  在那一天创建 entry，并反向写回原行 ✓DL 标记。当用户提到 #DL、obs-dispatch、
  日记投递、launchd 任务、fswatch、反向写回、✓DL、通知没收到、调试 / 改语法 /
  加日期格式 / 加 Journal 路由 / 重新部署到新 Mac 等相关问题时使用此 skill。
  关键触发词：#DL, obs-dispatch, obsidian 投递, 日记投递, fswatch 不工作,
  launchd 不工作, ✓DL 没出现, 重装 obs-dispatch.
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
---

# obs-dispatch：Obsidian → Day One 实时投递

把 Obsidian 笔记里的 `#DL` 标记任务，**实时**（< 5 秒）投递到 Day One 那一天的 entry，并反向写回 ✓DL 标记防重投。

**重要前提**：这是用户「易开军」机器上**已部署、已上线**的系统（首次部署日期 2026-05-05）。这里的 SKILL 是它的运维 + 扩展 + 故障恢复指南，不是从零设计文档。

## 用户语法 cheatsheet

任何笔记里写：

```
<日期> <内容> #DL
```

支持的日期：

| 格式 | 说明 |
|---|---|
| `5/8` | M/D，本年；过去日期 >90 天会视为明年 |
| `2026-05-08` | ISO 完整 |
| `今天` / `today` | 0 天 |
| `明天` / `tomorrow` / `后天` | +1/+2 |
| `+N` | N 天后 |
| `5/8 14:00` 或 `5/8 14:00-16:00` | 时间作为正文一部分（Day One 不调度时间，只是文本） |

**约束**：日期**必须在内容最前面**（去掉 `- [ ]` / 列表标记后），否则不识别——这是为避免歧义有意设计。

成功投递后原行尾会出现 `✓DL 5/8`。看到这个标记就是已投递。

## 文件清单（部署在用户 Mac 上）

| 文件 | 作用 |
|---|---|
| `~/.local/bin/obs-dispatch.py` | 解析 + 投递主脚本（80 行 Python） |
| `~/Library/LaunchAgents/com.user.obs-dispatch.plist` | launchd 服务定义 |
| `~/Library/Logs/obs-dispatch.log` | 运行日志 |
| `/opt/homebrew/bin/fswatch` | 文件监听器（brew 装） |
| `/Applications/Day One.app/Contents/MacOS/dayone` | Day One CLI（app 内置，**不要**用 `/usr/local/bin/dayone2`，那个是坏的） |
| Vault: `/Users/zhiquntang/Documents/龙山军团` | 监听目标 |

## 数据流

```
Obsidian 保存 .md
  ↓ fswatch (~50ms)
launchd 触发 obs-dispatch.py <文件路径>
  ↓ 跳过非 .md / 隐藏目录 / 文件不含 #DL
按行扫，找 #DL，跳过有 ✓DL 的
  ↓
解析行首日期 → 调 Day One CLI: dayone --date YYYY-MM-DD --all-day new "<content>"
  ↓
成功 → 原行尾追加 "  ✓DL M/D"，写回文件，触发 macOS 通知
失败 → 不写回，红色通知，日志记错误（下次保存重试）
```

**死循环防护**：写回后 fswatch 会再次触发，但 parser 看到 `✓DL` 标记直接跳过该行。

## 常用排障命令

```bash
# 状态
launchctl list | grep obs-dispatch

# 看日志
tail -f ~/Library/Logs/obs-dispatch.log

# 看 fswatch / xargs 进程
ps aux | grep -E "(fswatch|obs-dispatch)" | grep -v grep

# 暂停服务
launchctl unload ~/Library/LaunchAgents/com.user.obs-dispatch.plist

# 重启服务
launchctl unload ~/Library/LaunchAgents/com.user.obs-dispatch.plist 2>/dev/null
launchctl load ~/Library/LaunchAgents/com.user.obs-dispatch.plist

# 改完脚本无需重启服务（fswatch 每次都 fresh 调用 .py）

# 强制对某行重投：手动删掉行尾的 ✓DL 标记并保存
```

## 常见问题

| 症状 | 排查 |
|---|---|
| 写了 #DL 没反应 | 1) `launchctl list \| grep obs-dispatch` 看是否在跑；2) `tail -20 ~/Library/Logs/obs-dispatch.log` 看有无错误；3) Day One 是否启动并已登录 |
| 通知没弹 | 系统设置 → 通知 → 「脚本编辑器」/「osascript」开启允许通知；勿扰模式关掉 |
| Day One 写入失败 | `/usr/local/bin/dayone2` 框架坏（已知）；脚本必须用 `/Applications/Day One.app/Contents/MacOS/dayone` 这条路径，不要改 |
| ✓DL 标记没出现但 Day One 有 entry | 文件写权限问题 / 文件被 Obsidian 锁定，看日志 |
| 同一行被重复投递 | 检查反向写回是否成功（应该有 ✓DL）；fswatch 在 macOS 偶尔多次触发，但 parser 看到 ✓DL 会跳过 |
| 月日识别成上一年 | M/D 格式且日期早于今天 90+ 天 → 视为下一年；要确切某年用 ISO 完整格式 |
| 笔记里写 `#DL 是什么` 这种（非任务）被误识 | 不会，parser 要求行首有有效日期，纯文字提到 #DL 不会触发 |

## 扩展指南

### 加新日期格式

编辑 `~/.local/bin/obs-dispatch.py`，在 `DATE_PATTERNS` 列表里加正则 + 在 `parse_date_prefix` 里加分支。例如要加「下周一」：

```python
# 在 DATE_PATTERNS 加
(re.compile(r'^下周([一二三四五六日])\s+'), 'next_weekday'),

# 在 parse_date_prefix 加分支处理 next_weekday
```

无需重启服务。

### 加 Journal 路由

当前是**默认 Journal**（用户在 Day One 里切换默认 Journal 即可换目标）。

如果要按标签路由（比如 `#DL/工作` → 工作 Journal，`#DL/个人` → 个人 Journal）：

1. 在 `parse_line` 里加正则匹配 `#DL/<journal>`
2. 在 `write_dayone` 里加 `--journal "<name>"` 参数

### 加回 Calendar 投递

当前用户决定**砍掉了 Calendar**，只用 Day One。如果未来要加回：

1. 增加 `#CAL` tag 识别
2. `write_calendar` 函数：调 osascript：
   ```bash
   osascript -e 'tell application "Calendar" to tell calendar "工作" to make new event with properties {summary:"...", start date: date "...", end date: date "..."}'
   ```
3. 注意时间格式（中文 macOS 用本地化日期字符串）

### 加 iPhone Quick Capture

iPhone Obsidian 写笔记后，iCloud 同步到 Mac，Mac 上 fswatch 会触发处理 → 自动可用。前提：Mac 在线、iCloud Drive 开启 Obsidian 同步。

如果要 iPhone 端**不依赖 Mac** 直接投递（Mac 离线也能用）：需要在 iPhone 上跑捷径 / Pushcut / iOS Shortcuts，调用 Day One URL Scheme。架构变化大，单独立项。

## 从零部署到新 Mac

如果用户换电脑或文件丢了，按下面步骤重装。完整脚本在 `install/` 子目录。

```bash
# 1. 装 fswatch
brew install fswatch

# 2. 确认 Day One 已装并登录（CLI 路径必须存在）
ls -l "/Applications/Day One.app/Contents/MacOS/dayone"

# 3. 拷贝主脚本
mkdir -p ~/.local/bin
cp ~/.claude/skills/obs-dispatch/install/obs-dispatch.py ~/.local/bin/
chmod +x ~/.local/bin/obs-dispatch.py

# 4. 拷贝 launchd plist
mkdir -p ~/Library/LaunchAgents
cp ~/.claude/skills/obs-dispatch/install/com.user.obs-dispatch.plist ~/Library/LaunchAgents/

# 5. 修改 plist 里的 vault 路径（如果不是 /Users/zhiquntang/Documents/龙山军团）
# 修改 .py 里的 VAULT 常量

# 6. 装载
launchctl load ~/Library/LaunchAgents/com.user.obs-dispatch.plist

# 7. 验证
launchctl list | grep obs-dispatch  # 应该有一行
echo "+1 重装测试 #DL" >> "<vault>/03-个人/日记/_test.md"
sleep 5
tail ~/Library/Logs/obs-dispatch.log  # 应该看到 OK
cat "<vault>/03-个人/日记/_test.md"     # 应该看到 ✓DL 标记
```

## 关键设计决策（为什么这么做）

1. **fswatch 而非定时轮询**：用户要求「实时响应」，几秒延迟都不行。fswatch 监听文件系统事件 < 50ms 触发。

2. **#DL 行尾 tag 而非行首 emoji**：用户反馈 emoji 不好输入；tag 形式打字快、Obsidian 也会把 #DL 识别为标签便于反查。

3. **日期必须在最前面**：避免「写报价 5/10 测试」这种文本被误识——歧义比丢失偶尔识别能力更危险。

4. **反向写回 ✓DL**：作为持久化幂等性标志。任何重复触发（Obsidian 的 autosave 多次触发、文件被另一进程改动等）都不会重复投递。

5. **默认 Journal**：用户用 Day One 仪式是「每天一个 entry」，他切换默认 Journal 等于切换工作上下文。脚本不绑死任何 Journal 名。

6. **只 Day One，不 Calendar**：用户选择简化掉了。Day One 的「每天一条 entry，没做完顺延」用法已经覆盖了 Calendar 的提醒功能。

7. **失败不写回 ✓DL**：保证下次保存能重试，避免任务静默丢失。

## 该改 / 不该改

✅ **该改的（直接编辑 .py 即可，无需重启服务）**：
- 加新日期格式
- 调通知文案
- 加 Journal 路由

⚠️ **改前要思考**：
- 修改 ✓DL 标记格式（已有笔记里的旧标记会失效，导致重复投递）
- 改 #DL 标签为别的（同上）
- 改成支持行首日期之外的位置（增大误识风险）

❌ **不要做的**：
- 不要改成定时轮询（违背「实时」核心需求）
- 不要把 dayone CLI 路径换成 `/usr/local/bin/dayone2`（坏的）
- 不要监听 .obsidian/ 目录（会循环 + 噪音）
