#!/bin/bash
# 论文自动更新定时脚本
# 每天12点执行

REPO_DIR="/home/naca/.openclaw/agents/researcher/workspace/awesome-deeplearning-based-radar-perception"
LOG_FILE="/home/naca/.openclaw/agents/researcher/workspace/awesome-deeplearning-based-radar-perception/cron_update.log"

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 开始更新 ===" >> "$LOG_FILE"

cd "$REPO_DIR" || exit 1

# 搜索新论文并更新（调用Python脚本）
python3 scripts/update_papers.py >> "$LOG_FILE" 2>&1

# 检查是否有新内容需要提交
if git diff --quiet; then
    echo "$(date '+%Y-%m-%d %H:%M:%S'): 无新论文" >> "$LOG_FILE"
else
    git add -A
    git commit -m "daily: 更新论文 $(date '+%Y-%m-%d')" >> "$LOG_FILE" 2>&1
    git push origin main >> "$LOG_FILE" 2>&1
    echo "$(date '+%Y-%m-%d %H:%M:%S'): 更新完成并推送" >> "$LOG_FILE"
fi

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 结束 ===" >> "$LOG_FILE"