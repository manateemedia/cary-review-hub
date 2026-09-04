# Cary — start here

This repo is everything Nicolette and Angie have built for **GotACase** and **Final Affairs**, in one place. You're the decision maker; the goal is that you can see the whole workflow, change anything, and record decisions without going through anyone.

## Just look

Open the live hub link Nicolette sent you (it ends in `github.io/cary-review-hub/`). Switch companies at the top, click any file on the left to see it rendered. The **In review** filter shows what's waiting on you.

## Tell us what you want changed

Every page in the hub has three buttons under the title: **Approve**, **Request changes**, and **Comment**. Click one, type your note in the box that opens (the page name is already filled in), and press the green button at the bottom. Nicolette and Angie get an email right away, and your note appears in the hub under that page so everyone sees the same thread. The **Feedback** link at the top of the hub lists everything you've said and whether it's been handled.

The first time, GitHub will ask you to sign in — that's the free account Nicolette added you to.

## Make edits with your Claude

One-time:

```bash
git clone git@github.com:NICOLETTES-USERNAME/cary-review-hub.git
cd cary-review-hub
claude
```

Then talk to it like you'd talk to Nicolette:

- "Show me the GotACase homepage and tell me what's still marked in review."
- "Change the hero headline on the GotACase homepage to 'Your case, handled.' and approve it."
- "I don't like the plum in the Final Affairs palette — swap it for a deep navy across the brand files and mark them changes-requested with a note saying why."
- "Log a decision: Final Affairs launches with the subscription model, not one-time pricing."
- "Push my changes."

Claude already knows the repo's rules (they're in `CLAUDE.md`): it edits files in place, updates the status file, writes the decision log entry, and pushes. The hub updates itself about a minute after you push.

Before a session, run `git pull` (or ask Claude to) so you have Nicolette and Angie's latest.

## Quick edits without cloning

Every file in the hub has an **Edit on GitHub** button. Fine for a typo or a copy tweak.

## Statuses

| Status | Meaning |
|---|---|
| Draft | N&A are still working on it — no need to look yet |
| In review | Ready for your call |
| Approved | You've signed off |
| Changes requested | You sent it back; your note says why |

## Running the hub locally (optional)

If the live link isn't set up yet or you want to preview your own edits before pushing:

```bash
python3 scripts/build-manifest.py
python3 -m http.server 8000
```

Then open http://localhost:8000
