---
name: email-access
description: 访问虹识技术企业邮箱 kaijun.yi@homsh.cn，支持搜索、读取、导出邮件、下载员工周报附件。当用户要求查看邮件、搜索邮件、导出邮件、下载周报时自动触发。
---

# 虹识技术企业邮箱访问

通过 IMAP 协议访问 kaijun.yi@homsh.cn 企业邮箱。

## 触发条件

当用户提到以下关键词时使用此技能：
- 查看邮件
- 搜索邮件
- 导出邮件
- 读取收件箱
- 邮箱
- 下载周报
- 员工周报
- 绩效评估

## 邮箱配置

```python
EMAIL = "kaijun.yi@homsh.cn"
AUTH_CODE = "iSuCYRzJE3xc3ei3"  # 客户端专用密码（授权码）
IMAP_SERVER = "imap.exmail.qq.com"
IMAP_PORT = 993
SMTP_SERVER = "smtp.exmail.qq.com"
SMTP_PORT = 465
```

## 基础连接模板

```python
#!/usr/bin/env python3
"""虹识技术企业邮箱访问工具"""

import imaplib
import ssl
import email
from email.header import decode_header
from datetime import datetime

EMAIL = "kaijun.yi@homsh.cn"
AUTH_CODE = "iSuCYRzJE3xc3ei3"
IMAP_SERVER = "imap.exmail.qq.com"
IMAP_PORT = 993


def decode_mime_header(header):
    """解码邮件头（主题、发件人等）"""
    if not header:
        return ""
    decoded_parts = decode_header(header)
    result = []
    for part, charset in decoded_parts:
        if isinstance(part, bytes):
            try:
                result.append(part.decode(charset or 'utf-8', errors='ignore'))
            except:
                result.append(part.decode('utf-8', errors='ignore'))
        else:
            result.append(part)
    return ''.join(result)


def get_email_body(msg):
    """提取邮件正文"""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                try:
                    charset = part.get_content_charset() or 'utf-8'
                    body = part.get_payload(decode=True).decode(charset, errors='ignore')
                    break
                except:
                    pass
            elif content_type == "text/html" and not body:
                try:
                    charset = part.get_content_charset() or 'utf-8'
                    body = part.get_payload(decode=True).decode(charset, errors='ignore')
                except:
                    pass
    else:
        try:
            charset = msg.get_content_charset() or 'utf-8'
            body = msg.get_payload(decode=True).decode(charset, errors='ignore')
        except:
            pass
    return body


def connect_mailbox():
    """连接邮箱并返回 IMAP 对象"""
    context = ssl.create_default_context()
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT, ssl_context=context)
    mail.login(EMAIL, AUTH_CODE)
    return mail


# 使用示例
if __name__ == "__main__":
    mail = connect_mailbox()
    mail.select("INBOX")

    # 获取所有邮件ID
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    print(f"收件箱共有 {len(email_ids)} 封邮件")

    mail.logout()
```

## 常用操作

### 1. 搜索邮件

```python
# 按发件人搜索
mail.search(None, 'FROM', '"sender@example.com"')

# 按主题搜索
mail.search(None, 'SUBJECT', '"关键词"')

# 按日期搜索（2026年3月1日之后）
mail.search(None, 'SINCE', '01-Mar-2026')

# 按日期范围搜索
mail.search(None, 'SINCE', '01-Mar-2026', 'BEFORE', '31-Mar-2026')

# 搜索未读邮件
mail.search(None, 'UNSEEN')

# 组合搜索
mail.search(None, 'FROM', '"sales@"', 'SINCE', '01-Jan-2026')
```

### 2. 读取邮件内容

```python
def read_email(mail, email_id):
    """读取单封邮件的完整内容"""
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])

    subject = decode_mime_header(msg.get("Subject", ""))
    from_addr = decode_mime_header(msg.get("From", ""))
    to_addr = decode_mime_header(msg.get("To", ""))
    date = msg.get("Date", "")
    body = get_email_body(msg)

    return {
        "subject": subject,
        "from": from_addr,
        "to": to_addr,
        "date": date,
        "body": body
    }
```

### 3. 导出邮件到文件

```python
import os

def export_emails(mail, email_ids, output_dir):
    """导出邮件到指定目录"""
    os.makedirs(output_dir, exist_ok=True)

    for i, email_id in enumerate(email_ids, 1):
        email_data = read_email(mail, email_id)

        # 清理文件名
        safe_subject = "".join(c for c in email_data['subject'][:50] if c.isalnum() or c in ' -_')
        filename = f"{i:04d}_{safe_subject}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"主题: {email_data['subject']}\n")
            f.write(f"发件人: {email_data['from']}\n")
            f.write(f"收件人: {email_data['to']}\n")
            f.write(f"日期: {email_data['date']}\n")
            f.write(f"\n{'='*60}\n\n")
            f.write(email_data['body'])

        print(f"[{i}/{len(email_ids)}] 已导出: {filename}")
```

### 4. 下载附件

```python
def download_attachments(msg, output_dir):
    """下载邮件中的附件"""
    os.makedirs(output_dir, exist_ok=True)
    attachments = []

    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename:
            filename = decode_mime_header(filename)
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))

            attachments.append(filepath)
            print(f"已下载附件: {filename}")

    return attachments
```

### 5. 统计邮件

```python
def get_email_stats(mail):
    """获取邮箱统计信息"""
    folders = ["INBOX", "Sent Messages", "Drafts", "Junk"]
    stats = {}

    for folder in folders:
        try:
            mail.select(folder, readonly=True)
            status, messages = mail.search(None, "ALL")
            count = len(messages[0].split()) if messages[0] else 0
            stats[folder] = count
        except:
            stats[folder] = 0

    return stats
```

## 邮箱文件夹

| 文件夹名 | 说明 |
|---------|------|
| INBOX | 收件箱 |
| Sent Messages | 已发送 |
| Drafts | 草稿箱 |
| Junk | 垃圾邮件 |
| Deleted Messages | 已删除 |

## 注意事项

1. **授权码有效期**: 如果更改了邮箱密码，授权码会失效，需要重新生成
2. **生成新授权码**: 登录 https://exmail.qq.com → 设置 → 微信绑定 → 新增授权密码
3. **连接超时**: 建议设置合理的超时时间，避免长时间等待
4. **大量邮件**: 该邮箱有约 18000 封邮件，批量操作时注意分页处理
5. **编码问题**: 中文邮件可能有多种编码，decode_mime_header 函数已处理常见情况

## 批量下载员工周报

当用户要求下载周报时，使用以下脚本批量下载所有员工的周报 DOCX 附件：

```python
#!/usr/bin/env python3
"""批量下载员工周报 DOCX 附件"""

import imaplib
import ssl
import email
from email.header import decode_header
import os

EMAIL = "kaijun.yi@homsh.cn"
AUTH_CODE = "iSuCYRzJE3xc3ei3"
IMAP_SERVER = "imap.exmail.qq.com"
IMAP_PORT = 993
BASE_DIR = "/Users/zhiquntang/Kaijun_Projects/绩效评估/2026员工"

# 员工列表及对应文件夹
EMPLOYEES = {
    "何国伦": "何国伦/周报",
    "刘志波": "刘志波/周报",
    "吴慧妹": "吴慧妹/周报",
    "吴攀": "吴攀/周报",
    "汪倩": "汪倩/周报",
    "胡晨": "胡晨/周报",
    "胡金山": "胡金山/周报",
    "谢皓涵": "谢皓涵/周报",
    "熊琼": "熊琼/周报",
}

def decode_mime_header(header):
    if not header:
        return ""
    decoded_parts = decode_header(header)
    result = []
    for part, charset in decoded_parts:
        if isinstance(part, bytes):
            try:
                result.append(part.decode(charset or 'utf-8', errors='ignore'))
            except:
                result.append(part.decode('utf-8', errors='ignore'))
        else:
            result.append(part)
    return ''.join(result)

def download_weekly_reports(year=2026):
    """下载指定年份所有员工的周报"""

    # 创建所有目录
    for emp, folder in EMPLOYEES.items():
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

    context = ssl.create_default_context()
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT, ssl_context=context)
    mail.login(EMAIL, AUTH_CODE)
    mail.select("INBOX")

    print(f"搜索{year}年所有周报邮件...")
    status, messages = mail.search(None, 'SINCE', f'01-Jan-{year}')
    email_ids = messages[0].split() if messages[0] else []
    print(f"找到{year}年邮件: {len(email_ids)} 封\n")

    stats = {emp: 0 for emp in EMPLOYEES}
    total = 0

    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        subject = decode_mime_header(msg.get("Subject", ""))

        # 只处理周报/简报邮件
        if "周报" not in subject and "简报" not in subject:
            continue

        # 下载附件
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue

            filename = part.get_filename()
            if filename:
                filename = decode_mime_header(filename)

                # 只下载 docx/doc 文件
                if not (filename.endswith('.docx') or filename.endswith('.doc')):
                    continue

                # 匹配员工
                for emp, folder in EMPLOYEES.items():
                    if emp in filename:
                        filepath = os.path.join(BASE_DIR, folder, filename)

                        if os.path.exists(filepath):
                            continue

                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True))

                        stats[emp] += 1
                        total += 1
                        print(f"✅ [{emp}] {filename}")
                        break

    mail.logout()

    print(f"\n{'='*50}")
    print("📊 下载统计:")
    for emp, count in stats.items():
        if count > 0:
            print(f"   {emp}: {count} 份")
    print(f"\n✅ 共下载 {total} 份周报")

    return stats

if __name__ == "__main__":
    download_weekly_reports(2026)
```

### 下载单个员工的周报

```python
def download_employee_reports(employee_name, year=2026):
    """下载指定员工的周报"""
    output_dir = os.path.join(BASE_DIR, employee_name, "周报")
    os.makedirs(output_dir, exist_ok=True)

    context = ssl.create_default_context()
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT, ssl_context=context)
    mail.login(EMAIL, AUTH_CODE)
    mail.select("INBOX")

    status, messages = mail.search(None, 'SINCE', f'01-Jan-{year}')
    email_ids = messages[0].split() if messages[0] else []

    downloaded = 0
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        subject = decode_mime_header(msg.get("Subject", ""))

        if "周报" not in subject and "简报" not in subject:
            continue

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue

            filename = part.get_filename()
            if filename:
                filename = decode_mime_header(filename)

                if employee_name in filename and (filename.endswith('.docx') or filename.endswith('.doc')):
                    filepath = os.path.join(output_dir, filename)

                    if not os.path.exists(filepath):
                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True))
                        downloaded += 1
                        print(f"✅ {filename}")

    mail.logout()
    print(f"\n✅ {employee_name} 共下载 {downloaded} 份周报")
    return downloaded
```

## 员工邮箱列表

| 员工 | 邮箱 | 部门 |
|-----|------|------|
| 何国伦 | guolun.he@homsh.cn | 软件部 |
| 刘志波 | zhibo.liu@homsh.cn | — |
| 吴慧妹 | huimei.wu@homsh.cn | 行政部 |
| 汪倩 | qian.wang@homsh.cn | 财务部 |
| 谢皓涵 | haohan.xie@homsh.cn | 硬件部 |
| 熊琼 | qiong.xiong@homsh.cn | 财务部 |

## 绩效评估目录结构

```
/Users/zhiquntang/Kaijun_Projects/绩效评估/2026员工/
├── 何国伦/
│   └── 周报/
├── 刘志波/
│   └── 周报/
├── 吴慧妹/
│   └── 周报/
├── 吴攀/
│   └── 周报/
├── 汪倩/
│   └── 周报/
├── 胡晨/
│   └── 周报/
├── 胡金山/
│   └── 周报/
└── 谢皓涵/
    └── 周报/
```

## 相关邮箱

| 邮箱 | 用途 |
|-----|------|
| kaijun.yi@homsh.cn | CEO 主邮箱 |
| sales@opticsiris.com | 销售邮箱 |
| zhibo.liu@homsh.cn | 刘志波 |
