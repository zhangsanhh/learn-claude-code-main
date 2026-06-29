import re

def convert_links(text):
    """转换markdown链接为html链接"""
    return re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)

def parse_markdown(text):
    """将markdown文本转换为html"""
    lines = text.split('\n')
    html = []
    in_code_block = False
    in_list = False
    code_lang = ''

    for line in lines:
        # 代码块
        if line.startswith('```'):
            if in_code_block:
                html.append('</code></pre>')
                in_code_block = False
            else:
                code_lang = line[3:].strip()
                html.append(f'<pre><code class="{code_lang}">')
                in_code_block = True
            continue

        if in_code_block:
            html.append(line)
            continue

        # 标题
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            content = line.lstrip('#').strip()
            html.append(f'<h{level}>{content}</h{level}>')
            continue

        # 无序列表
        if line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html.append('<ul>')
                in_list = True
            content = line[2:].strip()
            content = convert_links(content)
            html.append(f'<li>{content}</li>')
            continue

        # 列表结束
        if in_list and line.strip() == '':
            html.append('</ul>')
            in_list = False
            html.append('<p></p>')
            continue

        # 空行
        if line.strip() == '':
            html.append('<p></p>')
            continue

        # 普通段落
        html.append(f'<p>{line}</p>')

    # 关闭未闭合的标签
    if in_list:
        html.append('</ul>')
    if in_code_block:
        html.append('</code></pre>')

    return '\n'.join(html)
