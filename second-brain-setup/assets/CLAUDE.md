# Conventions for this root

This file sits at `{{SECOND_BRAIN_PATH}}`, the folder Claude Code is launched from, so it loads at
the start of every session. It governs the vault at `Vault/` **and** anything else kept here later
(code, scripts, exports). Read `Vault/Doing/Map.md` next; it says what lives where.

```
Second Brain/
├── CLAUDE.md      <- this file
├── Vault/         <- the knowledge layer. Open THIS in Obsidian
│   ├── Thinking/  <- mine
│   └── Doing/     <- yours
└── ...            <- add project folders here as you get them
```

## The two spaces

- **`Vault/Thinking/`** is mine. My own notes, in my own words, in whatever shape suits me. There is
  no house format here, so do not impose one or tidy it. **Never write here unless I explicitly ask.**
  If you do draft something for this folder, say so clearly, so I always know which words are mine.
- **`Vault/Doing/`** is yours to navigate and maintain. A top-down hierarchy with the context you need
  to do real work.

## Working style

- I drive in plain English. You write and edit the `.md` files. I should rarely hand-edit structure.
- Explain in small steps and confirm between them. Do not deliver one large batch of changes.
- Stop and confirm before anything irreversible or outward-facing.
- Verify before claiming something is done. If you skipped a check, say so.
- Link liberally with `[[wikilinks]]`. Everything should be reachable from `Vault/Doing/Map.md`.

## The update rule

The biggest failure mode is this vault going stale. **Write things down as they happen, without being
asked.** I should never have to say "add that to the notes."

| What happened | Where it goes |
| --- | --- |
| A decision was made, with a reason | the project note's Decisions log, dated |
| A process changed, or a new one emerged | `Vault/Doing/01 - Frameworks/` |
| Output I judged clearly good or clearly bad | `Vault/Doing/02 - Examples/` |
| A reference fact worth keeping | `Vault/Doing/03 - Knowledge Base/` |
| **I named a person and said what they do** | **`Vault/Doing/03 - Knowledge Base/People/`, one note each** |
| A workstream started, finished, or was re-planned | `Vault/Doing/04 - Projects/` |
| An idea raised but not acted on | the Parking lot section of the relevant note |
| A gotcha, or a "wish I had known that" | the Gotchas section of the relevant note |

**The people rule is not optional.** If I mention someone and explain their role, who they report to,
what they own, or what they need from me, **write it down immediately** as a one-person note and link
it. If I explain the same person twice, that is a failure of this file, not of my memory. Keep those
notes short: role, what they own, what they need from me, what I am waiting on from them.

Rules of thumb:
- **Capture at the moment it happens**, not at the end. An unwritten decision is a lost decision.
- **Summarize at the end of every session:** one or two lines on what was written down, or an honest
  "nothing durable this session."
- **When in doubt, write it.** A slightly over-full vault is cheap. A forgotten decision is expensive.
- **Never write a secret's value.** Record only that it exists and where it lives.
- **Convert relative dates to absolute ones.** "Next Thursday" becomes the actual date.

## Note size

- **One topic per note.** If a note needs the word "and" to describe it, it is two notes. That is the
  only reason to split something.
- **Length follows the complexity of the topic.** A complicated thing gets a long note, and that is
  correct. **Never cut detail to make a note shorter.**
- **Long notes open with a state-of-play summary**, three to six lines: what this is, where it stands,
  what is next. That is what makes a long note usable, and it costs no detail.

## Frontmatter
- Thinking notes: `type: thinking`, `tags: [thinking]`
- Projects: `type: project`, `status`, `phase`, `tags: [project]`
- Frameworks: `type: framework`, `tags: [framework]`
- Knowledge Base: `type: reference`, `tags: [reference]`

## Constraints
- Work and personal stay in separate vaults. Never mix.
- No em-dashes in prose. Use commas, colons, semicolons, or parentheses.
