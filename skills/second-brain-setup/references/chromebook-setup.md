# Second Brain setup — Chromebook (ChromeOS, using Linux)

A from-scratch walkthrough: Obsidian + Claude Code on a Chromebook, set up the way this system expects.
No prior context assumed. Roughly 30 minutes, most of it waiting on installers.

> **Status: drafted from the official docs and one user's report; not yet run end to end on a Chromebook.**
> A reader (Kenny) set the kit up on a Chromebook through Linux and asked for this version. If a step does not
> match what you see, please open an issue on the repository and say what you saw. Parts marked *(unverified)*
> are the ones most likely to need a fix.

**How a Chromebook differs from a Mac or Windows PC.** ChromeOS can run a small Linux computer inside it
(Google calls it the "Linux development environment"). Obsidian and Claude Code both run there. Two things change:

1. **There is no iCloud.** The Mac and Windows guides use iCloud to keep the vault in sync. Here the vault lives in
   the Linux part of your Chromebook, and step 3 explains your options for backing it up or syncing it.
2. **You use a terminal for a few steps.** The Terminal app on a Chromebook is the Linux one; you paste short
   commands into it. Each command is shown in a box you can copy.

Where you'll end up (inside Linux, your "home" folder is `~`):
```
~/Second Brain/
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

## 0. Check your Chromebook can do this

- It must support Linux apps. Most Chromebooks from 2019 on do. School and work Chromebooks often have Linux
  switched off by the administrator; if you do not see the setting in step 1, that is why, and this guide will not work
  on that device.
- Claude Code asks for at least 4 GB of memory. Leave a few gigabytes of free storage for Linux and the two apps.
- You need a paid Claude account (Pro, Max, Team or Enterprise) or Anthropic API access to use Claude Code. The free
  claude.ai plan does not include it.

## 1. Turn on Linux

Settings → **About ChromeOS** → **Developers** → **Linux development environment** → **Set up** (on some
versions it is under Settings → Advanced → Developers). Follow the prompts; accept the default username and disk size.
It takes a few minutes. When it finishes, a **Terminal** window opens. (Later you can open it from the launcher by
searching "Terminal".)

In that Terminal, update the system once. Copy, paste, press Enter, and enter "Y" if asked:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git
```

## 2. Install Obsidian

Obsidian has no Chromebook app, but it does run in Linux. Pick **one** of these. Obsidian's own install page documents
three Linux routes (Snap, AppImage and Flatpak); Flatpak and AppImage are the two that suit a Chromebook's Debian-based Linux.
Flatpak is shown first because it can be updated with a single command.

**Option A: Flatpak** *(unverified on ChromeOS)*
```bash
sudo apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install -y flathub md.obsidian.Obsidian
```
Restart Linux once (close the Terminal, then in the launcher right-click Terminal → **Shut down Linux**, and reopen it),
then start Obsidian with:
```bash
flatpak run md.obsidian.Obsidian
```

**Option B: AppImage.** Download the Linux AppImage from **obsidian.md/download** (for most Chromebooks the
x86_64 / "Linux" one; a Chromebook with an ARM chip needs the arm64 one). Then, from the folder you saved it in:
```bash
sudo apt install -y libnss3-dev
chmod u+x Obsidian-*.AppImage
./Obsidian-*.AppImage --no-sandbox
```
Obsidian's install page says that on Chromebooks `libnss3-dev` must be installed, otherwise you get a "libnss3.so"
error. If it complains about FUSE, install the package it names (usually `libfuse2`).

Either way, when Obsidian starts it asks you to create or open a vault. **Cancel that for now**; you are about to
point it at a specific folder.

## 3. Decide where the vault lives (and how it is backed up)

Create the folder in Linux, in your home folder: `~/Second Brain`. (In the ChromeOS **Files** app it appears under
**Linux files**.) Then choose how you will keep a copy safe, because a Chromebook has no iCloud:

- **Simplest (recommended to start): keep it in Linux files and back it up.** Settings → **About ChromeOS** →
  **Developers** → **Linux development environment** → **Backup & restore** *(unverified wording)* makes a backup of the
  whole Linux environment, including your vault. Do it after any big session. This does not sync to other devices.
- **Sync through Google Drive** *(unverified for Obsidian and Claude Code)*. In the Files app, create a folder in Google Drive
  called `Second Brain`, right-click it, choose **Share with Linux**, and use the path under `/mnt/chromeos/GoogleDrive/MyDrive/Second Brain` in
  place of `~/Second Brain` everywhere below. Run `ls /mnt/chromeos` first to confirm the exact path on your device. Drive
  folders can be slower than Linux files and may not notice changes made on another device straight away; test with a
  throw-away note before trusting it.
- **Git** (for people who already use it): make `~/Second Brain` a repository and push it to a private repository on
  GitHub. Not covered here.

The rest of this guide writes `~/Second Brain`; substitute your chosen folder if you picked Drive.

## 4. Get the starter files and lay out the folders

In the Terminal:
```bash
cd ~
git clone https://github.com/titusmundi/second-brain-starter.git
mkdir -p "$HOME/Second Brain/Vault/Thinking" \
         "$HOME/Second Brain/Vault/Doing/01 - Frameworks" \
         "$HOME/Second Brain/Vault/Doing/02 - Examples" \
         "$HOME/Second Brain/Vault/Doing/03 - Knowledge Base/People" \
         "$HOME/Second Brain/Vault/Doing/04 - Projects"
```
Then copy the starter files into place:
```bash
A="$HOME/second-brain-starter/skills/second-brain-setup/assets"
B="$HOME/Second Brain"
cp "$A/CLAUDE.md" "$B/CLAUDE.md"
cp "$A/README - start here.md" "$B/README - start here.md"
cp "$A/Map.md" "$B/Vault/Doing/Map.md"
cp "$A/About Me.md" "$B/Vault/Doing/About Me.md"
cp "$A/How to write a framework.md" "$B/Vault/Doing/01 - Frameworks/"
cp "$A/Good and bad, side by side.md" "$B/Vault/Doing/02 - Examples/"
cp "$A/_Project Template.md" "$A/Projects Index.md" "$B/Vault/Doing/04 - Projects/"
```
In `CLAUDE.md`, replace the `{{SECOND_BRAIN_PATH}}` placeholder near the top with the real path:
```bash
sed -i "s|{{SECOND_BRAIN_PATH}}|$HOME/Second Brain/|" "$HOME/Second Brain/CLAUDE.md"
```
(If you used a Google Drive folder in step 3, put that path in place of `$HOME/Second Brain/`.)

## 5. Open the vault in Obsidian

Start Obsidian (step 2) → **Open folder as vault** → choose `Second Brain/Vault` inside **Linux files** (not `Second Brain` itself;
Obsidian should only ever see the `Vault` folder). You should see `Thinking` and `Doing` in the left sidebar and
nothing else.

## 6. Install Claude Code

On a Chromebook use the **command-line version** in the Linux Terminal. (Anthropic also publishes a desktop app for
Debian-based Linux, in beta, but its notes say the Cowork feature is not expected to work on ChromeOS, and it has not been tried
here.) Install it with Anthropic's installer, which does not need Node.js:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
It prints no progress while it downloads. When it finishes, close the Terminal, open it again, and check:
```bash
claude --version
```
A version number means it worked. If it says "command not found", the install folder is not on your path yet;
see **code.claude.com/docs/en/troubleshoot-install**. Then start it **from the right folder**, every time:
```bash
cd ~/"Second Brain"
claude
```
The first time, it asks you to sign in through a web page. If the page does not open by itself, copy the link it prints into
the Chrome browser *(unverified)*, sign in, and paste the code back into the Terminal if it asks. Install steps change, so
check **code.claude.com/docs/en/setup** if anything here does not match what you see.

The folder you open Claude on is `Second Brain`, one level **above** the vault, so that `CLAUDE.md` loads automatically
at the start of every session. Obsidian and Claude are deliberately pointed at two different levels of the same tree;
that is not a mistake to fix.

## 7. Fill in About Me

Inside the Claude session, say:

> *"Read Vault/Doing/Map.md and Vault/Doing/About Me.md, then ask me the three questions you most need
> answered to be useful to me."*

Answer in plain English. When Claude asks a follow-up question, the setup is done.

## Gotchas
- **Two windows, one folder.** Obsidian (a window) and Claude Code (in the Terminal) both work on the same files.
  Obsidian shows changes Claude makes within a moment.
- **Point Claude at `Second Brain`, not `Second Brain/Vault`.** Pointing it at `Vault` means `CLAUDE.md` never loads and
  every session starts with no conventions.
- **If something seems frozen,** shut Linux down (launcher → right-click Terminal → **Shut down Linux**) and reopen it.
- **Back up.** Without iCloud, nothing is syncing your vault for you unless you set up one of the options in step 3.
- **Files app.** Your vault shows under **Linux files** in the ChromeOS Files app. Treat that copy as the real one, and
  do not keep a second copy elsewhere, or you will not know which is current.
- **Just want to read the steps without Claude?** Everything above works by hand; Claude Code is only needed in step 6.
