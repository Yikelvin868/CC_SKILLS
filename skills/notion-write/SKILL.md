# Notion 写入技能

## 配置

- **API Token**: `ntn_O45890749248MdIM2Zc3EIwaiACnf0cFcXFaKKP3zZVcNC`
- **技术研究板块 Page ID**: `30f11187-b9ec-819a-b2b4-fd42ff4aa4af`

## 使用方法

### 创建子页面

```bash
curl -X POST https://api.notion.com/v1/pages \
  -H "Authorization: Bearer ntn_O45890749248MdIM2Zc3EIwaiACnf0cFcXFaKKP3zZVcNC" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
  "parent": {"page_id": "30f11187-b9ec-819a-b2b4-fd42ff4aa4af"},
  "properties": {
    "title": [{"text": {"content": "页面标题"}}]
  },
  "children": [
    {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"text":{"content":"内容"}}]}}
  ]
}'
```

## 常用 Block 类型

### 标题
```json
{"object":"block","type":"heading_2","heading_2":{"rich_text":[{"text":{"content":"标题"}}]}}
```

### 段落
```json
{"object":"block","type":"paragraph","paragraph":{"rich_text":[{"text":{"content":"内容"}}]}}
```

### 无序列表
```json
{"object":"block","type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"text":{"content":"项目"}}]}}
```

### 有序列表
```json
{"object":"block","type":"numbered_list_item","numbered_list_item":{"rich_text":[{"text":{"content":"步骤"}}]}}
```

### 待办事项
```json
{"object":"block","type":"to_do","to_do":{"rich_text":[{"text":{"content":"任务"}}],"checked":false}}
```

### 代码块
```json
{"object":"block","type":"code","code":{"language":"python","rich_text":[{"text":{"content":"代码"}}]}}
```

### Callout
```json
{"object":"block","type":"callout","callout":{"icon":{"emoji":"💡"},"rich_text":[{"text":{"content":"提示内容"}}]}}
```

## 快速写入模板

当用户说"写入 Notion 技术研究板块"时，构造上述 JSON 并调用 API。
