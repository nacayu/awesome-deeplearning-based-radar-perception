#!/bin/bash
# 定时任务脚本：每天中午12点更新论文列表
# 使用: 0 12 * * * /path/to/update_papers.sh

REPO_DIR="/home/naca/.openclaw/agents/researcher/workspace/awesome-deeplearning-based-radar-perception"
cd "$REPO" || exit 1

echo "开始更新论文列表..."

# 记录更新日志
echo "$(date '+%Y-%m-%d %H:%M:%S'): 开始更新" >> update.log

# 更新README
# 此脚本需要外部调用arXiv搜索并更新README

# 提交更改
git add -A
git commit -m "daily: 更新论文列表 $(date '+%Y-%m-%d')" 2>/dev/null

# 推送到GitHub
git push origin main 2>/dev/null

echo "$(date '+%Y-%m-%d %H:%M:%S'): 更新完成" >> update.log