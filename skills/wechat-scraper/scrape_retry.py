#!/usr/bin/env python3
"""
微信公众号文章下载 - 重试版
增加超时时间，重试失败文章
"""

import asyncio
import os
import re
from playwright.async_api import async_playwright

ACCOUNT_NAME = "AI驱动FPGA"
OUTPUT_DIR = os.path.expanduser("~/Desktop/学习/程序设计/wechat-scraper/articles")
MAX_PAGES = 10  # 增加页数
TIMEOUT = 60000  # 60秒超时
DELAY = 2


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/*?:"<>|\n\r]', '', name)
    return name[:80].strip()


def html_to_markdown(html_content: str, title: str) -> str:
    text = html_content
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<img[^>]*data-src=["\']([^"\']*)["\'][^>]*/?>', r'\n![image](\1)\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*/?>', r'\n![image](\1)\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    text = re.sub(r'\n{3,}', '\n\n', text)
    return f"# {title}\n\n{text.strip()}"


async def download_article(context, search_page, article, index, total):
    """下载单篇文章，带重试"""
    print(f"\n[{index}/{total}] {article['title'][:50]}...")

    for attempt in range(3):  # 最多重试3次
        try:
            # 回到搜索页
            url = f"https://weixin.sogou.com/weixin?type=2&query={ACCOUNT_NAME}&page={article['page']}"
            await search_page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(DELAY)

            # 检查验证码
            if "antispider" in search_page.url:
                print(f"   ⚠️ 验证码，请手动完成...")
                await search_page.wait_for_url("**/weixin?**", timeout=180000)
                await asyncio.sleep(2)

            # 找到文章链接
            links = await search_page.query_selector_all('li[id^="sogou_vr_"] h3 a')
            if article['idx'] >= len(links):
                print(f"   ⚠️ 找不到链接 (attempt {attempt+1})")
                continue

            # 新标签页打开
            async with context.expect_page(timeout=TIMEOUT) as new_page_info:
                await links[article['idx']].click(modifiers=["Meta"])

            page = await new_page_info.value

            # 等待加载
            try:
                await page.wait_for_load_state("networkidle", timeout=TIMEOUT)
            except:
                pass

            await asyncio.sleep(3)

            # 等待内容
            try:
                await page.wait_for_selector("#js_content", timeout=30000)
            except:
                print(f"   ⚠️ 内容未加载 (attempt {attempt+1})")
                await page.close()
                continue

            # 获取标题
            title_elem = await page.query_selector("#activity-name")
            title = await title_elem.inner_text() if title_elem else article['title']
            title = title.strip()

            # 获取内容
            content_elem = await page.query_selector("#js_content")
            content_html = await content_elem.inner_html() if content_elem else ""

            if len(content_html) < 100:
                print(f"   ⚠️ 内容太短 (attempt {attempt+1})")
                await page.close()
                continue

            # 获取完整HTML
            full_html = await page.content()

            # 保存
            filename = f"{index:03d}_{sanitize_filename(title)}"

            html_path = os.path.join(OUTPUT_DIR, "html", f"{filename}.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(full_html)

            md_content = html_to_markdown(content_html, title)
            md_path = os.path.join(OUTPUT_DIR, "markdown", f"{filename}.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_content)

            print(f"   ✅ 已保存 ({len(content_html)} 字符)")
            await page.close()
            return True

        except Exception as e:
            print(f"   ❌ 失败 (attempt {attempt+1}): {str(e)[:40]}")
            # 关闭可能打开的页面
            pages = context.pages
            if len(pages) > 1:
                await pages[-1].close()
            await asyncio.sleep(2)

    return False


async def main():
    print("=" * 60)
    print(f"🔍 微信公众号文章下载 (重试版)")
    print(f"📌 目标: {ACCOUNT_NAME}")
    print(f"⏱️ 超时: {TIMEOUT/1000}秒")
    print("=" * 60)

    os.makedirs(os.path.join(OUTPUT_DIR, "html"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "markdown"), exist_ok=True)

    # 获取已下载的文件
    existing = set()
    for f in os.listdir(os.path.join(OUTPUT_DIR, "markdown")):
        if f.endswith(".md"):
            existing.add(f[4:-3])  # 去掉序号和扩展名

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )

        search_page = await context.new_page()
        all_articles = []

        # 收集文章
        for page_num in range(1, MAX_PAGES + 1):
            url = f"https://weixin.sogou.com/weixin?type=2&query={ACCOUNT_NAME}&page={page_num}"
            print(f"\n📄 第 {page_num} 页...")

            await search_page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(DELAY)

            if "antispider" in search_page.url:
                print("⚠️ 验证码，请手动完成...")
                await search_page.wait_for_url("**/weixin?**", timeout=180000)

            articles = await search_page.query_selector_all('li[id^="sogou_vr_"] h3 a')
            if not articles:
                print("   没有更多")
                break

            for idx, link in enumerate(articles):
                try:
                    title = (await link.inner_text()).strip()
                    all_articles.append({"title": title, "page": page_num, "idx": idx})

                    # 检查是否已下载
                    clean_title = sanitize_filename(title)
                    status = "✓" if clean_title in existing else "○"
                    print(f"   {status} {title[:50]}...")
                except:
                    continue

        # 去重
        seen = set()
        unique = []
        for a in all_articles:
            if a['title'] not in seen:
                seen.add(a['title'])
                unique.append(a)

        # 过滤已下载
        to_download = []
        for a in unique:
            clean_title = sanitize_filename(a['title'])
            if clean_title not in existing:
                to_download.append(a)

        print(f"\n✅ 共 {len(unique)} 篇，待下载 {len(to_download)} 篇")

        if not to_download:
            print("所有文章已下载！")
            await browser.close()
            return

        # 下载
        print("\n📥 开始下载...")
        success = 0

        for i, article in enumerate(to_download, 1):
            # 使用原始序号
            orig_idx = unique.index(article) + 1
            if await download_article(context, search_page, article, orig_idx, len(unique)):
                success += 1
            await asyncio.sleep(DELAY)

        print("\n" + "=" * 60)
        print(f"🎉 完成! 本次成功: {success}/{len(to_download)}")
        total_files = len(os.listdir(os.path.join(OUTPUT_DIR, "markdown")))
        print(f"   总计已下载: {total_files} 篇")
        print("=" * 60)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
