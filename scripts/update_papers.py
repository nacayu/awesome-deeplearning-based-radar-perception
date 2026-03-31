#!/usr/bin/env python3
"""
论文自动更新脚本 v2.1 - 简化版
每天搜索各类别最新论文，生成摘要总结
"""

import re
import subprocess
from datetime import datetime
import urllib.parse

CATEGORIES = {
    "Detection": "radar 3D detection autonomous driving",
    "Segmentation": "radar semantic segmentation BEV", 
    "Tracking": "radar multi-object tracking autonomous driving",
    "World Models": "world model autonomous driving simulation",
    "3DGS": "3D Gaussian splatting autonomous driving",
    "VLA": "vision language action end-to-end driving"
}

def generate_summary(title, abstract):
    """基于摘要生成中文总结"""
    if not abstract:
        return "待补充"
    
    # 关键词识别
    kw_map = {
        'radar': '雷达', 'mmwave': '毫米波', '4d': '4D',
        'fusion': '融合', 'detection': '检测', 'camera': '相机',
        'transformer': 'Transformer', 'attention': '注意力',
        'gaussian': '3DGS', 'splatting': '高斯',
        'language': '语言', 'action': '动作', 'vlm': 'VLM',
        'bev': 'BEV', 'depth': '深度', 'tracking': '跟踪'
    }
    
    keywords = []
    lower_abs = abstract.lower()
    for k, v in kw_map.items():
        if k in lower_abs:
            keywords.append(v)
    
    kw_str = " | ".join(set(keywords)) if keywords else "自动驾驶"
    return f"[{kw_str}] {abstract[:100]}..."

def search_arxiv(query):
    """搜索arXiv论文"""
    try:
        url = f"https://export.arxiv.org/api/query?search_query=all:{query.replace(' ', '+')}&start=0&max_results=5"
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True, text=True, timeout=20
        )
        return result.stdout
    except Exception as e:
        print(f"Error: {e}")
        return ""

def parse_papers(xml):
    """解析arXiv XML"""
    papers = []
    for entry in re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL):
        title = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
        summary = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
        published = re.search(r'<published>(.*?)</published>', entry)
        arxiv_id = re.search(r'<id>http://arxiv.org/abs/(.*?)</id>', entry)
        
        if title:
            t = title.group(1).replace('\n', ' ').strip()
            a = summary.group(1).replace('\n', ' ').strip() if summary else ""
            papers.append({
                'title': t,
                'abstract': a,
                'year': published.group(1)[:4] if published else '2026',
                'arxiv_id': arxiv_id.group(1) if arxiv_id else '',
                'summary': generate_summary(t, a)
            })
    return papers

def main():
    print(f"=== 论文搜索 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
    
    results = {}
    for cat, query in CATEGORIES.items():
        print(f"正在搜索: {cat}")
        xml = search_arxiv(query)
        papers = parse_papers(xml)[:3]  # 每类3篇
        
        print(f"  找到 {len(papers)} 篇")
        
        # 打印新论文
        for p in papers:
            print(f"  - {p['year']} {p['title'][:50]}...")
            print(f"    摘要: {p['summary'][:60]}...")
        
        results[cat] = papers
    
    print("\n=== 完成 ===")
    return results

if __name__ == "__main__":
    main()