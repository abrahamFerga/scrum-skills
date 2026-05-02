#!/usr/bin/env python3
"""
validate-skill.py — agentskills.io spec compliance checker
https://agentskills.io/specification

Usage:
  python3 scripts/validate-skill.py                        # validate all skills
  python3 scripts/validate-skill.py skills/daily-sync-dev  # validate one skill
  python3 scripts/validate-skill.py --strict               # exit 1 on warnings too

Exit codes:
  0 — all checks passed (warnings allowed unless --strict)
  1 — one or more FAIL results found
"""

import re
import os
import sys
import glob
import argparse
from pathlib import Path


# ── Spec constants ────────────────────────────────────────────────────────────

MAX_NAME_LEN        = 64
MAX_DESC_LEN        = 1024
MAX_COMPAT_LEN      = 500
MAX_BODY_LINES      = 500
VALID_NAME_RE       = re.compile(r'^[a-z0-9]([a-z0-9-]*[a-z0-9])?$')
CONSECUTIVE_HYPHEN  = re.compile(r'--')

# Fields allowed at the top level of frontmatter per the spec.
# Any other field must live inside the `metadata:` block.
ALLOWED_TOP_LEVEL   = {'name', 'description', 'license', 'compatibility',
                       'metadata', 'allowed-tools'}

# Common non-spec keys that we want to catch explicitly
KNOWN_NON_SPEC_KEYS = ['ceremony', 'perspective', 'scrum_guide_ref',
                       'requires_mcp', 'mcp_backends', 'version',
                       'references', 'scrum_ref']


# ── Colours (disabled on Windows if not supported) ───────────────────────────

USE_COLOR = sys.stdout.isatty() and os.name != 'nt'

def red(s):    return f'\033[31m{s}\033[0m' if USE_COLOR else s
def yellow(s): return f'\033[33m{s}\033[0m' if USE_COLOR else s
def green(s):  return f'\033[32m{s}\033[0m' if USE_COLOR else s
def bold(s):   return f'\033[1m{s}\033[0m'  if USE_COLOR else s


# ── Result helpers ────────────────────────────────────────────────────────────

def ok(msg):   return ('OK',   green('  [ OK ]'), msg)
def warn(msg): return ('WARN', yellow('  [WARN]'), msg)
def fail(msg): return ('FAIL', red(  '  [FAIL]'), msg)


# ── Validator ─────────────────────────────────────────────────────────────────

def validate(skill_dir: Path) -> list[tuple]:
    results = []
    skill_file = skill_dir / 'SKILL.md'

    # SKILL.md must exist
    if not skill_file.exists():
        return [fail(f'{skill_dir}: SKILL.md not found')]

    content = skill_file.read_text(encoding='utf-8')

    # ── Frontmatter presence ──────────────────────────────────────────────────
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return [fail('No YAML frontmatter found (file must start with ---)')]
    fm = fm_match.group(1)

    # ── name ─────────────────────────────────────────────────────────────────
    name_match = re.search(r'^name:\s*(.+)$', fm, re.MULTILINE)
    if not name_match:
        results.append(fail('name field is missing'))
    else:
        name = name_match.group(1).strip()

        if len(name) == 0:
            results.append(fail('name is empty'))
        elif len(name) > MAX_NAME_LEN:
            results.append(fail(f'name too long: {len(name)} chars (max {MAX_NAME_LEN})'))
        else:
            results.append(ok(f'name length [{len(name)}/{MAX_NAME_LEN}]'))

        if not VALID_NAME_RE.match(name):
            results.append(fail(
                f'name "{name}" contains invalid characters or starts/ends with a hyphen. '
                'Only lowercase a-z, 0-9, and hyphens are allowed.'))
        elif CONSECUTIVE_HYPHEN.search(name):
            results.append(fail(f'name "{name}" contains consecutive hyphens'))
        else:
            results.append(ok(f'name format valid [{name}]'))

        dir_name = skill_dir.name
        if name != dir_name:
            results.append(fail(
                f'name "{name}" does not match parent directory "{dir_name}". '
                'The name field must exactly match the directory name.'))
        else:
            results.append(ok(f'name matches directory [{name}]'))

    # ── description ──────────────────────────────────────────────────────────
    desc_match = re.search(r'^description:\s*(.+?)(?=\n[a-z]|\Z)', fm,
                           re.DOTALL | re.MULTILINE)
    if not desc_match:
        results.append(fail('description field is missing'))
    else:
        desc = desc_match.group(1).strip()
        if len(desc) == 0:
            results.append(fail('description is empty'))
        elif len(desc) > MAX_DESC_LEN:
            results.append(fail(
                f'description too long: {len(desc)} chars (max {MAX_DESC_LEN})'))
        else:
            results.append(ok(f'description length [{len(desc)}/{MAX_DESC_LEN}]'))

        if "don't use" in desc.lower() or "do not use" in desc.lower():
            results.append(ok('negative trigger present ("Don\'t use for...")'))
        else:
            results.append(warn(
                'description has no negative trigger. '
                'Add "Don\'t use for..." to prevent agents from over-triggering.'))

    # ── license ───────────────────────────────────────────────────────────────
    if re.search(r'^license:', fm, re.MULTILINE):
        results.append(ok('license field present'))
    else:
        results.append(warn(
            'license field missing. Recommended: add "license: MIT" '
            'or a reference to a bundled LICENSE file.'))

    # ── compatibility ─────────────────────────────────────────────────────────
    compat_match = re.search(r'^compatibility:\s*(.+)$', fm, re.MULTILINE)
    if compat_match:
        compat = compat_match.group(1).strip()
        if len(compat) > MAX_COMPAT_LEN:
            results.append(fail(
                f'compatibility too long: {len(compat)} chars (max {MAX_COMPAT_LEN})'))
        else:
            results.append(ok(f'compatibility field present [{len(compat)}/{MAX_COMPAT_LEN}]'))
    else:
        results.append(warn(
            'compatibility field missing. Add one if the skill has environment requirements '
            '(MCP, Python version, network access, etc.).'))

    # ── metadata ──────────────────────────────────────────────────────────────
    if re.search(r'^metadata:', fm, re.MULTILINE):
        results.append(ok('metadata block present'))
    else:
        results.append(warn(
            'metadata block missing. Custom fields (version, ceremony, etc.) '
            'must live here, not at the top level.'))

    # ── non-spec top-level keys ───────────────────────────────────────────────
    found_non_spec = []
    for key in KNOWN_NON_SPEC_KEYS:
        if re.search(rf'^{key}:', fm, re.MULTILINE):
            found_non_spec.append(key)
    if found_non_spec:
        results.append(fail(
            f'Non-spec top-level keys found: {found_non_spec}. '
            'Move them inside the metadata: block.'))
    else:
        results.append(ok('no non-spec top-level keys'))

    # ── body length ───────────────────────────────────────────────────────────
    body = content[fm_match.end():]
    line_count = body.count('\n')
    if line_count > MAX_BODY_LINES:
        results.append(fail(
            f'SKILL.md body too long: {line_count} lines (max {MAX_BODY_LINES}). '
            'Move dense content to references/ files.'))
    else:
        results.append(ok(f'body length [{line_count}/{MAX_BODY_LINES} lines]'))

    # ── file references use relative forward-slash paths ─────────────────────
    backslash_refs = re.findall(r'\b\w+\\\w+', body)
    if backslash_refs:
        results.append(warn(
            f'Possible Windows-style paths found: {backslash_refs}. '
            'Use forward slashes (/) for cross-platform compatibility.'))
    else:
        results.append(ok('no backslash paths detected'))

    return results


# ── Runner ────────────────────────────────────────────────────────────────────

def find_skills(root: Path) -> list[Path]:
    """Return all directories under root/skills/ that contain a SKILL.md."""
    skills_dir = root / 'skills'
    if not skills_dir.exists():
        return []
    return sorted([
        p.parent for p in skills_dir.rglob('SKILL.md')
    ])


def run(targets: list[Path], strict: bool) -> int:
    exit_code = 0
    total_ok = total_warn = total_fail = 0

    for skill_dir in targets:
        results = validate(skill_dir)
        print(f'\n{bold(str(skill_dir))}')
        for (level, label, msg) in results:
            print(f'{label}  {msg}')
            if level == 'OK':   total_ok   += 1
            if level == 'WARN': total_warn += 1
            if level == 'FAIL': total_fail += 1; exit_code = 1

    print(f'\n{"-"*60}')
    print(f'Results: {green(str(total_ok)+" passed")}  '
          f'{yellow(str(total_warn)+" warnings")}  '
          f'{red(str(total_fail)+" failed")}')

    if strict and total_warn > 0:
        print(yellow('--strict mode: treating warnings as failures'))
        exit_code = 1

    return exit_code


def main():
    parser = argparse.ArgumentParser(
        description='Validate scrum-skills against the agentskills.io specification.')
    parser.add_argument('targets', nargs='*',
        help='Skill directory paths to validate. Defaults to all skills/ subdirectories.')
    parser.add_argument('--strict', action='store_true',
        help='Exit with code 1 if any warnings are found.')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent

    if args.targets:
        targets = [Path(t) for t in args.targets]
    else:
        targets = find_skills(repo_root)
        if not targets:
            print(red('No skills found under skills/'))
            sys.exit(1)

    sys.exit(run(targets, strict=args.strict))


if __name__ == '__main__':
    main()
