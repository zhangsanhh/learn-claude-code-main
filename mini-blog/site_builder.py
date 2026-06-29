from pathlib import Path
from markdown_parser import parse_markdown

def get_html_template(title, content):
    """生成html页面模板"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        h1, h2, h3 {{ color: #2c3e50; }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
        }}
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        ul {{ padding-left: 20px; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <nav><a href="index.html">← 返回首页</a></nav>
    {content}
</body>
</html>"""

def build_site(posts_dir, build_dir):
    """构建静态网站"""
    posts_path = Path(posts_dir)
    build_path = Path(build_dir)

    # 清空build目录
    for file in build_path.glob('*.html'):
        file.unlink()

    # 转换所有markdown文件
    for md_file in posts_path.glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # 提取标题
        first_line = md_content.split('\n')[0]
        title = first_line.lstrip('#').strip() if first_line.startswith('#') else md_file.stem

        # 转换为html
        html_content = parse_markdown(md_content)
        full_html = get_html_template(title, html_content)

        # 写入build目录
        output_file = build_path / f"{md_file.stem}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)

    return len(list(posts_path.glob('*.md')))
