#!/usr/bin/env python3
"""Validate the public skills package without third-party dependencies."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "clinicas-saude-lp-suite"
SKILL = PLUGIN / "skills" / "clinicas-saude-lp-completa"
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}


def frontmatter(path: Path) -> str:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: {exc}")
        return ""
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        ERRORS.append(f"{path.relative_to(ROOT)}: YAML frontmatter missing")
        return ""
    return match.group(1)


skill_md = SKILL / "SKILL.md"
fm = frontmatter(skill_md)
require(re.search(r"(?m)^name:\s*clinicas-saude-lp-completa\s*$", fm) is not None,
        "SKILL.md name must match its folder")
require(re.search(r"(?m)^description:\s*", fm) is not None,
        "SKILL.md description missing")

# Check relative Markdown links within the skill tree.
for md in SKILL.rglob("*.md"):
    for target in re.findall(r"\]\(([^\s)]+)\)", md.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("#"):
            continue
        rel = target.split("#", 1)[0]
        if rel and not (md.parent / rel).resolve().exists():
            ERRORS.append(f"broken reference in {md.relative_to(ROOT)}: {target}")

plugin = read_json(PLUGIN / ".claude-plugin" / "plugin.json")
marketplace = read_json(ROOT / ".claude-plugin" / "marketplace.json")
require(plugin.get("name") == "clinicas-saude-lp-suite", "plugin name mismatch")
require(plugin.get("version") == "1.0.0", "plugin version must be 1.0.0")
require("MIT" in (ROOT / "LICENSE").read_text(encoding="utf-8"), "MIT license missing")
require(any(p.get("name") == plugin.get("name") for p in marketplace.get("plugins", [])),
        "marketplace entry must match plugin name")
require((PLUGIN / "agents" / "clinicas-saude-lp-completa-agent.md").is_file(),
        "Claude coordinator agent missing")
require((SKILL / "agents" / "openai.yaml").is_file(), "Codex UI metadata missing")

# Catch common credential formats without flagging documentation labels.
secret_patterns = [
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bsk-ant-api03-[A-Za-z0-9_-]{30,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    for pattern in secret_patterns:
        if pattern.search(content):
            ERRORS.append(f"possible credential pattern in {path.relative_to(ROOT)}")
            break

if ERRORS:
    print(json.dumps({"valid": False, "errors": ERRORS}, indent=2))
    raise SystemExit(1)
print(json.dumps({"valid": True, "skill": "clinicas-saude-lp-completa", "plugin": plugin["name"], "version": plugin["version"], "errors": []}, indent=2))
