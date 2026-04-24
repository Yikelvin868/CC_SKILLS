---
name: supermemory
description: Persistent memory management using Supermemory MCP. Save, recall, and organize memories across sessions. Use when storing user preferences, project context, or retrieving past knowledge.
---

# Supermemory - Persistent Memory Management

This skill provides persistent memory across Claude Code sessions via the Supermemory MCP server.

## When to Activate

- User asks to "remember" or "save" something
- User asks to "recall" or "search" past context
- User wants to store project-specific knowledge
- User asks "what do you know about me/this project?"
- User wants to organize memories by project
- Starting a new session and need prior context

## Prerequisites

Supermemory MCP must be configured in `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "supermemory": {
      "url": "https://mcp.supermemory.ai/mcp"
    }
  }
}
```

## Available Tools

### 1. memory - Save or Forget Information

Save a memory:
```
Tool: mcp__supermemory__memory
Parameters:
  - content (string, required): The information to save
  - action (string, optional): "save" or "forget" (default: "save")
  - containerTag (string, optional): Project tag to scope the memory
```

Forget a memory:
```
Tool: mcp__supermemory__memory
Parameters:
  - content: "description of what to forget"
  - action: "forget"
```

### 2. recall - Search and Retrieve Memories

```
Tool: mcp__supermemory__recall
Parameters:
  - query (string, required): Search query
  - includeProfile (boolean, optional): Include user profile summary (default: true)
  - containerTag (string, optional): Project tag to scope the search
```

### 3. whoAmI - Get Current User Info

```
Tool: mcp__supermemory__whoAmI
Parameters: (none)
```

## Resources

- `supermemory://profile` - User preferences and activity summary
- `supermemory://projects` - Available memory projects

## Usage Patterns

### Save Project Context
When working on a project, save key decisions and patterns:
```
memory(content="Project X uses Next.js 15 with App Router, Supabase for DB, and Tailwind CSS", containerTag="project-x")
```

### Save User Preferences
Store user preferences for future sessions:
```
memory(content="User prefers functional components, Vim keybindings, and dark theme", action="save")
```

### Recall Before Starting Work
At the beginning of a session, recall relevant context:
```
recall(query="project setup and architecture decisions", containerTag="project-x")
```

### Recall User Profile
Get a summary of stored user knowledge:
```
recall(query="user preferences", includeProfile=true)
```

### Forget Outdated Information
Remove outdated memories:
```
memory(content="Project X no longer uses Redux", action="forget")
```

### Organize by Project
Use containerTag to scope memories to specific projects:
```
memory(content="API uses JWT auth with refresh tokens", containerTag="my-api")
recall(query="authentication", containerTag="my-api")
```

## Workflow Integration

### Session Start
1. Use `recall` to retrieve relevant context for the current task
2. Use `whoAmI` to verify identity if needed
3. Read `supermemory://profile` for user summary

### During Work
1. Save important decisions with `memory`
2. Tag memories with project names using `containerTag`
3. Recall past decisions before making new ones

### Session End
1. Save key learnings and decisions made
2. Save any unfinished task context for next session
3. Forget any outdated information that was corrected

## Troubleshooting

If supermemory tools are not available:
1. Check `~/.claude/settings.json` for correct MCP config
2. Restart Claude Code session to reconnect MCP
3. Verify internet connectivity (supermemory is a remote MCP)
4. Check if authentication is required (API key or OAuth)

## Best Practices

- Save concise, specific memories (not entire code blocks)
- Use descriptive containerTags for project organization
- Recall before saving to avoid duplicates
- Forget outdated information to keep memory clean
- Include context in memories: WHY decisions were made, not just WHAT
