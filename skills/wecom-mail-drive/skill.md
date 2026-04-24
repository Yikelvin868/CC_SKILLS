# 企业微信邮箱和微盘 Skill

访问企业微信邮箱和微盘功能。

## 触发条件

当用户提到以下内容时使用此Skill：
- 企业微信邮箱、企微邮箱、发邮件
- 企业微信微盘、企微微盘、上传文件到微盘、下载微盘文件
- WeCom email、WeDrive

## 配置

需要设置环境变量：
```bash
export WECOM_CORP_ID="ww4d3e18a99c2d9b61"
export WECOM_WEDRIVE_SECRET="你的微盘Secret"  # 在企业微信后台获取
```

**获取微盘Secret：**
1. 登录企业微信管理后台
2. 应用管理 → 微盘
3. 查看Secret并复制

## 微盘API接口

### 获取Access Token

```bash
curl "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=${WECOM_CORP_ID}&corpsecret=${WECOM_WEDRIVE_SECRET}"
```

### 获取空间信息

```bash
curl -X POST "https://qyapi.weixin.qq.com/cgi-bin/wedrive/space_info?access_token=${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"userid": "用户ID"}'
```

### 上传文件

```bash
curl -X POST "https://qyapi.weixin.qq.com/cgi-bin/wedrive/file_upload?access_token=${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "spaceid": "空间ID",
    "fatherid": "父文件夹ID",
    "file_name": "文件名.txt",
    "file_base64_content": "BASE64编码的文件内容"
  }'
```

### 下载文件

```bash
curl -X POST "https://qyapi.weixin.qq.com/cgi-bin/wedrive/file_download?access_token=${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"fileid": "文件ID"}'
```

返回下载链接，需要带cookie访问。

### 获取文件列表

```bash
curl -X POST "https://qyapi.weixin.qq.com/cgi-bin/wedrive/file_list?access_token=${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "spaceid": "空间ID",
    "fatherid": "父文件夹ID",
    "sort_type": 1,
    "start": 0,
    "limit": 100
  }'
```

## 使用Python客户端

```python
import os
import sys
sys.path.insert(0, os.path.expanduser("~/.claude/skills/wecom-mail-drive"))
from wecom_client import WeComWeDrive

# 初始化客户端
client = WeComWeDrive()

# 获取空间列表
spaces = client.get_space_list()

# 获取文件列表
files = client.list_files(space_id="xxx", folder_id="xxx")

# 上传文件
result = client.upload_file(
    space_id="xxx",
    folder_id="xxx",
    file_path="/path/to/file.txt"
)

# 下载文件
client.download_file(file_id="xxx", save_path="/path/to/save.txt")
```

## 注意事项

1. **IP白名单**：API调用需要将服务器IP加入企业微信白名单
2. **微盘Secret**：必须使用微盘专用Secret，不是自建应用的Secret
3. **文件限制**：微盘API不支持下载微文档和微表格，仅支持普通文件
4. **下载链接**：下载链接有效期2小时，需带cookie访问

## 相关文档

- [企业微信开发者中心](https://developer.work.weixin.qq.com/)
- [微盘文件上传](https://developer.work.weixin.qq.com/document/path/97914)
- [微盘文件下载](https://developer.work.weixin.qq.com/document/path/98021)
- [文件分块上传](https://developer.work.weixin.qq.com/document/path/98004)
