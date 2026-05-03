#!/usr/bin/env python3
"""
Validates every skills/<name>/SKILL.md against the agentskills.io spec.

Rules enforced:
  1. YAML frontmatter is present and parses cleanly.
  2. Required top-level fields: name, description, license.
  3. name matches the parent directory name exactly.
  4. No unknown top-level fields (custom data belongs inside metadata:).
  5. File body is 500 lines or fewer.

Exit codes:
  0 — all skills pass
  1 — one or more skills failed
"""

import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Run: pip install pyyaml")
    sys.exit(1)

# ── Configuration ──────────────────────────────────────────────────────────────

SKILLS_DIR = Path(__file__).parent.parent / "skills"

REQUIRED_FIELDS = {"name", "description", "license"}

# Fields explicitly allowed at the top level of the frontmatter.
# Everything else must live inside metadata:.
ALLOWED_TOP_LEVEL = {"name", "description", "license", "compatibility", "metadata"}

MAX_LINES = 500

# ── Helpers ────────────────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    """
    Returns (frontmatter_dict, error_message).
    error_message is empty string on success.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, "No YAML frontmatter found (expected --- ... --- at top of file)"

    raw_yaml = match.group(1)
    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as exc:
        return None, f"YAML parse error: {exc}"

    if not isinstance(data, dict):
        return None, "Frontmatter parsed but is not a YAML mapping"

    return data, ""


def validate_skill(skill_md: Path) -> list[str]:
    """
    Returns a list of error strings. Empty list means the skill passes.
    """
    errors: list[str] = []
    dir_name = skill_md.parent.name

    # Skip the top-level skills/README.md
    if skill_md.name != "SKILL.md":
        return errors

    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()

    # ── Rule 5: line count ──────────────────────────────────────────────────
    if len(lines) > MAX_LINES:
        errors.append(
            f"File is {len(lines)} lines (max {MAX_LINES}). "
            "Move large reference material to a references/ subdirectory."
        )

    # ── Parse frontmatter ───────────────────────────────────────────────────
    fm, parse_error = parse_frontmatter(text)
    if parse_error:
        errors.append(parse_error)
        return errors  # Can't validate further without parsed data

    # ── Rule 2: required fields ─────────────────────────────────────────────
    for field in sorted(REQUIRED_FIELDS):
        if field not in fm or not fm[field]:
            errors.append(f"Missing required frontmatter field: '{field}'")

    # ── Rule 3: name matches directory ──────────────────────────────────────
    skill_name = fm.get("name", "")
    if skill_name and skill_name != dir_name:
        errors.append(
            f"'name' field '{skill_name}' does not match directory name '{dir_name}'. "
            "The name field must exactly match the skill directory."
        )

    # ── Rule 4: no unknown top-level fields ─────────────────────────────────
    unknown = set(fm.keys()) - ALLOWED_TOP_LEVEL
    if unknown:
        errors.append(
            f"Unknown top-level frontmatter field(s): {sorted(unknown)}. "
            "Custom fields must be nested inside 'metadata:'."
        )

    return errors


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> int:
    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    # Exclude the skills/README.md catch — rglob only picks up SKILL.md files
    skill_files = [f for f in skill_files if f.parent != SKILLS_DIR]

    if not skill_files:
        print(f"No SKILL.md files found under {SKILLS_DIR}")
        return 1

    total = len(skill_files)
    failed: list[tuple[Path, list[str]]] = []

    for skill_md in skill_files:
        errors = validate_skill(skill_md)
        if errors:
            failed.append((skill_md, errors))

    # ── Report ─────────────────────────────────────────────────────────────
    passed = total - len(failed)

    if not failed:
        print(f"PASS: All {total} skills passed validation.")
        return 0

    print(f"FAIL: {len(failed)} of {total} skills failed validation:\n")
    for skill_md, errors in failed:
        rel = skill_md.relative_to(SKILLS_DIR.parent)
        print(f"  {rel}")
        for err in errors:
            print(f"    - {err}")
        print()

    print(f"Passed: {passed}/{total}  Failed: {len(failed)}/{total}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
