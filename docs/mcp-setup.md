# MCP Setup

Skills auto-detect the connected project management tool at runtime — no configuration inside skill files. Configure the MCP server once at the project or global level, then skills pick it up automatically.

---

## Azure DevOps

### MCP server

Use the official Microsoft package: [`@azure-devops/mcp`](https://github.com/microsoft/azure-devops-mcp)

**1. Create the local config file** (never commit this)

Copy `.mcp.json.example` to `.mcp.json` and fill in your org name:

```json
{
  "mcpServers": {
    "azure-devops": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "<your-org-name>", "--authentication", "pat"],
      "env": {
        "PERSONAL_ACCESS_TOKEN": "<base64 of 'user:your-raw-pat'>"
      }
    }
  }
}
```

**2. Create a Personal Access Token (PAT)**

Go to `https://dev.azure.com/<your-org>/_usersSettings/tokens` and create a token with the scopes your skills need:

| Scope | Required by |
|---|---|
| `Work Items (Read)` | All ceremony and audit skills |
| `Work Items (Write)` | `po-create-user-story`, `audit-sprint-ado` (comments), `audit-sprint-retrospective-ado` (action item creation) |
| `Wiki (Read)` | `audit-sprint-retrospective-ado` (reads wiki retro pages) |
| `Wiki (Write)` | `audit-sprint-ado`, `audit-sprint-retrospective-ado` (optional — posts summaries to wiki) |
| `Project and Team (Read)` | `sprint-planning`, `sprint-review` (reads team capacity and iterations) |

Grant only the scopes you need. Most read-only workflows need only `Work Items (Read)`.

**3. Encode the PAT**

```powershell
# PowerShell
[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("user:YOUR_PAT_HERE"))
```

```bash
# bash / macOS / WSL
echo -n "user:YOUR_PAT_HERE" | base64
```

Paste the result as `PERSONAL_ACCESS_TOKEN` in `.mcp.json`.

> **Never commit `.mcp.json`** — it is listed in `.gitignore`. Use `.mcp.json.example` as the shareable template.

**4. Set your default project in `CLAUDE.md`**

Skills ask for the ADO project on every new session unless you declare it in your project's `CLAUDE.md`. Add this once and you will never be prompted again:

```markdown
## ADO defaults
- **Project:** `your-project-name`
- **Team:** `your-team-name`
Always pass these values to ADO tools — never prompt for project or team selection.
```

Replace `your-project-name` with the name shown in your ADO URL: `https://dev.azure.com/<org>/<your-project-name>`.

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

| Scope | Required by |
|---|---|
| `read:jira-work` | All Jira ceremony and audit skills |
| `write:jira-work` | `po-create-user-story` (creates issues), `audit-sprint-jira` (comments) |

---

## Verify the connection

Restart Claude Code in your project directory, then run:

```
/mcp
```

You should see `azure-devops` or `jira` listed as connected. If neither appears, check that `.mcp.json` is in the project root (not a subdirectory) and that the PAT is correctly base64-encoded.

### Common connection issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser OAuth window opens | `--authentication pat` arg missing | Add `"--authentication", "pat"` to the `args` array |
| `401 Unauthorized` | PAT not base64-encoded, or wrong format | Re-encode as `base64("user:YOUR_PAT")` |
| Skills keep asking for the project | No `CLAUDE.md` in the project root | Add ADO defaults to `CLAUDE.md` (see step 4 above) |
| MCP not listed in `/mcp` | `.mcp.json` not in project root | Move file to the root of the project Claude Code is opened in |
| PAT rejected | Wrong scopes | Regenerate PAT with required scopes from the table above |

---

## Using skills without MCP

All skills include a manual fallback. When no MCP is connected the skill asks you to paste sprint items, work item content, or retro notes directly into the chat.

Useful for:
- Teams with security restrictions on MCP servers
- GitHub Copilot (does not support MCP — manual mode always applies)
- Cursor users who haven't configured MCP yet

---

## Security checklist

- [ ] `.mcp.json` is in `.gitignore` *(already set in this repo)*
- [ ] `.claude/settings.local.json` is in `.gitignore` *(already set in this repo)*
- [ ] PAT has only the minimum required scopes for your workflow
- [ ] PAT has an expiry date set (recommended: 90 days or less)
- [ ] No PAT values appear in any tracked file, commit message, or PR description
- [ ] If a PAT is accidentally exposed, rotate it immediately at `https://dev.azure.com/<org>/_usersSettings/tokens`
