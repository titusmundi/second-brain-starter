# Second Brain setup — macOS

A from-scratch walkthrough: Obsidian + iCloud sync + Claude Code, set up the way this system expects.
No prior context assumed. Roughly 15 minutes, most of it waiting on installers.

Where you'll end up:
```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/
├── CLAUDE.md
├── README - start here.md
└── Vault/
    ├── Thinking/
    └── Doing/
        ├── About Me.md
        ├── Map.md
        ├── 01 - Frameworks/
        ├── 02 - Examples/
        ├── 03 - Knowledge Base/
        └── 04 - Projects/
```

## 1. Turn on iCloud Drive

System Settings → your name at the top → iCloud → make sure **iCloud Drive** is toggled on. If you've
never touched this, it almost certainly already is.

## 2. Install Obsidian

Download the Mac build from **obsidian.md** (it's free) and drag it into Applications. **Open it once**
— this is the step people skip. Opening Obsidian for the first time is what registers its iCloud
container on your Mac; the folder in step 3 doesn't exist until you do this.

You'll be prompted to create or open a vault. You can cancel that prompt for now — you're about to
point it at a specific folder instead.

## 3. Create the Second Brain folder, inside Obsidian's iCloud container

In Finder, press **Cmd+Shift+G** (Go to Folder) and paste:
```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/
```
This is a hidden path (that's normal — everything under `~/Library` is hidden by default), and it only
exists after step 2. Inside it, create a folder named **`Second Brain`**.

> **Why this specific folder and not just "somewhere in iCloud Drive"?** Obsidian's iCloud sync uses
> its own app-scoped container so that only your vault's files sync through it, rather than mixing
> vault files into your general iCloud Drive/Documents. It also means Obsidian's iOS/iPadOS app finds
> the vault automatically with zero configuration, if you ever use one. Anywhere else that's
> iCloud-synced would technically work, but this is the path the rest of this system assumes, and it's
> what keeps a phone or iPad picking the vault up for free.

## 4. Lay out the folders

Inside `Second Brain/`, create:
```
Second Brain/
└── Vault/
    ├── Thinking/
    └── Doing/
        ├── 01 - Frameworks/
        ├── 02 - Examples/
        ├── 03 - Knowledge Base/
        │   └── People/
        └── 04 - Projects/
```
Empty folders are fine at this point.

## 5. Drop in the starter files

Copy these from this skill's `assets/` folder into place (if a person, not Claude, is doing this by
hand, they were bundled alongside this guide):

| File | Goes to |
| --- | --- |
| `CLAUDE.md` | `Second Brain/CLAUDE.md` |
| `README - start here.md` | `Second Brain/README - start here.md` |
| `Map.md` | `Second Brain/Vault/Doing/Map.md` |
| `About Me.md` | `Second Brain/Vault/Doing/About Me.md` |
| `How to write a framework.md` | `Second Brain/Vault/Doing/01 - Frameworks/How to write a framework.md` |
| `Good and bad, side by side.md` | `Second Brain/Vault/Doing/02 - Examples/Good and bad, side by side.md` |
| `_Project Template.md` | `Second Brain/Vault/Doing/04 - Projects/_Project Template.md` |
| `Projects Index.md` | `Second Brain/Vault/Doing/04 - Projects/Projects Index.md` |

In `CLAUDE.md`, replace the `{{SECOND_BRAIN_PATH}}` placeholder near the top with the real path:
`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/`.

## 6. Open the vault in Obsidian

Obsidian → **Open folder as vault** → select `Second Brain/Vault` (not `Second Brain` itself — Obsidian
should only ever see the `Vault` folder). You should see `Thinking` and `Doing` in the left sidebar and
nothing else. That confirms iCloud sync and the folder layout are both working.

## 7. Install Claude Code

Two ways to get it; pick whichever fits how you work.

- **Claude desktop app (simplest, no terminal needed).** Download the Mac app from **claude.com/download**,
  sign in, and open its **Code** tab. Use its "open folder" action to point it at `Second Brain` — the
  parent folder, **not** `Vault`. This is what this particular setup uses.
- **Claude Code CLI (for terminal users).** Install it with Anthropic's native installer (no Node.js needed):
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  ```
  (Homebrew also works: `brew install --cask claude-code`.) Open a new terminal window and run
  `claude --version` to confirm. Launch it from the right folder every time:
  ```bash
  cd ~/"Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
  claude
  ```
  The first time, `claude` opens a browser to sign in. Claude Code needs a paid Claude account (Pro, Max, Team
  or Enterprise) or Anthropic API access; the free claude.ai plan does not include it. Install steps change, so
  check **code.claude.com/docs/en/setup** if anything here does not match what you see.

Either way, the folder you open Claude on is `Second Brain` — one level **above** the vault — so that
`CLAUDE.md` loads automatically at the start of every session. Obsidian and Claude are deliberately
pointed at two different levels of the same tree; that's not a mistake to fix.

## 8. Fill in About Me

Inside the Claude session, say:

> *"Read Vault/Doing/Map.md and Vault/Doing/About Me.md, then ask me the three questions you most need
> answered to be useful to me."*

Answer in plain English. When Claude asks a follow-up question, the setup is done.

## Verify it actually synced

Edit a note in Obsidian, wait ~10 seconds, then check the iCloud icon in the menu bar isn't showing a
spinning-sync state forever. If you have another Apple device signed into the same iCloud account,
opening Obsidian there (or Files → iCloud Drive → Obsidian on iOS) and seeing the same file is the real
proof.

## Gotchas
- If `~/Library/Mobile Documents/iCloud~md~obsidian/` doesn't exist yet, you skipped opening Obsidian
  once first (step 2) — go do that, then come back.
- Point Claude at `Second Brain`, not `Second Brain/Vault`. Pointing it at `Vault` means `CLAUDE.md`
  never loads and every session starts with no conventions.
- `~/Library` is hidden in Finder by default. Cmd+Shift+G (Go to Folder) is the fast way in; there's
  nothing wrong with your Mac if you can't find it by clicking around.
