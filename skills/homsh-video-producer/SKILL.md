# HOMSH Video Producer — 虹识产品视频制作技能

## Overview

将原始产品素材（展会录像、工厂视频、产品演示）自动化加工为 YouTube/社媒级别的专业产品视频。全流程：素材分析 → 脚本生成 → AI 配音 → 字幕合成 → 场景图 → 过渡效果 → 质检。

## When to Use This Skill

- 收到原始产品视频/展会录像，需要制作 YouTube 产品宣传片
- 需要将旧素材（低分辨率、有水印）翻新为专业视频
- 需要为新产品快速生成多语言版本视频

## Prerequisites

```bash
pip3 install --break-system-packages edge-tts moviepy pydub
brew install ffmpeg
```

## Workflow

### Phase 1: 素材分析

1. **获取视频元数据**
   ```bash
   ffprobe -v quiet -print_format json -show_format -show_streams <input.mp4>
   mdls <input.mp4>  # macOS
   ```

2. **亮度扫描 — 定位黑屏/过渡帧**
   ```python
   from PIL import Image
   # 逐秒提取帧，计算平均亮度
   # avg < 30 = 黑屏（删除）
   # avg < 60 = 暗帧（检查）
   ```

3. **关键帧提取 — 每秒一帧审查**
   ```bash
   for t in $(seq 0 <duration>); do
     ffmpeg -y -ss $t -i input.mp4 -frames:v 1 -q:v 2 frame_${t}s.jpg
   done
   ```

4. **内容区间标注**
   - 标记有效内容区间（OK）
   - 标记黑屏/过渡区间（DELETE）
   - 标记有时间码水印的区间（CROP）

### Phase 2: 素材切割

5. **精确切割 — 避开所有黑屏帧**
   ```bash
   # 去时间码水印：crop 顶部 100px（480p 源）
   ffmpeg -y -ss <start> -to <end> -i input.mp4 \
     -vf "crop=iw:ih-100:0:100,scale=1920:1080:flags=lanczos" \
     -c:v libx264 -crf 18 -an clip.mp4
   ```

6. **去隔行扫描**（如有伪影）
   ```bash
   ffmpeg ... -vf "yadif,crop=...,scale=..." ...
   ```

7. **变速处理**（人流演示段可加速）
   ```bash
   -vf "...,setpts=0.7*PTS"  # 1.4x 加速
   ```

### Phase 3: 脚本 & AI 配音

8. **设计视频结构**
   ```
   引导段（3段，~20s）：痛点 → 设问 → 揭示产品
   产品段（5段，~35s）：介绍 → 演示 → 特写 → 功能 → 特性
   CTA段（1段，~15s）：场景切换 → Logo + 联系方式
   ```

9. **生成 AI 旁白**（edge-tts）
   ```python
   import edge_tts
   # 英文：en-US-GuyNeural（专业男声）
   # 品牌名 HOMSH 写成 "Hongshi" 让 TTS 正确发音
   # rate: "-5%" 到 "+10%" 控制语速
   communicate = edge_tts.Communicate(text, voice, rate=rate)
   await communicate.save(output_path)
   ```

10. **品牌发音规则**
    - HOMSH → 写作 "Hongshi"（中文拼音）
    - 不要逐字母拼读品牌名

### Phase 4: 视频合成

11. **字幕规则**
    - 中文（黄色 #FFD700）在上，英文（白色）在下
    - 字号：英文 28px，中文 24px（不遮挡画面）
    - 描边：stroke_width=2, stroke_color="black"
    - 底部 padding：文字后加 `"\n "` 防止截断
    - 字体：英文 `/Library/Fonts/Arial Bold.ttf`，中文 `/Library/Fonts/Arial Unicode.ttf`
    - 位置：中文 `H - 140`，英文 `H - 90`

12. **场景图（CTA 段）**
    - 从 Pexels 下载免版税场景图（机场/政府/数据中心）
    - Ken Burns 缓推效果：
      ```bash
      ffmpeg -loop 1 -i scene.jpg \
        -vf "scale=2200:-1,crop=1920:1080:'140*t/4.5':0" \
        -t 4.5 -c:v libx264 clip.mp4
      ```
    - CTA 子段与旁白时间码精确同步

13. **Logo 处理**
    - PNG 透明背景 Logo 用 PIL 合成到黑色背景
    - Logo 上移，留出下方文字空间
    ```python
    from PIL import Image
    bg = Image.new('RGB', (1920, 1080), (0, 0, 0))
    logo = Image.open('logo.png').convert('RGBA')
    logo = logo.resize((1100, int(h * ratio)), Image.LANCZOS)
    bg.paste(logo, (x, y - 120), logo)
    ```

14. **过渡效果**
    - 使用 fade-to-black（FadeIn/FadeOut），不用 CrossFade
    - CrossFade 会导致两段字幕重叠
    - 淡入淡出时长：0.4 秒
    ```python
    from moviepy.video.fx import FadeIn, FadeOut
    part.with_effects([FadeIn(0.4), FadeOut(0.4)])
    ```

15. **背景音乐**
    - ffmpeg 合成简单环境音（避免版权）
    - 音量混合：BGM 30%，旁白 100%
    ```python
    bgm.with_effects([MultiplyVolume(0.3)])
    CompositeAudioClip([voice, bgm])
    ```

### Phase 5: 质检

16. **自动化 QA（必须用 Agent 执行）**
    - 每 3-5 秒提取一帧
    - 检查清单：
      - [ ] 无黑屏帧
      - [ ] 无时间码水印
      - [ ] 中文在英文上方
      - [ ] 文字无截断
      - [ ] 联系方式正确（opticsiris.com）
      - [ ] 过渡处无字幕重叠
      - [ ] 无隔行扫描伪影
      - [ ] CTA 声画同步

17. **发现问题 → 修复 → 重新渲染 → 再次 QA**

### Phase 6: 输出

18. **最终渲染参数**
    ```python
    final.write_videofile(
        output, fps=30, codec="libx264",
        audio_codec="aac", bitrate="8000k",
        preset="medium", threads=4
    )
    ```

## HOMSH 品牌规范

| 项目 | 值 |
|------|-----|
| 公司名 | HOMSH Technology / 虹识技术 |
| 网站 | www.opticsiris.com |
| 邮箱 | sales@opticsiris.com |
| Logo | /Users/xunlong/Downloads/logo3.png（RGBA 透明） |
| 品牌色 | 红色（Logo）+ 黑色背景 |
| 发音 | "Hongshi"（不逐字母拼） |

## Common Pitfalls

- 黑屏过渡帧未清理干净 → 用亮度扫描定位
- 时间码水印未去除 → crop 顶部 100px（480p 源）
- 字幕底部截断 → 文字末尾加 `"\n "`
- CrossFade 导致字幕重叠 → 改用 FadeIn/FadeOut
- TTS 逐字母拼读品牌名 → 写成拼音 "Hongshi"
- CTA 声画不同步 → 按旁白时间码分段切割
- BGM 时长不足 → 生成足够长度（视频时长 + 10s）

## Related Skills

- `homsh-youtube-optimizer` — YouTube SEO 优化
- `homsh-social-copywriter` — 社媒文案生成
- `homsh-agents` — HOMSH 全团队智能体体系
