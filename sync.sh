#!/bin/bash
# CC_SKILLS 双向同步脚本
# 用法:
#   ~/.claude/CC_SKILLS_repo/sync.sh status    查看本地修改状态
#   ~/.claude/CC_SKILLS_repo/sync.sh pull      从 GitHub 拉取最新
#   ~/.claude/CC_SKILLS_repo/sync.sh push "提交说明"   推送本地修改到 GitHub
#   ~/.claude/CC_SKILLS_repo/sync.sh diff      查看待提交的差异

set -e
REPO=~/.claude/CC_SKILLS_repo
cd "$REPO"

case "${1:-status}" in
  status)
    echo "=== Git 状态 ==="
    git status --short
    echo ""
    echo "=== 与 origin/main 差异 ==="
    git fetch -q origin main
    LOCAL=$(git rev-parse @)
    REMOTE=$(git rev-parse @{u} 2>/dev/null || echo "no-upstream")
    BASE=$(git merge-base @ @{u} 2>/dev/null || echo "no-base")
    if [ "$LOCAL" = "$REMOTE" ]; then
      echo "本地与远程一致"
    elif [ "$LOCAL" = "$BASE" ]; then
      echo "本地落后于远程，建议 pull"
    elif [ "$REMOTE" = "$BASE" ]; then
      echo "本地领先远程，建议 push"
    else
      echo "本地与远程已分叉，需要手动合并"
    fi
    ;;
  pull)
    echo "=== 从 GitHub 拉取最新 skills ==="
    git pull --ff-only origin main
    ;;
  push)
    MSG="${2:-update skills}"
    echo "=== 推送本地修改到 GitHub ==="
    git add -A
    if git diff --cached --quiet; then
      echo "没有需要提交的修改"
      exit 0
    fi
    git commit -m "$MSG"
    git push origin main
    ;;
  diff)
    echo "=== 待提交的差异 ==="
    git status --short
    echo ""
    git diff --stat
    ;;
  *)
    echo "用法: $0 {status|pull|push|diff} [commit-msg]"
    exit 1
    ;;
esac
