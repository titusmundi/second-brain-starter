# Second Brain setup — Windows

A from-scratch walkthrough for the PC side of the same system: Obsidian + iCloud sync + Claude Code.
No prior context assumed. The Mac side of this system uses an Apple-only feature (an app-specific
iCloud folder) that Windows doesn't have an equivalent of, so step 3 below is a deliberate, honest
adaptation rather than a literal copy — read the callout there before you pick a folder.

Where you'll end up (path confirmed in step 3):
```
<iCloud Drive>\Second Brain\
├── CLAUDE.md
├── README - start here.md
└── Vault\
    ├── Thinking\
    └── Doing\
        ├── About Me.md
        ├── Map.md
        ├── 01 - Frameworks\
        ├── 02 - Examples\
        ├── 03 - Knowledge Base\
        └── 04 - Projects\
```

## 1. Install iCloud for Windows

Get **iCloud** from the Microsoft Store (search "iCloud", publisher Apple Inc.) — this is the
supported route on current Windows 10/11 and keeps itself updated. Sign in with the **same Apple ID**
the Mac side uses (if there is a Mac side). In the iCloud app, tick **iCloud Drive**, then give it a
minute to finish its first sync.

## 2. Install Obsidian

Download the Windows build from **obsidian.md** (free) and run the installer.

## 3. Choose where the vault lives — read this before creating folders

On Mac, this system stores the vault inside Obsidian's own private iCloud container
(`iCloud~md~obsidian`), which is a macOS app-sandboxing feature. Windows doesn't have app-scoped
iCloud folders in that sense, and whether that specific container even shows up on the Windows side
depends on your iCloud version and isn't something worth relying on.

**Use the general iCloud Drive folder instead** — it's the reliable, symmetric choice:
- Open File Explorer → **This PC** → **iCloud Drive** (or find it under "iCloud Drive" in the sidebar).
- Create a folder here named **`Second Brain`**.

This is functionally identical to the Mac setup — same account, same sync, same files everywhere —
it just lives in the general iCloud Drive folder rather than Obsidian's private one. The only
practical difference: on a Mac opening the *same* vault later, you'd point Obsidian at this general
iCloud Drive location too (`~/Library/Mobile Documents/com~apple~CloudDocs/Second Brain`) instead of
the app-specific path, for the two machines to actually be sharing one vault. If you're setting up a
Windows machine as a companion to an *existing* Mac vault that already lives in the app-specific
container, look inside iCloud Drive for a folder Obsidian created (it sometimes surfaces there) before
assuming you need to move anything — but verify by checking file timestamps match, don't guess.

## 4. Lay out the folders

Inside `Second Brain\`, create:
```
Second Brain\
└── Vault\
    ├── Thinking\
    └── Doing\
        ├── 01 - Frameworks\
        ├── 02 - Examples\
        ├── 03 - Knowledge Base\
        │   └── People\
        └── 04 - Projects\
```

## 5. Drop in the starter files

Copy these from this skill's `assets\` folder into place (if a person, not Claude, is doing this by
hand, they were bundled alongside this guide):

| File | Goes to |
| --- | --- |
| `CLAUDE.md` | `Second Brain\CLAUDE.md` |
| `README - start here.md` | `Second Brain\README - start here.md` |
| `Map.md` | `Second Brain\Vault\Doing\Map.md` |
| `About Me.md` | `Second Brain\Vault\Doing\About Me.md` |
| `How to write a framework.md` | `Second Brain\Vault\Doing\01 - Frameworks\How to write a framework.md` |
| `Good and bad, side by side.md` | `Second Brain\Vault\Doing\02 - Examples\Good and bad, side by side.md` |
| `_Project Template.md` | `Second Brain\Vault\Doing\04 - Projects\_Project Template.md` |
| `Projects Index.md` | `Second Brain\Vault\Doing\04 - Projects\Projects Index.md` |

In `CLAUDE.md`, replace the `{{SECOND_BRAIN_PATH}}` placeholder near the top with the real path from
step 3, e.g. `C:\Users\<you>\iCloudDrive\Second Brain\`.

## 6. Open the vault in Obsidian

Obsidian → **Open folder as vault** → select `Second Brain\Vault` (not `Second Brain` itself — Obsidian
should only ever see the `Vault` folder). You should see `Thinking` and `Doing` in the left sidebar and
nothing else.

## 7. Install Claude Code

- **Claude desktop app (simplest, no terminal needed).** Download the Windows app from
  **claude.com/download**, sign in, and open its **Code** tab. Use its "open folder" action to point it
  at `Second Brain` — the parent folder, **not** `Vault`.
- **Claude Code CLI (for terminal users).** Claude Code now runs natively on Windows (no WSL needed). Open
  **PowerShell** and run Anthropic's native installer:
  ```powershell
  irm https://claude.ai/install.ps1 | iex
  ```
  (Or: `winget install Anthropic.ClaudeCode`.) Open a new terminal window and run `claude --version` to confirm.
  Git for Windows is optional. Launch it from the right folder every time (adjust the path to where your
  `Second Brain` folder is, see step 3):
  ```powershell
  cd "$HOME\iCloudDrive\Second Brain"
  claude
  ```
  The first time, `claude` opens a browser to sign in. Claude Code needs a paid Claude account (Pro, Max, Team
  or Enterprise) or Anthropic API access; the free claude.ai plan does not include it. WSL is still an option
  if you prefer a Linux shell. Install steps change, so check **code.claude.com/docs/en/setup** if anything
  here does not match what you see.

Either way, the folder you open Claude on is `Second Brain` — one level **above** the vault — so that
`CLAUDE.md` loads automatically at the start of every session.

## 8. Fill in About Me

Inside the Claude session, say:

> *"Read Vault/Doing/Map.md and Vault/Doing/About Me.md, then ask me the three questions you most need
> answered to be useful to me."*

Answer in plain English. When Claude asks a follow-up question, the setup is done.

## Verify it actually synced

Right-click the folder in File Explorer and check its iCloud status icon isn't stuck mid-sync. If
there's a Mac (or another PC) on the same account, confirm a newly edited note shows up there.

## Gotchas
- Point Claude at `Second Brain`, not `Second Brain\Vault`. Pointing it at `Vault` means `CLAUDE.md`
  never loads and every session starts with no conventions.
- If iCloud Drive doesn't appear in File Explorer's sidebar, it can take a few minutes after first
  sign-in, or a sign-out/sign-in in the iCloud app usually kicks it loose.
- Don't fight to replicate the exact Mac folder path (`iCloud~md~obsidian`). The general iCloud Drive
  folder does the same job and is the one Windows actually gives you cleanly.
