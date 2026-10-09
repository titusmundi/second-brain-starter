---
name: second-brain-setup
description: Scaffolds a fresh "Second Brain" Obsidian + Claude Code vault on a new Mac, Windows PC or Chromebook — the Thinking/Doing folder structure, the house CLAUDE.md conventions, and a Second Brain folder (iCloud-synced on Mac and Windows; stored in Linux on a Chromebook) that Claude Code loads automatically. Use this whenever the user wants to set up Obsidian to work with Claude Code, replicate their "second brain" or PKM (personal knowledge management) system on a new machine, start a fresh Obsidian vault an agent can read and maintain, or asks for a starter kit, template, or onboarding walkthrough for this setup — on macOS, Windows or ChromeOS. Also produces a standalone how-to guide (Mac, PC and Chromebook versions) that can be handed to someone doing the setup by hand, without Claude Code involved at all.
---

# Second Brain setup

Bootstraps the two-space vault system this skill is modeled on: `Thinking/` (the person's own notes,
untouched by any agent) and `Doing/` (a hierarchy an agent can navigate and maintain), synced via
iCloud so the same vault works from any device, with a `CLAUDE.md` that loads automatically every
session because Claude is launched one level above the vault, not inside it.

## Before doing anything: ask two questions

1. **Which OS is this for** — macOS, Windows or a Chromebook (ChromeOS, using its Linux environment)? If the user is asking on behalf of "a PC" or "my
   Windows laptop" while this session is running on a Mac (or vice versa), that's fine — you're
   producing files and instructions, not running the target OS.
2. **Is this to actually build the vault right now** (you have shell/file access to the target
   machine and iCloud is already signed in there), **or does the user just want the guide** to follow
   themselves, possibly later, possibly by hand? Don't assume — a lot of the value here is the
   standalone guide, and jumping straight to creating files when the user only wanted to read the
   guide is the wrong move.

## Path A: the user wants the guide

Read `references/mac-setup.md`, `references/windows-setup.md` or `references/chromebook-setup.md` (or several, if they want to compare or
this is going to someone else) and present it to them. These are self-contained — written so a person
with zero prior context can follow them without Claude Code at all — and cover: turning on iCloud
Drive, installing Obsidian, exactly which folder the vault goes in (and why the Mac and Windows
answers differ — Windows has no equivalent of Obsidian's macOS app-scoped iCloud container, so the
Windows guide uses the general iCloud Drive folder instead, and says so honestly rather than
pretending the paths match), installing Claude Code, and the folder layout to create. The Chromebook guide has
no iCloud at all: the vault lives in the Linux files, with backup or Google Drive options, and Obsidian and Claude Code
are installed inside Linux. It is drafted from the docs and one user's report and is marked as not yet fully verified.

If the user wants a document they can hand to someone else, give them the relevant guide as a file
(`references/mac-setup.md`, `references/windows-setup.md`, `references/chromebook-setup.md`, or the beginner PDF below) rather than only
pasting it into chat, and offer to put it into whatever format or tool they prefer to share.

For someone new to *both* tools (not just new to this vault's conventions), hand them
`assets/Getting Started with Claude and Obsidian.pdf` instead of the two OS reference guides above —
it's a plain-language install-and-orient walkthrough with no mention of the Thinking/Doing system,
built for a true beginner. The PDF is the shipped version. `scripts/build_beginner_guide.py` rebuilds the editable .docx source and `scripts/docx_to_pdf.py` exports it to the PDF (needs Google Chrome). The build script uses python-docx; this
environment had no Node/npm/pandoc/LibreOffice available, so it doesn't use the docx skill's usual
docx-js approach — check what's available before assuming either path).

## Path B: actually scaffold it

Do this only once you know **where** — confirm the exact target path with the user before writing
anything; don't guess at a path on their filesystem. Walk them through the OS-specific setup steps in
the relevant reference guide first (installing Obsidian, turning on iCloud Drive/iCloud for Windows or, on a
Chromebook, turning on Linux and choosing where the vault is backed up; confirming the target folder exists) — those steps involve OS settings and installers this skill can't
do for the user, so confirm each is actually done before moving on rather than assuming.

Once the target folder is confirmed:

1. **Create the folder tree.** Under the confirmed `Second Brain/` path:
   ```
   Second Brain/
   ├── CLAUDE.md
   ├── README - start here.md
   └── Vault/
       ├── Thinking/          (empty)
       └── Doing/
           ├── About Me.md
           ├── Map.md
           ├── 01 - Frameworks/
           │   └── How to write a framework.md
           ├── 02 - Examples/
           │   └── Good and bad, side by side.md
           ├── 03 - Knowledge Base/
           │   └── People/    (empty)
           └── 04 - Projects/
               ├── _Project Template.md
               └── Projects Index.md
   ```
   Use the Write tool to place each file straight from `assets/` at its target path (it creates
   intermediate directories, so there's no separate mkdir step needed) — copy the content verbatim
   except for the one substitution below.

2. **Fill in the one placeholder.** In the copied `CLAUDE.md`, replace `{{SECOND_BRAIN_PATH}}` with
   the real absolute path to the `Second Brain` folder you just created (the OS-specific reference
   guide shows the expected shape of that path for Mac, Windows and Chromebook; on a Chromebook it is
   inside the Linux home folder, for example `/home/<user>/Second Brain/`).

3. **Tell the user what to do by hand**, because these steps need a GUI, not a shell:
   - Open `Second Brain/Vault` (not `Second Brain`) as a vault in Obsidian.
   - Point Claude Code at `Second Brain` itself (one level *above* the vault) for future sessions —
     that's what makes `CLAUDE.md` load automatically.
   - Say the About-Me prompt from `README - start here.md` in a fresh Claude session on that folder,
     to fill in the one file that actually needs their own words.

4. **Don't personalize the templates yourself.** Leave `About Me.md`, `Projects Index.md`, and the
   `Constraints` section of `CLAUDE.md` (currently "no em-dashes" and "work/personal stay separate," a
   default pulled from the original setup this skill was modeled on) as generic placeholders. Those
   are the person's own conventions to write, not yours to infer or copy from anywhere.

## Judgment calls

- **If the user already has a Second Brain vault and wants a second machine to share it**, this is a
  sync-and-open task, not a scaffold task — don't recreate the folder tree, just walk them through
  getting the *existing* vault visible on the new machine (same iCloud account, same folder). Only
  fall back to full scaffolding if they actually want a second, independent vault.
- **If they want to fork this for someone else's use** (a teammate, a friend), the templates in
  `assets/` are already generic — no need to strip anything further. Just don't carry over any
  specifics from *this* conversation into their copy.
- **Keep it to the two questions above before writing files.** This skill would rather ask once than
  scaffold the wrong OS's paths or step on an existing vault.
