# HOMSH Product Video Ad Generator

When the user wants to generate a product video ad from a HOMSH product image. Trigger when user mentions "product video", "generate video ad", "product ad", "图生视频", "产品视频广告", or provides a HOMSH product image for video creation.

## Overview

Automates the end-to-end flow of generating AI video ads from HOMSH product images using Seedance 2.0 on Jimeng (即梦) platform.

## Prerequisites

- User must have a Jimeng account with active membership (basic member 41 RMB/month minimum)
- Chrome browser with CDP enabled
- web-access skill must be loaded for browser automation

## Workflow

### Step 1: Validate Input

- Confirm product image file path exists
- Identify product model from image (D30, D50, etc.)
- Check image format (PNG/JPG/WebP supported)

### Step 2: Open Jimeng Video Generation

```
Navigate to: https://jimeng.jianying.com/ai-tool/video/generate
```

- Verify user is logged in (check for login button visibility)
- If not logged in, ask user to login in Chrome first
- Dismiss any popups (VIP promo, agreement dialogs, profession selection)

### Step 3: Configure Generation Settings

Default settings for HOMSH product ads:
- Model: **Seedance 2.0 Fast VIP**
- Aspect ratio: **16:9** (landscape for social media) or **auto** based on input image
- Duration: **4s** (default) or **10s** for longer ads
- Mode: **First frame reference** (upload product image as first frame)

### Step 4: Generate Prompt

Template for HOMSH product videos:

**Chinese prompt (for Jimeng):**
```
镜头缓缓推进，展示这台{product_name}智能门禁设备的精致外观，屏幕微微亮起，背景为现代化办公大厅，光线柔和，科技感强烈
```

**Variations by scene:**
- Office lobby: 现代化办公大厅，商务人士走过
- Building entrance: 高端写字楼入口，玻璃门旁
- Data center: 数据中心机房入口，蓝色冷光
- School/Hospital: 学校/医院走廊，温暖光线

### Step 5: Submit and Wait

- Upload product image as first frame via file input
- Fill in prompt via textarea
- Click submit button (circular primary button)
- Handle safety confirmation dialogs (click confirm)
- Wait for generation (VIP: ~2 min, Free: 5-10 min)
- Cost: ~44 credits per 4s video

### Step 6: Download Video

- Click on generated video to open detail view
- Click download button for member-quality version
- Or extract video URL from `<video>` element src and download via curl
- Save to `~/Downloads/HOMSH_{model}_ad.mp4`

## HOMSH Product Catalog

| Model | Description | Key Features |
|-------|-------------|-------------|
| D30 | Smart biometric access terminal | Iris/face recognition, keypad, RFID, touchscreen |
| D50 | Advanced iris recognition terminal | Dual iris, anti-spoofing, outdoor rated |
| QE50 | Embedded iris module | OEM integration, compact form factor |

## Prompt Library

See [references/prompt-templates.md](references/prompt-templates.md) for full prompt library.

## Troubleshooting

- **"合规校验失败"**: Retry with simpler prompt, avoid mentioning surveillance/monitoring
- **Generation stuck loading**: Free tier queue is slow, upgrade to member
- **Black/blank video**: Ensure product image is high quality, min 512px on shortest side
- **Agent mode vs Direct mode**: Direct mode (Seedance Agent creation panel at bottom) is more reliable than the Agent chat mode at top
