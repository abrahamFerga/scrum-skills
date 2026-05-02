# MCP Setup

Skills in this library use MCP (Model Context Protocol) to read work items from your project management tool. You need one of the following configured in Claude Code.

---

## Azure DevOps

### Recommended MCP server

Use the official or community ADO MCP server. Configure it in your Claude Code settings:

```json
// .claude/settings.json  (project) or ~/.claude/settings.json (global)
{
  "mcpServers": {
    "ado": {
      "command": "npx",
      "args": ["-y", "@your-ado-mcp-package/server"],
      "env": {
        "ADO_ORG_URL": "https://dev.azure.com/your-org",
        "ADO_PAT": "<your-personal-access-token>"
      }
    }
  }
}
```

> **Note:** Never commit your PAT. Use environment variables or a secrets manager.

### Required PAT scopes

| Scope | Reason |
|---|---|
| `Work Items (Read)` | Fetch sprint work items |
| `Work Items (Write)` | Optional — only needed if a skill updates item state |

---

## Jira

### Recommended MCP server

```json
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": ["-y", "@your-jira-mcp-package/server"],
      "env": {
        "JIRA_BASE_URL": "https://your-org.atlassian.net",
        "JIRA_EMAIL": "you@example.com",
        "JIRA_API_TOKEN": "<your-api-token>"
      }
    }
  }
}
```

### Required API token scopes

| Scope | Reason |
|---|---|
| `read:jira-work` | Fetch sprint issues |
| `write:jira-work` | Optional — only needed if a skill transitions issue state |

---

## Verifying your setup

After configuring, run the following inside Claude Code to confirm the MCP is active:

```
/mcp
```

You should see your `ado` or `jira` server listed as connected.

---

## Using skills without MCP

All skills include a manual fallback. If no MCP is connected, the skill will ask you to paste your work items directly into the chat. This is useful for teams that cannot install an MCP server due to security policy.
