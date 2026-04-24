---
name: wechat-scraper
description: 批量下载微信公众号文章为 HTML 和 Markdown 格式。当用户要求下载、导出、备份微信公众号文章时自动触发。
---

# WeChat Public Account Article Scraper

批量下载微信公众号文章，保存为 HTML 和 Markdown 格式。

## 触发条件

当用户提到以下关键词时使用此技能：
- 下载公众号文章
- 导出微信文章
- 备份公众号
- 批量下载微信

## 使用方式

用户调用: `/wechat-scraper <公众号名称> [输出目录]`

示例:
- `/wechat-scraper AI驱动FPGA`
- `/wechat-scraper 虹识科技 ~/Documents/articles`

## 执行流程

### Step 1: 检查依赖

```bash
python3 -c "import playwright" 2>/dev/null || pip3 install playwright
playwright install chromium 2>/dev/null || true
```

### Step 2: 解析参数

从用户输入中提取:
- `ACCOUNT_NAME`: 公众号名称 (必填)
- `OUTPUT_DIR`: 输出目录 (可选，默认 `~/Desktop/wechat-articles/<公众号名称>`)
- `MAX_PAGES`: 搜索页数 (可选，默认 10)

### Step 3: 生成并运行脚本

在用户指定的输出目录创建并运行下载脚本。脚本模板如下:

```python
#!/usr/bin/env python3
"""微信公众号文章批量下载器"""

import asyncio
import os
import re
from playwright.async_api import async_playwright

ACCOUNT_NAME = "{ACCOUNT_NAME}"
OUTPUT_DIR = "{OUTPUT_DIR}"
MAX_PAGES = {MAX_PAGES}
TIMEOUT = 60000
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
    print(f"\n[{index}/{total}] {article['title'][:50]}...")

    for attempt in range(3):
        try:
            url = f"https://weixin.sogou.com/weixin?type=2&query={ACCOUNT_NAME}&page={article['page']}"
            await search_page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(DELAY)

            if "antispider" in search_page.url:
                print(f"   ⚠️ 验证码，请手动完成...")
                await search_page.wait_for_url("**/weixin?**", timeout=180000)
                await asyncio.sleep(2)

            links = await search_page.query_selector_all('li[id^="sogou_vr_"] h3 a')
            if article['idx'] >= len(links):
                print(f"   ⚠️ 找不到链接 (attempt {attempt+1})")
                continue

            async with context.expect_page(timeout=TIMEOUT) as new_page_info:
                await links[article['idx']].click(modifiers=["Meta"])

            page = await new_page_info.value

            try:
                await page.wait_for_load_state("networkidle", timeout=TIMEOUT)
            except:
                pass

            await asyncio.sleep(3)

            try:
                await page.wait_for_selector("#js_content", timeout=30000)
            except:
                print(f"   ⚠️ 内容未加载 (attempt {attempt+1})")
                await page.close()
                continue

            title_elem = await page.query_selector("#activity-name")
            title = await title_elem.inner_text() if title_elem else article['title']
            title = title.strip()

            content_elem = await page.query_selector("#js_content")
            content_html = await content_elem.inner_html() if content_elem else ""

            if len(content_html) < 100:
                print(f"   ⚠️ 内容太短 (attempt {attempt+1})")
                await page.close()
                continue

            full_html = await page.content()
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
            pages = context.pages
            if len(pages) > 1:
                await pages[-1].close()
            await asyncio.sleep(2)

    return False


async def main():
    print("=" * 60)
    print(f"🔍 微信公众号文章下载器")
    print(f"📌 目标: {ACCOUNT_NAME}")
    print(f"📁 输出: {OUTPUT_DIR}")
    print(f"⏱️ 超时: {TIMEOUT/1000}秒")
    print("=" * 60)

    os.makedirs(os.path.join(OUTPUT_DIR, "html"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "markdown"), exist_ok=True)

    existing = set()
    md_dir = os.path.join(OUTPUT_DIR, "markdown")
    if os.path.exists(md_dir):
        for f in os.listdir(md_dir):
            if f.endswith(".md"):
                existing.add(f[4:-3])

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )

        search_page = await context.new_page()
        all_articles = []

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
                    clean_title = sanitize_filename(title)
                    status = "✓" if clean_title in existing else "○"
                    print(f"   {status} {title[:50]}...")
                except:
                    continue

        seen = set()
        unique = []
        for a in all_articles:
            if a['title'] not in seen:
                seen.add(a['title'])
                unique.append(a)

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

        print("\n📥 开始下载...")
        success = 0

        for i, article in enumerate(to_download, 1):
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
```

### Step 4: 执行下载

1. 将脚本写入临时文件
2. 运行脚本: `python3 /tmp/wechat_scraper.py`
3. 脚本会打开浏览器窗口
4. 如遇验证码，提示用户手动完成
5. 等待下载完成

### Step 5: 报告结果

下载完成后:
1. 统计下载数量
2. 打开输出目录
3. 显示示例文件列表

## 技术要点

### 搜狗微信搜索反爬机制
直接访问 URL 会被拦截，必须使用 Cmd+Click 在新标签页打开:
```python
async with context.expect_page(timeout=TIMEOUT) as new_page_info:
    await links[article['idx']].click(modifiers=["Meta"])
```

### 内容检测
微信文章内容在 `#js_content` 元素中，需验证内容长度 > 100 字符。

### 增量下载
检查已下载文件，跳过重复下载。

## 输出格式

```
{OUTPUT_DIR}/
├── html/
│   ├── 001_文章标题.html
│   └── ...
└── markdown/
    ├── 001_文章标题.md
    └── ...
```

## 注意事项

1. 需要手动完成验证码（脚本会等待 180 秒）
2. 部分文章可能因删除或超时下载失败
3. 重新运行会自动跳过已下载的文章
4. 建议每次下载间隔 2-3 秒避免触发反爬
