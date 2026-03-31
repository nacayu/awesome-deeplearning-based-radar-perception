#!/bin/bash
# 论文自动更新脚本 - 使用web_fetch获取论文详情
# 每天12点执行

REPO_DIR="/home/naca/.openclaw/agents/researcher/workspace/awesome-deeplearning-based-radar-perception"
LOG_FILE="$REPO_DIR/cron_update.log"

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 开始更新 ===" >> "$LOG_FILE"

cd "$REPO_DIR" || exit 1

# 搜索各类别新论文并更新
# 这里的更新逻辑需要人工审核后更新

# 简单方式：git pull检查更新
git fetch origin
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)

if [ "$LOCAL" != "$REMOTE" ]; then
    git pull origin main >> "$LOG_FILE" 2>&1
    echo "$(date '+%Y-%m-%d %H:%M:%S'): 已更新远程变更" >> "$LOG_FILE"
else
    echo "$(date '+%Y-%m-%d %H:%M:%S'): 无新变更" >> "$LOG_FILE"
fi

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 结束 ===" >> "$LOG_FILE"