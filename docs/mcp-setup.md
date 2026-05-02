# MCP Setup

Skills auto-detect the connected project management tool at runtime — no configuration inside skill files. You only need to configure the MCP server once, at the project or global level.

---

## Azure DevOps

### MCP server

Use the official Microsoft package: [`@azure-devops/mcp`](https://github.com/microsoft/azure-devops-mcp)

**1. Create the local config file** (never commit this):

Copy `.mcp.json.example` to `.mcp.json` and fill in your org name:

```json
{
  "mcpServers": {
    "azure-devops": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "<your-org-name>", "--authentication", "pat"],
      "env": {
        "PERSONAL_ACCESS_TOKEN": "<base64 of 'anystring:your-raw-pat'>"
      }
    }
  }
}
```

**2. Create a Personal Access Token (PAT)**

Go to `https://dev.azure.com/<your-org>/_usersSettings/tokens` and create a token with:

| Scope | Reason |
|---|---|
| `Work Items (Read)` | Fetch sprint work items |
| `Work Items (Write)` | Optional — only if a skill creates or updates items |

**3. Encode the PAT**

```powershell
# PowerShell
[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("user:YOUR_PAT_HERE"))
```

```bash
# bash / macOS
echo -n "user:YOUR_PAT_HERE" | base64
```

Set the result as `PERSONAL_ACCESS_TOKEN` in `.mcp.json`.

> **Never commit `.mcp.json`** — it is listed in `.gitignore`. Use `.mcp.json.example` as the shareable template.

---

## Jira

### MCP server

Use your preferred Jira MCP package and configure it in `.mcp.json`:

```json
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": ["-y", "<your-jira-mcp-package>"],
      "env": {
        "JIRA_BASE_URL": "https://your-org.atlassian.net",
        "JIRA_EMAIL": "you@example.com",
        "JIRA_API_TOKEN": "<your-api-token>"
      }
    }
  }
}
```

Create a Jira API token at `https://id.atlassian.com/manage-profile/security/api-tokens`.

| Scope | Reason |
|---|---|
| `read:jira-work` | Fetch sprint issues |
| `write:jira-work` | Optional — only if a skill creates or transitions issues |

---

## Verify the connection

Restart Claude Code in your project directory, then run:

```
/mcp
```

You should see `azure-devops` or `jira` listed as connected.

---

## Using skills without MCP

All skills include a manual fallback. When no MCP is connected, the skill asks you to paste your sprint items directly into the chat. Useful for teams with security restrictions on MCP servers or when using agents that don't support MCP (e.g. GitHub Copilot Chat).

---

## Security checklist

- [ ] `.mcp.json` is in `.gitignore` *(already set in this repo)*
- [ ] `.claude/settings.local.json` is in `.gitignore` *(already set in this repo)*
- [ ] PAT has only the minimum required scopes
- [ ] PAT has an expiry date set
- [ ] You are not storing PAT values in any tracked file
