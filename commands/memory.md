# /memory - Supermemory Management

Manage persistent memories across Claude Code sessions using Supermemory MCP.

## Usage

```
/memory                    # Interactive mode - choose action
/memory save <content>     # Save a memory
/memory recall <query>     # Search memories
/memory forget <content>   # Remove a memory
/memory profile            # View user profile and summary
/memory whoami             # Check current user identity
```

## Process

### Parse Command Arguments

Parse the arguments passed to this command:
- If no arguments: ask user what they want to do (save/recall/forget/profile)
- If starts with "save": save the remaining text as a memory
- If starts with "recall" or "search": search memories with the remaining text as query
- If starts with "forget" or "remove": forget the memory matching the remaining text
- If "profile": recall with includeProfile=true
- If "whoami": call whoAmI tool

### Step 1: Load Supermemory Tools

Use ToolSearch to find and load supermemory MCP tools:
```
ToolSearch query: "+supermemory"
```

If no tools found, inform user that supermemory MCP is not connected and suggest:
1. Restart Claude Code session
2. Check ~/.claude/settings.json configuration

### Step 2: Execute Action

#### Save Memory
```
Tool: mcp__supermemory__memory
- content: the information to save
- action: "save"
- containerTag: (optional) project name if specified
```

Confirm to user what was saved.

#### Recall Memory
```
Tool: mcp__supermemory__recall
- query: the search query
- includeProfile: true (unless user says otherwise)
- containerTag: (optional) project name if specified
```

Display results in a readable format.

#### Forget Memory
```
Tool: mcp__supermemory__memory
- content: description of what to forget
- action: "forget"
```

Confirm to user what was removed.

#### Profile
```
Tool: mcp__supermemory__recall
- query: "user profile preferences"
- includeProfile: true
```

Display the user profile summary.

#### Who Am I
```
Tool: mcp__supermemory__whoAmI
```

Display user identity information.

### Step 3: Report Results

- For save/forget: confirm the action was completed
- For recall: display memories in a clean, organized format
- For profile: show user profile summary
- For whoami: show user identity

## Notes

- Supermemory MCP must be configured in ~/.claude/settings.json
- Memories persist across sessions and across different AI tools
- Use containerTag to organize memories by project
- Memories are semantically searchable (not just keyword matching)
