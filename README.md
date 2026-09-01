# Cary Review Hub — GotACase & Final Affairs

One place for everything Nicolette and Angie have built for the two companies, so Cary can see the whole workflow, review it rendered, and make edits directly with his Claude.

**Live hub (after GitHub Pages is on):** `https://<your-github-username>.github.io/cary-review-hub/`

## How it's organized

```
cary-review-hub/
├── index.html            ← the hub: browse + preview every file in one place
├── manifest.json         ← auto-generated list of files (don't edit by hand)
├── DECISIONS.md          ← Cary's running log of decisions (the source of truth)
├── gotacase/
│   ├── status.json       ← per-file status: draft / in-review / approved / changes-requested
│   ├── 01-strategy/
│   ├── 02-brand-and-design/
│   ├── 03-website/
│   ├── 04-copy-and-content/
│   ├── 05-workflow/
│   └── 06-assets/
├── final-affairs/
│   └── (same structure)
├── shared/               ← anything that applies to both companies
├── scripts/build-manifest.py
└── .github/workflows/pages.yml   ← rebuilds manifest + publishes the hub on every push
```

Drop files into the numbered folders. HTML, Markdown, images, PDFs, JSON, CSV and plain text all show up in the hub automatically on the next push. Folder numbers keep things in workflow order; rename or add folders freely — the hub reads whatever is there.

## Roles

| Who | Does what |
|---|---|
| Nicolette & Angie | Add and revise work. Push to `main` (or open a PR if you want Cary to approve before it lands). |
| Cary | Final decision maker. Reviews in the hub, edits files with Claude Code, updates `status.json` and `DECISIONS.md`, pushes. |

## Quick start

- **Nicolette / Angie:** see `SETUP.md`
- **Cary:** see `CARY-START-HERE.md` (and `CLAUDE.md` is already written for your Claude)

## Rules of the road

1. `main` is always the current state of truth. The live hub reflects `main`.
2. Every file has a status in its company's `status.json`. Anything not listed is `draft`.
3. Decisions go in `DECISIONS.md`, newest at the top, with a date and who decided.
4. Commit messages say what changed and why in one line — Claude will do this for you.
