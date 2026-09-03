# Step 3 — Set up Git and push your code to GitHub

> **Goal of this page:** learn Git from zero — install it, configure it, save your work in commits, and push your CoppeliaSim Python code to GitHub. Both absolute-beginner paths and a quick cheatsheet are included.

---

## 1. What is Git? (30 seconds)

Git is a **version control system**. You can think of it as "super-save with time travel":

- Every time you **commit**, Git takes a snapshot of your project.
- You can go back to any snapshot, see what changed, or undo mistakes.
- You can **push** your snapshots to **GitHub** so your code is backed up and shareable.

```
Edit files ──► git add  (stage changes)
                 │
                 ▼
           git commit  (save a snapshot / "save point")
                 │
                 ▼
           git push    (upload snapshot to GitHub)
```

---

## 2. Install Git

| OS | How |
| -- | --- |
| **Windows** | Download from <https://git-scm.com/download/win> and run the installer (default settings are fine). This also installs **Git Bash** |
| **macOS** | Run `xcode-select --install` in Terminal, or `brew install git` if you use Homebrew |
| **Linux (Ubuntu/Debian)** | `sudo apt update && sudo apt install git` |

Check it works:

```bash
git --version
# git version 2.x.x
```

---

## 3. Configure Git (one time only)

Tell Git who you are — it gets written into every commit:

```bash
git config --global user.name  "Your Name"
git config --global user.email "your.email@example.com"
```

Optional but nice: set your default editor and branch name.

```bash
git config --global init.defaultBranch main
```

---

## 4. Create a GitHub repository

1. Log in to <https://github.com>.
2. Click the **+** icon (top right) → **New repository**.
3. Give it a name, e.g. `coppeliasim-tutorial`.
4. Leave it **empty** (don't tick "Add a README"), then click **Create repository**.
5. Copy the repository URL. It looks like:
   - HTTPS: `https://github.com/YOUR-USERNAME/coppeliasim-tutorial.git`
   - SSH: `git@github.com:YOUR-USERNAME/coppeliasim-tutorial.git`

> HTTPS is easiest for beginners — Git will ask for your GitHub username and a **PAT (personal access token)**, not your password, when you push. Create one at <https://github.com/settings/tokens> (scope: `repo`).

---

## 5. Path A — Start fresh in YOUR new folder

If you want a brand-new project on your computer:

```bash
# 1. create a folder and go inside it
mkdir coppeliasim-tutorial
cd coppeliasim-tutorial

# 2. turn this folder into a Git repository
git init

# 3. create your first file
echo "# my coppeliasim project" > README.md

# 4. put ALL files in the "staging area"
git add .

# 5. see what Git is about to commit (very useful!)
git status

# 6. save a snapshot
git commit -m "First commit: project readme"

# 7. rename the main branch (matches GitHub convention)
git branch -M main

# 8. link this folder to your GitHub repository
git remote add origin https://github.com/YOUR-USERNAME/coppeliasim-tutorial.git

# 9. upload everything to GitHub
git push -u origin main
```

✅ Done! Refresh your GitHub page — your files are there.

---

## 6. Path B — Use THIS tutorial repository

You are already inside a Git repository, so you can learn by doing:

```bash
# 1. look at what has changed
git status

# 2. check what a snapshot would contain
git diff

# 3. save everything ("stage" + "commit")
git add .
git commit -m "Add CoppeliaSim beginner tutorial and Python scripts"

# 4. link your local repo to YOUR GitHub repository
git remote add origin https://github.com/YOUR-USERNAME/coppeliasim-tutorial.git

# 5. upload
git push -u origin main
```

If the repository already has commits on GitHub, clone it instead and copy your files in:

```bash
git clone https://github.com/YOUR-USERNAME/coppeliasim-tutorial.git
```

---

## 7. The 3-command habit

From now on, after finishing a piece of work:

```bash
git add .
git commit -m "Describe what you changed"
git push
```

Commit **often** (a commit per small step, not per month) — e.g.:

```bash
git commit -m "Add first Python simulation script"
git commit -m "Move cube in a circle, not a square"
git commit -m "Add Git setup guide"
```

---

## 8. Why `.gitignore` matters

Your folder contains files that should **not** be uploaded (virtual environments, caches, OS junk). The `.gitignore` file in this repo tells Git to ignore them:

```gitignore
# Python virtual environment (never upload this!)
.venv/
venv/

# Python bytecode cache
__pycache__/
*.py[cod]

# Editor / OS junk
.vscode/
.idea/
.DS_Store
Thumbs.db
```

Check that Git is really ignoring them:

```bash
git status          # .venv/ and __pycache__/ should NOT appear
git add .           # they will never be added
```

> 🧠 **Why?** A virtual environment contains thousands of files, is different on every computer, and can be re-created anytime with `python -m venv .venv`. Uploading it is a beginner's classic mistake.

---

## 9. Everyday Git cheatsheet

| Command | What it does |
| ------- | ------------ |
| `git status` | Show changed files |
| `git add .` | Stage all changes |
| `git add file.py` | Stage one file |
| `git commit -m "msg"` | Save a snapshot |
| `git log --oneline` | Show commit history |
| `git diff` | Show uncommitted changes |
| `git push` | Upload your commits |
| `git pull` | Download new commits from GitHub |
| `git restore file.py` | Discard changes in one file (careful!) |
| `git reset --soft HEAD~1` | Undo the last commit, keep the changes |
| `git branch` | List branches |
| `git checkout -b my-experiment` | Create + switch to a branch |
| `git merge my-experiment` | Merge a branch into the current one |

---

## 10. Common beginner mistakes

| Mistake | Fix |
| ------- | --- |
| Forgetting `git add .` before commit | You committed nothing → run `git add .` and `git commit` again |
| Committing `.venv/` | Add it to `.gitignore` (already done here) |
| `push` fails with *"failed to push some refs"* | Someone else pushed → run `git pull` first, then `git push` |
| Using your GitHub password | GitHub requires a **personal access token** over HTTPS |
| Huge commits of binary files | Keep generated files (e.g. `.ttt` backups, videos) out of Git |

---

## 11. Git + this tutorial = your robotics lab

A nice practical pattern as you learn:

```
├── my_first_project/
│   ├── README.md            ← what the project does
│   ├── requirements.txt     ← pip install -r requirements.txt
│   ├── .gitignore           ← ignore .venv/, __pycache__/ …
│   └── scripts/
│       ├── 00_hello_coppelia.py
│       └── 01_move_robot.py
```

Every step of your CoppeliaSim learning journey becomes a commit — and your history on GitHub tells the story of everything you learned. 🚀
