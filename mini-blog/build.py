#!/usr/bin/env python3
from pathlib import Path
from index_generator import generate_index
from site_builder import build_site
from markdown_parser import parse_markdown

def main():
    """主程序入口"""
    base_dir = Path(__file__).parent
    posts_dir = base_dir / 'posts'
    build_dir = base_dir / 'build'

    print("🚀 开始构建博客...")

    # 生成文章列表
    print("📝 生成文章列表...")
    index_md = generate_index(posts_dir)
    index_file = posts_dir / 'index.md'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_md)

    # 构建静态网站
    print("🔨 转换markdown为html...")
    count = build_site(posts_dir, build_dir)

    print(f"✅ 构建完成！共生成 {count} 个页面")
    print(f"📂 输出目录: {build_dir}")
    print(f"💡 运行 'python -m http.server 8000 -d build' 预览网站")

if __name__ == '__main__':
    main()
