# HOMSH Brand Overlay

When the user wants to add HOMSH branding to a video, cover AI watermarks, or brand product videos. Trigger when user mentions "add logo", "brand video", "cover watermark", "去水印", "加Logo", "品牌标识", or needs to overlay HOMSH logo on video content.

## Overview

Overlays the HOMSH logo on video content with a clean white background, primarily to cover AI-generation watermarks and establish brand identity. Uses ffmpeg + Python PIL for high-quality rendering.

## Prerequisites

- ffmpeg installed (`brew install ffmpeg`)
- Python 3 with PIL/Pillow (`pip install Pillow numpy`)
- HOMSH logo file

## Brand Assets

| Asset | Path | Size |
|-------|------|------|
| Logo (full, with text) | `~/Library/Mobile Documents/com~apple~CloudDocs/Desktop/企业-虹识技术/公司/LOGO和口号/logo3.png` | 2451x884 |

## Workflow

### Step 1: Prepare Transparent Logo

Remove white background from the original logo PNG:

```python
from PIL import Image
import numpy as np

img = Image.open("logo3.png").convert("RGBA")
data = np.array(img)
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
white_mask = (r > 240) & (g > 240) & (b > 240)
data[white_mask] = [0, 0, 0, 0]
result = Image.fromarray(data)
result.save("/tmp/homsh_logo_transparent.png")
```

### Step 2: Render HD Logo with White Background

Render at 2x target size then scale down for sharpness:

```python
from PIL import Image

logo = Image.open("/tmp/homsh_logo_transparent.png").convert("RGBA")
target_w = 520  # 2x final size (260px on video)
ratio = target_w / logo.width
target_h = int(logo.height * ratio)
logo_resized = logo.resize((target_w, target_h), Image.LANCZOS)

padding = 20
canvas = Image.new("RGBA", (target_w + padding*2, target_h + padding*2), (255, 255, 255, 255))
canvas.paste(logo_resized, (padding, padding), logo_resized)
canvas.save("/tmp/homsh_logo_hd.png")
```

### Step 3: Overlay on Video

```bash
ffmpeg -y \
  -i input_video.mp4 \
  -i /tmp/homsh_logo_hd.png \
  -filter_complex "[1:v]scale=280:-1:flags=lanczos[logo];[0:v][logo]overlay=0:0" \
  -c:v libx264 -crf 18 -preset slow \
  -c:a copy \
  output_video.mp4
```

## Position Options

| Position | overlay value | Use Case |
|----------|---------------|----------|
| Top-left (default) | `overlay=0:0` | Cover AI watermark |
| Top-right | `overlay=W-w:0` | Alternative branding |
| Bottom-left | `overlay=0:H-h` | Subtle branding |
| Bottom-right | `overlay=W-w:H-h` | Standard logo placement |
| Center | `overlay=(W-w)/2:(H-h)/2` | Intro/outro frame |

## Quality Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| `-crf` | 18 | High quality (lower = better, 0-51 range) |
| `-preset` | slow | Better compression, slower encoding |
| `flags=lanczos` | Logo scaling | Best quality downscaling algorithm |
| Logo render at 2x | 520px wide | Prevents downscale blur |

## Common Issues

- **Logo appears blurry**: Render logo at 2x target size in Python first, then let ffmpeg scale down
- **White background too large**: Adjust padding value in Step 2
- **Logo too small/large**: Adjust `scale=280` value in ffmpeg filter (280 is good for ~834px wide video)
