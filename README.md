# Second Brain starter

A small kit that sets up a "second brain" you can work with an AI agent: an [Obsidian](https://obsidian.md) vault that
[Claude Code](https://www.anthropic.com/claude-code) can read, write and keep up to date, with one simple rule at its heart:
**your own thinking stays yours, and the agent maintains the rest.**

I built it after setting up my wife with Claude Code and Obsidian. In an hour she had a working AI environment, and by
mid-afternoon she had built the software her small business needed. This is the set-up behind that story.

## What you get

- **A Claude Code skill** (`second-brain-setup`) that scaffolds the vault on a new Mac, Windows PC or Chromebook, or just hands you a
  step-by-step guide to do it by hand.
- **The two-space structure:**
  - `Thinking/` is yours. Your notes, in your words. The agent never writes there unless you ask.
  - `Doing/` is the agent's. A top-down hierarchy (frameworks, examples, knowledge base, projects) it navigates and maintains.
- **A `CLAUDE.md`** that loads automatically every session, so the agent knows how you work: small steps, confirm before
  anything irreversible, write things down as they happen, never record secrets.
- **Starter files:** a map, a blank "About Me", a project template, and short notes on how to write a framework and good
  versus bad examples.
- **A plain-language beginner guide** (`Getting Started with Claude and Obsidian.pdf`) for someone new to both tools, in the
  skill's `assets/` folder (`skills/second-brain-setup/assets/`). It does not mention the Thinking/Doing system at all.

## What you need

- A Mac or a Windows PC with iCloud Drive turned on (the guides explain why the Mac and Windows folder paths differ), **or a
  Chromebook** that can run Linux apps (see the Chromebook guide; there is no iCloud there, so it also covers backup).
- [Obsidian](https://obsidian.md). Free to use, including for work; Obsidian offers an optional paid commercial license
  and paid Sync and Publish services, none of which this kit needs. Check their current terms.
- [Claude Code](https://code.claude.com/docs/en/setup) (the desktop app or the command line). It requires a paid Claude
  account (Pro, Max, Team or Enterprise) or Anthropic API access; the free claude.ai plan does not include it. This kit does
  not provide that.

## Install

**Option A: as a Claude Code plugin** (one command, and you get updates). In a terminal:

```bash
claude plugin marketplace add titusmundi/second-brain-starter
claude plugin install second-brain-starter@titusmundi
```

Then start Claude Code and say something like: *"Set up a second brain for me."*

**Option B: copy the skill by hand.**

1. Download or clone this repository.
2. Copy the `skills/second-brain-setup` folder into your personal Claude Code skills folder, which is the `.claude/skills/`
   folder inside your user folder (on a Mac: `~/.claude/skills/`).
3. Start Claude Code and say: *"Set up a second brain for me."*

Either way, the skill first asks which operating system you use and whether you want it to build the vault now or give you
the guide to follow yourself.

Prefer no Claude Code at all? Open `skills/second-brain-setup/references/mac-setup.md`, `windows-setup.md` or
`chromebook-setup.md` and follow it by hand, or hand the beginner guide to someone who is new to all of this.

## Make it yours

The starter `CLAUDE.md` is a set of defaults, not commandments. Two lines in its "Constraints" section ("no em-dashes in prose"
and "work and personal stay in separate vaults") are the author's own preferences; change or delete them. The skill is built to
leave `About Me.md`, the project index and those constraints for you to write.

## Good to know

- **Your notes stay on your machine** and in the cloud service you choose to sync with. The skill does not send your vault
  anywhere on its own. What Claude Code reads is governed by Anthropic's terms and your settings; read them.
- **Chromebook:** the guide is new and has not yet been run end to end by its author; steps marked *(unverified)* may need
  a fix. A reader set the kit up on a Chromebook through Linux and asked for it. Please open an issue with what you saw.
- **Windows:** Obsidian's app-specific iCloud folder only exists on macOS. The Windows guide uses the general iCloud Drive
  folder instead and says so. If you hit a snag, please open an issue.
- **Not affiliated.** This is an independent project. Obsidian and Claude are products of their respective owners, and this
  kit is not affiliated with or endorsed by Obsidian or Anthropic.
- **No warranty.** See the license.

## License

MIT. See [LICENSE](LICENSE).

## Credits

Published by Titus Mundi LLC. Built by JC Titus with Claude. Part of a set of small experiments run in the open under Titus Mundi.
