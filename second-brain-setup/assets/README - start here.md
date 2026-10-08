# Start here

You are looking at an empty second brain. Five minutes to set up.

## What you just extracted

```
Second Brain/
├── CLAUDE.md      <- teaches Claude the conventions. Loads automatically
├── Vault/         <- the notes. Open THIS one in Obsidian
│   ├── Thinking/  <- yours
│   └── Doing/     <- the agent's
└── ...            <- room for project folders later, if you have them
```

Two folders, two tools: **Obsidian opens `Second Brain/Vault`. Claude opens `Second Brain`.** That is
the only thing to keep straight, and there is a reason for it below.

## Setup

**1. Put the folder somewhere synced**, e.g. inside your iCloud Drive. The exact path differs by OS:
see `mac-setup.md` or `windows-setup.md` (whichever came with this) for the walkthrough.

That is it for file wrangling. Nothing to create, nothing to rename, nothing to move around inside.

**2. Open the vault in Obsidian.**

Obsidian → **Open folder as vault** → pick `Second Brain/Vault`.

You should see two folders in the sidebar: `Thinking` and `Doing`. That is the whole idea, on screen.

**3. Open `Doing/Map.md` and read it.** That is your index; it explains the rest.

**4. Point Claude at `Second Brain`** — the level *above* the vault, not the vault itself.

- **Desktop app:** open `Second Brain`.
- **Terminal:** `cd "Second Brain"` then `claude`.

Either works; nothing here depends on which you use.

> **Why the level above?** Two reasons. `CLAUDE.md` sits at `Second Brain/`, so launching there means
> it is read at the start of every session and you never have to explain your conventions again. And
> it leaves room to drop project folders next to the vault later, so Claude can read your notes and
> edit your code in the same session.

**5. Ask it this:**

> *"Read Vault/Doing/Map.md and Vault/Doing/About Me.md, then ask me the three questions you most need
> answered to be useful to me."*

Answer in plain English and let it write `About Me.md` for you. That file is the highest-value thing in
the vault and it is the only one you need to fill in today.

**When Claude asks you a question back, you are done.**

## The idea in one line

Two spaces, because two readers want opposite things. `Thinking/` is yours: your notes, in your own
words, in whatever shape you like. `Doing/` is the agent's: a hierarchy with the context it needs to
do real work.

## What to do this week

Nothing structural, and nothing in `Thinking/` unless you feel like it. The one thing worth doing is a
single **framework** in `Doing/01 - Frameworks/` for the task you have explained to someone else more
than twice. That is the note that starts paying you back immediately.

## What not to do

- Do not port everything in on day one.
- Do not build folders you will not use. Delete the ones that do not fit your work.
- Do not clip and paste into `Thinking/`. If it is not in your words, it is not a thinking note.
- Do not mix work and personal. Separate vaults, always.

## Where the detail lives

- `CLAUDE.md` teaches Claude the conventions automatically. Read it once so you know what it will do.
  It also carries a couple of personal defaults (no em-dashes, work/personal stay separate) — edit the
  **Constraints** section to your own taste; nothing else in this system depends on those two rules.
- `Vault/Doing/Map.md` is the index of everything.
- `Vault/Doing/01 - Frameworks/How to write a framework.md` explains the folder that does the most work.
