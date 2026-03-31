#!/usr/bin/env python3
"""
论文自动更新脚本
每天搜索各类别最新论文并更新README
类别: 3D检测, 分割, 深度估计, 跟踪, World Model, 3DGS, VLA
"""

import re
import subprocess
from datetime import datetime

# 搜索关键词配置
CATEGORIES = {
    "3D Detection": [
        "radar 3D detection autonomous driving",
        "4D radar object detection",
        "camera radar fusion 3D detection"
    ],
    "Segmentation": [
        "radar semantic segmentation autonomous driving",
        "BEV segmentation radar",
        "radar freespace detection"
    ],
    "Depth Estimation": [
        "radar depth estimation monocular",
        "radar camera depth fusion"
    ],
    "Tracking": [
        "radar tracking autonomous driving",
        "multi-object tracking radar"
    ],
    "World Models": [
        "world model autonomous driving simulation",
        "video generation driving world model"
    ],
    "3DGS": [
        "3D Gaussian splatting autonomous driving",
        "4D Gaussian splatting scene reconstruction"
    ],
    "VLA": [
        "vision language action autonomous driving",
        "VLA end-to-end driving"
    ]
}

def search_arxiv(query):
    """搜索arXiv论文（使用curl）"""
    try:
        url = f"https://export.arxiv.org/api/query?search_query=all:{query.replace(' ', '+')}&start=0&max_results=5"
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True, text=True, timeout=30
        )
        return result.stdout
    except Exception as e:
        print(f"搜索失败: {e}")
        return ""

def parse_papers(xml_content):
    """解析arXiv XML响应"""
    papers = []
    entries = re.findall(r'<entry>(.*?)</entry>', xml_content, re.DOTALL)
    for entry in entries:
        title = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
        summary = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
        published = re.search(r'<published>(.*?)</published>', entry)
        
        if title:
            papers.append({
                'title': title.group(1).replace('\n', ' ').strip(),
                'summary': summary.group(1).replace('\n', ' ').strip()[:200] if summary else '',
                'year': published.group(1)[:4] if published else '2026'
            })
    return papers[:3]  # 每个类别最多3篇

def main():
    print(f"开始论文搜索... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    all_papers = {}
    
    for category, queries in CATEGORIES.items():
        print(f"\n搜索类别: {category}")
        category_papers = []
        
        for query in queries:
            print(f"  查询: {query}")
            results = search_arxiv(query)
            papers = parse_papers(results)
            category_papers.extend(papers)
        
        # 去重并取前3篇
        seen = set()
        unique_papers = []
        for p in category_papers:
            if p['title'][:50] not in seen:
                seen.add(p['title'][:50])
                unique_papers.append(p)
        
        all_papers[category] = unique_papers[:3]
        print(f"  找到 {len(all_papers[category])} 篇论文")
    
    print("\n搜索完成!")
    return all_papers

if __name__ == "__main__":
    main()