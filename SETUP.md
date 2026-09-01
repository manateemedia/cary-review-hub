# Setup — for Nicolette and Angie

Fifteen minutes, once. After this, adding work is "drop file in folder, push."

## 1. Create the private repo on GitHub

1. Go to https://github.com/new
2. Repository name: `cary-review-hub` · Visibility: **Private** · leave everything else unchecked (no README, no .gitignore)
3. Click **Create repository**

## 2. Push this folder to it

In Terminal, inside this folder:

```bash
git remote add origin git@github.com:YOUR-USERNAME/cary-review-hub.git   # or the https:// URL GitHub shows you
python3 scripts/build-manifest.py
git add -A
git commit -m "Initial review hub for GotACase and Final Affairs"
git push -u origin main
```

(Or tell Claude: "push this folder to my new GitHub repo cary-review-hub" — it will run the same steps.)

## 3. Turn on the live hub (GitHub Pages)

1. In the repo on GitHub: **Settings → Pages**
2. Under **Build and deployment → Source**, choose **GitHub Actions**
3. Go to the **Actions** tab. The "Publish review hub" workflow runs automatically on every push; the first run takes about a minute.
4. Your hub is live at `https://YOUR-USERNAME.github.io/cary-review-hub/`

Private repos on GitHub Pages need GitHub Pro/Team for the *site* to be private too. On a free account the repo stays private but the Pages URL is public-but-unlisted (nobody finds it without the link). If that matters, either upgrade or keep the repo private and have Cary run the hub locally (see `CARY-START-HERE.md`).

## 4. Invite Cary

**Settings → Collaborators → Add people** → his GitHub username → role **Write**. Send him the link to `CARY-START-HERE.md`.

## Adding work (every time)

1. Put files in the right numbered folder under `gotacase/` or `final-affairs/`.
   - HTML pages → `03-website/`. Keep CSS/JS inline or in the same folder so previews work.
   - Design exports → `02-brand-and-design/` as PNG/PDF/SVG (Figma links go in that folder's README).
   - Markdown, docs, copy → `04-copy-and-content/`
   - Process/flow → `05-workflow/`
2. When something is ready for Cary, mark it in `<company>/status.json`:
   ```json
   "03-website/homepage.html": { "status": "in-review", "note": "Two hero options — see 04-copy-and-content/hero-options.md" }
   ```
3. `git add -A && git commit -m "GotACase: homepage v3 ready for review" && git push`

The hub rebuilds itself. Cary's "Waiting on you" list shows everything marked `in-review`.

## Working from Claude (Cowork or Claude Code)

Connect this folder, then just ask: "add these three files to Final Affairs website, mark them in-review with a note that the pricing table is placeholder, and push." `CLAUDE.md` in the repo tells Claude the conventions.

## If Cary edits something and you disagree

Everything is in git. `git log -p -- path/to/file` shows exactly what changed. Reply by editing the file again and adding a line to `DECISIONS.md`, or ask him to reopen it. Cary's entry in `DECISIONS.md` is final unless he changes it.
