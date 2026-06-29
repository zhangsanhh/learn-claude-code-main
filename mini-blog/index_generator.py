import os
from pathlib import Path

def generate_index(posts_dir):
    """扫描posts目录，生成文章列表"""
    posts = []

    for file in Path(posts_dir).glob('*.md'):
        with open(file, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # 提取第一行作为标题
            title = first_line.lstrip('#').strip() if first_line.startswith('#') else file.stem

        posts.append({
            'title': title,
            'filename': file.stem,
            'path': file.name
        })

    # 按文件名排序
    posts.sort(key=lambda x: x['filename'])

    # 生成index.md内容
    index_content = ['# 文章列表\n']
    for post in posts:
        index_content.append(f'- [{post["title"]}]({post["filename"]}.html)')

    return '\n'.join(index_content)
