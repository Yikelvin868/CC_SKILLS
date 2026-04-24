# DayOne 日记写入技能

## 使用方法

通过 URL scheme 写入 DayOne 日记。

### 写入日记

```bash
# 1. 将内容 URL 编码
CONTENT="你的日记内容"
ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$CONTENT'''))")

# 2. 打开 DayOne 并创建条目
open "dayone://post?entry=$ENCODED"
```

### 完整示例

```bash
dayone_write() {
    local content="$1"
    local encoded=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.stdin.read()))" <<< "$content")
    open "dayone://post?entry=$encoded"
}

# 使用
dayone_write "## 标题

这是内容

#标签1 #标签2"
```

### 注意事项

- DayOne 会打开并显示新条目预览
- 用户需要点击"保存"确认
- 支持 Markdown 格式
- 支持 #标签
