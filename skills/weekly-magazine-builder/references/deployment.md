# Deployment

Two strong defaults based on audience.

## For China audiences: Tencent COS + custom domain + CDN

Tested workflow used for 《识界》deployment. Result: `https://weekly.publisher.cn/` serving from a COS bucket with sub-second response times.

### One-time setup

1. **Tencent Cloud account** + real-name verification
2. **COS bucket** — create with name `publisher-weekly-NUMBER` (e.g., `homsh-weekly-1403305689`), region typically `ap-guangzhou` or `ap-shanghai`, permission "public-read / private-write"
3. **Static website hosting** — bucket settings → enable, set index document to `index.html`, error document to `404.html`
4. **Custom domain** — bucket settings → custom domain, add `weekly.publisher.cn`, requires the parent domain to have ICP filing
5. **HTTPS certificate** — Tencent Cloud SSL → apply free DV cert for the subdomain, install on bucket custom domain
6. **CDN acceleration** — recommended; CDN domain becomes the actual customer-facing endpoint, edge nodes cache static assets

### Credentials

Stored in `.secrets/.env`:

```bash
TENCENT_COS_SECRET_ID=AKID...
TENCENT_COS_SECRET_KEY=...
TENCENT_COS_BUCKET=publisher-weekly-NUMBER
TENCENT_COS_REGION=ap-guangzhou
```

`.gitignore` must exclude `.secrets/`. Permissions on the file: `chmod 600 .secrets/.env`.

### Per-deploy script

The full `tools/deploy.sh` (~150 lines) wraps coscmd. Key concerns:

**Proxy environment cleanup** (the most common failure):
```bash
# At top of deploy.sh, before any coscmd command:
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy ALL_PROXY all_proxy
```

This is non-optional on macOS where users often have ClashX/Surge/V2Ray installed. Stale proxy env vars cause 100% upload failures with `[Errno 61] Connection refused` errors.

**HTTP header fix for HTML files** (also non-optional):

After upload, every `.html` file needs its headers set explicitly, otherwise COS serves them as downloads:

```bash
HTML_HEADER='{"Content-Type":"text/html; charset=utf-8","Content-Disposition":"inline"}'

for html in $(find site -name "*.html" | sed 's|^site||'); do
  coscmd copy -d Replaced -H "$HTML_HEADER" \
    "${TENCENT_COS_BUCKET}.cos.${TENCENT_COS_REGION}.myqcloud.com${html}" \
    "${html}"
done
```

**Exclude originals and macOS junk:**
```bash
find site -type f \
  ! -path '*/_raw/*' \
  ! -name '.DS_Store' \
  ! -name 'Thumbs.db'
```

**Required commands:**
```bash
coscmd config -a "$ID" -s "$KEY" -b "$BUCKET" -r "$REGION"
coscmd upload -rsf site/ /
# Then loop through HTML files for header fix as above
```

**CDN cache flush** (manual step, easy to forget):

After deploy, go to Tencent Cloud Console → CDN → 刷新预热 → 刷新目录, input `https://weekly.publisher.cn/`, submit. Edge nodes refresh in 1-2 minutes; without this step users see cached old version for up to 30 minutes.

Or via Tencent Cloud CLI:
```bash
tccli cdn PurgePathCache --Paths '["https://weekly.publisher.cn/"]' --FlushType flush
```

### Deploy script modes

The full `deploy.sh` should support three modes:
- `deploy` (default) — full upload + header fix
- `dry` — print file list, don't upload
- `backup` — download current production to `.backup/YYYYMMDD-HHMMSS/` for rollback

### Rollback

If a deploy goes badly:

1. If `.backup/` exists from a pre-deploy backup, re-upload from there:
   ```bash
   cd .backup/timestamp/
   coscmd upload -rsf ./ /
   # then re-run header fix
   ```

2. If no backup, check Tencent Cloud Console → COS → bucket → 版本控制 (if enabled, restore from previous version)

3. Worst case: redeploy from local files, which means you lose the old content but get to a working state quickly

## For global audiences: Cloudflare Pages

For magazines targeting non-China readers:

1. Push project to GitHub
2. Connect Cloudflare Pages to the repo
3. Build command: none (static site), output directory: `site/`
4. Domain: weekly.publisher.com or *.pages.dev
5. Each Git push auto-deploys

No HTTP header fix needed — Cloudflare serves correctly by default. CDN is global by default.

## Other static hosts

- **Vercel** — same pattern as Cloudflare Pages, slight different DX
- **Netlify** — same pattern, has form handling if you ever add subscription
- **GitHub Pages / Gitee Pages** — works but slower edge delivery
- **AWS S3 + CloudFront** — works but most operationally heavy

For all of these: skip `coscmd` and use the platform's native deploy. The 10-column structure and HTML templates work identically.

## Domain considerations

**Subdomain strategy**: `weekly.publisher.com` or `weekly.publisher.cn` is the cleanest.

**Path strategy**: `publisher.com/weekly/` works but **all absolute paths in HTML must be rewritten** to be `/weekly/...` instead of `/...`. This is a common source of breakage. If using a sub-path, either rewrite paths consistently OR use `<base href="/weekly/">` and rewrite all absolute paths to relative.

**For initial inaugural deployments**, deploy directly to root of the chosen domain. Don't try to deploy to a `/preview/` subpath — the absolute-path issue makes this brittle.

## Pre-deploy checklist

Before running `deploy.sh`:

- [ ] All HTML files validate (no unclosed tags, no broken anchor links)
- [ ] All image references in HTML correspond to actual files in `site/assets/img/`
- [ ] All CSS and JS files are committed (not just edited locally)
- [ ] All deep articles have their corresponding `articles/SLUG.html` files
- [ ] Cards and stack items in issue index have correct `阅读全文` links
- [ ] Subscribe / contact mailto links have correct email addresses
- [ ] Footer copyright year is current
- [ ] Open Graph metadata on each page has issue-specific description and image

A common pre-deploy check script:
```bash
# Verify all "阅读全文" links point to existing files
grep -r 'card-read-more' site/ -h | grep -oE '/issues/[^"]*\.html' | sort -u | while read href; do
  test -f "site$href" && echo "✓ $href" || echo "✗ MISSING: $href"
done
```

## Post-deploy verification

In a real browser:

1. Open `https://weekly.publisher.cn/`
2. Confirm hero motif animation plays
3. Click into the current issue card
4. Scroll through all 10 columns of the issue
5. Click into one deep article from each column type (Inside Brand, Tech Radar, Industry Watch)
6. Verify breadcrumb navigation works
7. Click sibling articles in deep article footer
8. Test 404 page: visit `https://weekly.publisher.cn/nothing`
9. Click subscribe / contact mailto links — confirm email client opens with pre-filled subject

If any step fails, deploy is not complete.
