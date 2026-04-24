#!/usr/bin/env python3
"""
小红书笔记读取工具（Playwright + Cookie方案）
用法：python3 read_xhs.py <小红书URL或关键词>
"""
import sys, json, os, asyncio
from playwright.async_api import async_playwright

COOKIE_FILE = os.path.expanduser("~/.agent-reach/xhs_cookies.json")

async def read_xhs(url_or_query: str):
    if not os.path.exists(COOKIE_FILE):
        print("❌ 未找到登录Cookie，请先运行登录脚本")
        return

    with open(COOKIE_FILE) as f:
        cookies = json.load(f)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        await context.add_cookies(cookies)
        page = await context.new_page()

        # 判断是URL还是搜索词
        if url_or_query.startswith("http"):
            await page.goto(url_or_query, wait_until="domcontentloaded", timeout=15000)
        else:
            search_url = f"https://www.xiaohongshu.com/search_result?keyword={url_or_query}&source=web_search_result_notes"
            await page.goto(search_url, wait_until="domcontentloaded", timeout=15000)

        await page.wait_for_timeout(3000)

        # 提取内容
        title = await page.title()
        # 尝试提取笔记正文
        content = ""
        try:
            # 笔记详情页
            desc = await page.query_selector("#detail-desc, .desc, [class*='desc']")
            if desc:
                content = await desc.inner_text()
            # 搜索结果页
            if not content:
                items = await page.query_selector_all("section.note-item, [class*='note-item']")
                for item in items[:5]:
                    text = await item.inner_text()
                    content += text + "\n---\n"
        except Exception:
            pass

        if not content:
            content = await page.inner_text("body")
            content = content[:2000]

        await browser.close()
        print(f"📕 标题：{title}")
        print(f"\n📝 内容：\n{content[:1500]}")

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "虹膜识别"
    asyncio.run(read_xhs(query))
