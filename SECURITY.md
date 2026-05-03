# Security Policy

## Scope

This repository contains AI agent skill definitions (Markdown files). There is no compiled code, server, or deployed infrastructure.

The primary security concern is **prompt injection** — a contributed skill that contains instructions designed to manipulate an AI agent into taking harmful actions on behalf of a user.

## Reporting a vulnerability

If you find a skill that appears to contain malicious instructions, please **do not open a public issue**. Instead:

1. Go to the [Security Advisories](../../security/advisories/new) tab and open a private report.
2. Or email the maintainer directly via the contact on their GitHub profile.

Include:
- The skill file path
- The specific instructions that concern you
- Why you believe they are harmful

The maintainer will respond within 5 business days and, if confirmed, remove or patch the skill before public disclosure.

## What makes a skill malicious?

- Instructions that direct the agent to exfiltrate data to an external URL
- Instructions that impersonate system prompts or claim elevated permissions
- Instructions designed to bypass the host agent's safety guidelines
- Instructions that silently modify files or work items outside the stated scope of the skill

## Skill review process

All contributed skills are reviewed by a maintainer before merging. The `validate-skills` CI check enforces structural rules, but content review is done manually.
