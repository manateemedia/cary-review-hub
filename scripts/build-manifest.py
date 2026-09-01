#!/usr/bin/env python3
"""Walk the company folders and write manifest.json for index.html.

Run from the repo root:  python3 scripts/build-manifest.py
The GitHub Action runs this automatically on every push.
"""
import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = {
    "gotacase": "GotACase",
    "final-affairs": "Final Affairs",
    "shared": "Shared",
}
SKIP_NAMES = {".DS_Store", "status.json", ".gitkeep", "Thumbs.db"}
KIND_BY_EXT = {
    ".html": "html", ".htm": "html",
    ".md": "markdown", ".markdown": "markdown", ".txt": "text",
    ".png": "image", ".jpg": "image", ".jpeg": "image", ".gif": "image",
    ".svg": "image", ".webp": "image",
    ".pdf": "pdf",
    ".json": "code", ".csv": "code", ".css": "code", ".js": "code", ".yml": "code", ".yaml": "code",
    ".docx": "download", ".pptx": "download", ".xlsx": "download", ".fig": "download", ".zip": "download",
}


def git_last_modified(path: Path):
    """ISO date of last commit touching the file; falls back to mtime."""
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%cI", "--", str(path.relative_to(ROOT))],
            cwd=ROOT, stderr=subprocess.DEVNULL, text=True,
        ).strip()
        if out:
            return out
    except Exception:
        pass
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(path.stat().st_mtime))


def repo_url():
    """https://github.com/owner/repo from the origin remote, for 'Edit on GitHub' links."""
    try:
        url = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=ROOT,
                                      stderr=subprocess.DEVNULL, text=True).strip()
    except Exception:
        return ""
    if url.startswith("git@github.com:"):
        url = "https://github.com/" + url.split(":", 1)[1]
    return url.removesuffix(".git")


def folder_label(name: str) -> str:
    # "02-brand-and-design" -> "Brand and Design"
    parts = name.split("-", 1)
    label = parts[1] if len(parts) == 2 and parts[0].isdigit() else name
    return label.replace("-", " ").replace("_", " ").title().replace(" And ", " and ")


def build():
    manifest = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "repo": repo_url(), "companies": []}
    for slug, display in COMPANIES.items():
        base = ROOT / slug
        if not base.exists():
            continue
        status_file = base / "status.json"
        status = {}
        if status_file.exists():
            try:
                status = json.loads(status_file.read_text()).get("files", {})
            except json.JSONDecodeError:
                print(f"WARNING: {status_file} is not valid JSON; ignoring")
        sections = []
        for folder in sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith(".")):
            files = []
            for f in sorted(folder.rglob("*")):
                if not f.is_file() or f.name in SKIP_NAMES or f.name.startswith("."):
                    continue
                rel = f.relative_to(ROOT).as_posix()
                st = status.get(f.relative_to(base).as_posix(), {})
                files.append({
                    "path": rel,
                    "name": f.name,
                    "kind": KIND_BY_EXT.get(f.suffix.lower(), "download"),
                    "size": f.stat().st_size,
                    "modified": git_last_modified(f),
                    "status": st.get("status", "draft"),
                    "note": st.get("note", ""),
                })
            readme = folder / "README.md"
            sections.append({
                "slug": folder.name,
                "label": folder_label(folder.name),
                "readme": readme.relative_to(ROOT).as_posix() if readme.exists() else None,
                "files": files,
            })
        manifest["companies"].append({"slug": slug, "name": display, "sections": sections})
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    n = sum(len(s["files"]) for c in manifest["companies"] for s in c["sections"])
    print(f"manifest.json written: {n} files across {len(manifest['companies'])} companies")


if __name__ == "__main__":
    build()
