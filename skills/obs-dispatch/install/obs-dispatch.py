#!/opt/miniconda3/bin/python3
"""obs-dispatch: 监听 Obsidian vault, 把 #DL 任务投递到 Day One。

用法: obs-dispatch.py <file1.md> [file2.md ...]
  通常由 fswatch 通过 launchd 调用。
"""

import os
import re
import sys
import subprocess
from datetime import date, timedelta
from pathlib import Path

VAULT = Path("/Users/zhiquntang/Documents/龙山军团")
DAYONE = "/Applications/Day One.app/Contents/MacOS/dayone"
LOG_FILE = Path.home() / "Library/Logs/obs-dispatch.log"

DL_TAG = re.compile(r'#DL\b')
DONE_MARKER = re.compile(r'✓DL\b')

DATE_PATTERNS = [
    (re.compile(r'^(\d{4})-(\d{1,2})-(\d{1,2})(?:\s+\d{1,2}:\d{2}(?::\d{2})?)?\s+'), 'iso'),
    (re.compile(r'^(\d{1,2})/(\d{1,2})(?:\s+\d{1,2}:\d{2}(?:-\d{1,2}:\d{2})?)?\s+'), 'md'),
    (re.compile(r'^\+(\d+)\s+'), 'plus'),
    (re.compile(r'^(今天|明天|后天|today|tomorrow)\s+'), 'word'),
]

WORD_OFFSET = {
    '今天': 0, 'today': 0,
    '明天': 1, 'tomorrow': 1,
    '后天': 2,
}


def log(msg):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open('a', encoding='utf-8') as f:
        from datetime import datetime
        f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}\n")


def parse_date_prefix(text):
    """从 text 头部解析日期。返回 (date, remaining_text) 或 (None, text)。"""
    today = date.today()
    for pat, kind in DATE_PATTERNS:
        m = pat.match(text)
        if not m:
            continue
        rest = text[m.end():].strip()
        try:
            if kind == 'iso':
                y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                return date(y, mo, d), rest
            if kind == 'md':
                mo, d = int(m.group(1)), int(m.group(2))
                target = date(today.year, mo, d)
                # 月日已过去且超过 90 天 → 视为明年
                if (today - target).days > 90:
                    target = date(today.year + 1, mo, d)
                return target, rest
            if kind == 'plus':
                return today + timedelta(days=int(m.group(1))), rest
            if kind == 'word':
                return today + timedelta(days=WORD_OFFSET[m.group(1)]), rest
        except (ValueError, OverflowError):
            return None, text
    return None, text


def parse_line(line):
    """如果行匹配 #DL + 有效日期且未投递过, 返回 (target_date, content)。"""
    if DONE_MARKER.search(line):
        return None
    if not DL_TAG.search(line):
        return None

    stripped = line.strip()
    # 去掉前导 list / checkbox 标记
    stripped = re.sub(r'^(?:[-*+]\s+)?(?:\[[ xX]\]\s+)?', '', stripped)

    dl_idx = stripped.rfind('#DL')
    if dl_idx == -1:
        return None
    content_part = stripped[:dl_idx].rstrip() + ' '  # 加空格便于 pattern 匹配
    target, content = parse_date_prefix(content_part)
    if target is None or not content.strip():
        return None
    return target, content.strip()


def write_dayone(target_date, content):
    """调 Day One CLI 在指定日期建 entry。"""
    cmd = [
        DAYONE,
        "--date", target_date.strftime("%Y-%m-%d"),
        "--all-day",
        "new", content
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return result.returncode == 0, (result.stderr or '').strip()
    except subprocess.TimeoutExpired:
        return False, "timeout"


def notify(title, msg):
    safe_msg = msg.replace('"', "'").replace('\\', '/')
    safe_title = title.replace('"', "'")
    subprocess.run([
        "osascript", "-e",
        f'display notification "{safe_msg}" with title "{safe_title}"'
    ], capture_output=True)


def process_file(path: Path):
    try:
        if not path.exists() or path.suffix != '.md':
            return
        # 跳过 vault 隐藏目录(.obsidian, .trash 等)
        if any(p.startswith('.') for p in path.parts):
            return
        text = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError) as e:
        log(f"read fail {path}: {e}")
        return

    if '#DL' not in text:
        return  # 快速跳过

    lines = text.split('\n')
    changed = False
    for i, line in enumerate(lines):
        result = parse_line(line)
        if result is None:
            continue
        target_date, content = result
        ok, err = write_dayone(target_date, content)
        date_short = f"{target_date.month}/{target_date.day}"
        if ok:
            lines[i] = line + f"  ✓DL {date_short}"
            changed = True
            log(f"OK {path.name}: {date_short} | {content}")
            notify("✓ Day One", f"{date_short}: {content[:60]}")
        else:
            log(f"FAIL {path.name}: {err}")
            notify("⚠️ Day One 失败", err[:100] or "未知错误")

    if changed:
        try:
            path.write_text('\n'.join(lines), encoding='utf-8')
        except OSError as e:
            log(f"write fail {path}: {e}")


def main():
    if len(sys.argv) < 2:
        log("no args")
        return
    for arg in sys.argv[1:]:
        process_file(Path(arg))


if __name__ == "__main__":
    main()
