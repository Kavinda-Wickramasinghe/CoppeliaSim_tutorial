# 🚀 CoppeliaSim for Complete Beginners — The One Guide

This guide takes you from **zero** to:

1. Running CoppeliaSim (a robot simulator program)
2. Controlling robots with **Python**
3. Saving your code online with **GitHub**

You do **not** need to know robotics or programming. Every step tells you exactly what to click or type.

---

## How to use this guide

The steps are a little different on Windows and Mac. Find yours and follow only that one:

| Symbol | Your computer |
| ------ | ------------- |
| 🪟 **Windows** | Most laptops and PCs (Windows 10 or 11) |
| 🍎 **macOS** | Apple computers (MacBook, iMac) |

Rules that always apply:

- **Type the commands exactly as shown**, then press **Enter**.
- **Copy-paste is fine** (Ctrl+C / Ctrl+V on Windows, Cmd+C / Cmd+V on Mac).
- If something goes wrong, jump to **Part 8 — Problems & Fixes**.

## What you need before starting

- [ ] A computer with **Windows 10/11** or **macOS**
- [ ] Internet (we download 2 things: CoppeliaSim + one Python package)
- [ ] About 30–45 minutes

---

# PART 1 — Install CoppeliaSim ⏱️ 5 minutes

CoppeliaSim is a program that shows robots in 3D and simulates them. The free version for learning is called **CoppeliaSim Edu**.

## 1.1 Download it

**Step 1.** Open your browser and go to:

**<https://www.coppeliarobotics.com/downloads>**

**Step 2.** Scroll to the section called **CoppeliaSim Edu**.

**Step 3.** Click the button for your computer:

| Your computer | Click on | You get a file like |
| ------------- | -------- | ------------------- |
| 🪟 Windows | **Windows** (installer package) | `CoppeliaSim_Edu_V4_10_0_Setup.exe` |
| 🍎 macOS | **macOS** | `CoppeliaSim_Edu_V4_10_0_Mac.dmg` |

> Don't worry about the exact version number. Any version **4.4 or newer** works with this guide.

> 🍎 **Mac only — which macOS button do I click?**
> Click the **Apple logo** (top-left corner of your screen) → **About This Mac**.
> - If it says chip **Apple M1 / M2 / M3 / M4** → download the **Apple Silicon** version.
> - If it says **Intel** → download the **Intel** version.

## 1.2 Install it

**Step 1.** Wait for the download to finish. The file is in your **Downloads** folder.

**Step 2.** Follow only your system:

### 🪟 Windows

1. Double-click the `.exe` file you downloaded.
2. If Windows asks *"Do you want to allow this app to make changes?"* → click **Yes**.
3. Click **Next** → **Next** → **Install** → **Finish**. (Default settings are fine.)

### 🍎 macOS

1. Double-click the `.dmg` file you downloaded. A window opens with two icons.
2. **Drag the CoppeliaSim icon onto the Applications folder.** This copies the app into your Applications.
3. Close the window.

> 🍎 **If macOS says "unidentified developer" or blocks the app:**
> Don't panic. Open your **Applications** folder, **right-click** (or Ctrl+click) the CoppeliaSim icon → click **Open** → click **Open** again. You only need to do this the first time.

## 1.3 Open CoppeliaSim

### 🪟 Windows
Press the **Windows key**, type `CoppeliaSim`, press **Enter**.

### 🍎 macOS
Press `Cmd + Space`, type `CoppeliaSim`, press **Enter** (or open the **Applications** folder and double-click it).

**What you should see:** a 3D scene opens with a small robot in the middle. That means it works! 🎉

## 1.4 The 4 buttons you need

At the top of the CoppeliaSim window:

| Button | What it does |
| ------ | ------------ |
| ▶️ **Play** | Starts the simulation (robot starts moving) |
| ⏸ **Pause** | Freezes everything |
| ⏹ **Stop** | Resets everything back to the start |
| 🖱️ **Drag with left mouse button** | Rotates the camera around the scene |

**Try it now:** click ▶️ Play → watch the robot → click ⏹ Stop.

## 1.5 Turn on the "bridge" to Python (one click)

Python talks to CoppeliaSim through a built-in helper called the **ZMQ remote API server**. It usually starts by itself, but let's check once:

**Step 1.** In the CoppeliaSim menu bar (top of the window) click:

**`Modules → Connectivity → ZMQ remote API server`**

**Step 2.** Look at the bottom of the window (the console area). You should see a line like:

```
ZMQ remote API server started
```

That's it. **Keep CoppeliaSim open** — we come back to it in Part 3.

---

# PART 2 — Get the tutorial files + Python ⏱️ 10 minutes

## 2.1 Open a terminal

A **terminal** is a window where you type commands to your computer. Every computer has one:

- 🪟 **Windows:** press the **Windows key**, type `powershell`, press **Enter**.
- 🍎 **macOS:** press **Cmd + Space**, type `terminal`, press **Enter**.

You should see a small window with a blinking cursor, waiting for you to type. That's the terminal. ✅

## 2.2 Check that Python is installed

Python is the programming language we use to control the robots.

**Step 1.** In the terminal, type this and press **Enter**:

```bash
python --version
```

**Step 2.** Read the answer:

- If you see something like `Python 3.11.5` → Python is ready. Skip to 2.3.
- If you see an error, or `"python" not found` → try `python3 --version`.
- If **both** fail → install Python now:

### 🪟 Windows — install Python

1. Go to <https://www.python.org/downloads/> and click the big yellow **Download Python 3.x.x** button.
2. Run the downloaded file.
3. ⚠️ **MOST IMPORTANT STEP:** on the first screen, **tick the checkbox "Add python.exe to PATH"** (bottom of the window). If you forget this, nothing will work.
4. Click **Install Now** → wait → **Close**.
5. **Close your terminal and open a new one** (the old one doesn't know about Python yet), then try `python --version` again.

### 🍎 macOS — install Python

1. Go to <https://www.python.org/downloads/> and click the big yellow **Download Python 3.x.x** button.
2. Run the downloaded `.pkg` file → **Continue** → **Continue** → **Install**.
3. Try `python3 --version` in your terminal.

> On Mac you may always need to type `python3` instead of `python`. That's normal — this guide shows `python`, just add the `3` if needed.

## 2.3 Get the tutorial files onto your computer

All tutorial files live on GitHub here:

**<https://github.com/Kavinda-Wickramasinghe/CoppeliaSim_tutorial>**

**Step 1.** Open that link in your browser.

**Step 2.** Click the green **`<> Code`** button → click **Download ZIP**.

**Step 3.** Open the downloaded ZIP file:

- 🪟 Windows: right-click the ZIP (in Downloads) → **Extract All...** → **Extract**
- 🍎 macOS: double-click the ZIP — it extracts by itself

**Step 4.** In the terminal, go into that folder. Type the command for your system:

```bash
# 🪟 Windows:
cd Downloads\CoppeliaSim_tutorial-main

# 🍎 macOS:
cd Downloads/CoppeliaSim_tutorial-main
```

> `cd` means "**c**hange **d**irectory" = "go into this folder".
> Tip: type `cd Down` and press **Tab** — the terminal fills in the rest of the name for you.

**Check it worked:** type `dir` (Windows) or `ls` (Mac) and press Enter. You should see `GUIDE.md`, `scripts`, `requirements.txt`.

## 2.4 Make a private "room" for Python (one time only)

We create a folder called `.venv` (a **virtual environment**). It keeps this tutorial's Python packages separate from everything else on your computer, so nothing can break.

**Step 1.** In the terminal (inside the tutorial folder), type:

```bash
python -m venv .venv
```

Nothing much seems to happen — it just creates a hidden `.venv` folder. Now we "enter" it:

**Step 2.** Activate it — different on Windows and Mac:

### 🪟 Windows

```powershell
.venv\Scripts\activate
```

> ⚠️ If you see red text saying *"running scripts is disabled"*: PowerShell is being careful. Fix it with this one command, then try again:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 🍎 macOS

```bash
source .venv/bin/activate
```

**What success looks like:** the start of your terminal line now shows `(.venv)`, like:

```
(.venv) C:\Users\you\CoppeliaSim_tutorial-main>
```

Everything you install now stays inside this project. ✅

> You need to activate it **every time you open a new terminal** (it turns off when you close the window).

## 2.5 Install the talking package (one command)

This installs `coppeliasim-zmqremoteapi-client` — the small Python package that lets Python "call" CoppeliaSim:

```bash
python -m pip install -r requirements.txt
```

Wait until it finishes (some lines scroll by — that's normal).

**Check it worked:**

```bash
python -c "from coppeliasim_zmqremoteapi_client import RemoteAPIClient; print('OK')"
```

If it prints `OK` → you are ready. ✅

---

# PART 3 — First connection test ⏱️ 2 minutes

**Step 1.** Look at CoppeliaSim. Is it still open? Good. (If not, open it — see Part 1.3.)

**Step 2.** In your terminal (the one showing `(.venv)`), type:

```bash
python scripts/00_hello_coppelia.py
```

**Step 3.** You should see:

```
Connected to CoppeliaSim!
Simulation time: 0.00 s
Found 21 shape object(s) in the scene.
  - cuboid
  - ...
```

If you see `Connected to CoppeliaSim!` → **Python and CoppeliaSim are talking!** 🎉

> 🟢 **The golden rule:** CoppeliaSim must be **open before** you run any Python script. If you close CoppeliaSim, Python has nobody to talk to.

---

# PART 4 — Your first simulation: a moving cube ⏱️ 5 minutes

**Step 1.** Keep CoppeliaSim open.

**Step 2.** In the terminal, type:

```bash
python scripts/01_first_simulation.py
```

**Step 3.** Look at the **CoppeliaSim window**: a **cube appears and moves in a circle** for 5 seconds. Meanwhile the terminal prints its position:

```
t = 0.00 s  ->  cube at (0.000, 0.500, 0.300)
t = 0.05 s  ->  cube at (0.050, 0.499, 0.300)
...
Simulation finished.
```

After it ends, the cube (named `MyFirstCube`) stays in the scene so you can look at it.

## 4.1 What just happened (simple version)

Think of it as a phone call:

| Code | Plain English |
| ---- | ------------- |
| `client = RemoteAPIClient()` | **Dial the phone** — connect to CoppeliaSim |
| `sim = client.require("sim")` | **Get the remote control** — now `sim` is the remote |
| `sim.setStepping(True)` | **"Don't move until I say so"** — simulation waits for us |
| `sim.step()` | **"Move one tiny step now"** |

Then the loop runs 100 times, each time telling the cube where to go:

```python
sim.setObjectPosition(cube, sim.handle_world, [x, y, z])
```

That's it. You are a robot programmer now. 🎓

## 4.2 The 5 commands you'll use most

| Command | Remember it as |
| ------- | -------------- |
| `sim.startSimulation()` | Press ▶️ Play |
| `sim.stopSimulation()` | Press ⏹ Stop |
| `sim.createPrimitiveShape(...)` | "Make me a box" |
| `sim.setObjectPosition(...)` | "Cube, go there" |
| `sim.step()` | "Take one step" |

---

# PART 5 — Your first robot arm: spin a joint ⏱️ 5 minutes

A **joint** is a motor that rotates — every real robot arm, wheel, and gripper is built from joints.

**Step 1.** CoppeliaSim still open? Yes.

**Step 2.** Run:

```bash
python scripts/02_spin_the_joint.py
```

**Step 3.** In CoppeliaSim: a **rod appears and spins in circles** like a clock hand, for 5 seconds. The terminal prints the angle:

```
t = 0.00 s  ->  joint angle = 0.00 rad
t = 0.05 s  ->  joint angle = 0.10 rad
...
```

## 5.1 The 3 lines that do all the work

```python
sim.createJoint(sim.joint_revolute, sim.jointmode_kinematic, 0)  # 1. make a hinge
sim.setObjectParent(arm, joint, True)                            # 2. stick the arm on it
sim.setJointTargetVelocity(joint, 2.0)                           # 3. spin at speed 2
```

Real robotics, three lines. 🤖

---

# PART 6 — Change the numbers (learn by playing) 🧪 5 minutes

**Step 1.** Open `scripts/01_first_simulation.py` in any editor:

- 🪟 Windows: **Notepad** (right-click the file → Open with → Notepad)
- 🍎 macOS: **TextEdit**

(Better both: install the free **VS Code** editor from <https://code.visualstudio.com>.)

**Step 2.** Change **one** number:

| Change this | To this | What happens |
| ----------- | ------- | ------------ |
| `0.5 * math.sin(...)` | `1.0 * math.sin(...)` | Circle gets bigger |
| `2.0 * t` | `4.0 * t` | Cube moves faster |
| `DURATION = 5.0` | `DURATION = 10.0` | Runs for 10 seconds |

**Step 3.** Save the file (Ctrl+S on Windows / Cmd+S on Mac) and run it again:

```bash
python scripts/01_first_simulation.py
```

> Break it, fix it, change it — **that's how you learn.** (The script rebuilds the cube if needed, so running it again is always safe.)

---

# PART 7 — Save your work with Git & GitHub ⏱️ 10 minutes

**Why?** Git is like **save points in a video game** — every `commit` is a save point. GitHub is your **cloud backup**, so your code can never be lost.

This project already has a GitHub home:

**<https://github.com/Kavinda-Wickramasinghe/CoppeliaSim_tutorial>**

## 7.1 Install Git

### 🪟 Windows
1. Download from <https://git-scm.com/download/win> and run the installer.
2. Click **Next** on every screen (default settings are fine) → **Install** → **Finish**.
3. **Close and reopen your terminal** so it notices Git.

### 🍎 macOS
In the terminal:
```bash
xcode-select --install
```
A window appears → click **Install** → wait for it to finish.

**Check it worked** (both systems): type `git --version` → you should see a version number.

## 7.2 Tell Git who you are (one time only)

Type these 2 commands, but put **your own name and email**:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

(This is just a signature on your save points — use the same email as your GitHub account.)

## 7.3 Create your free GitHub account

1. In your browser, go to <https://github.com> → **Sign up** (top right) → follow the steps (free).
2. Sign in.

> To push to **this** repository (`Kavinda-Wickramasinghe/CoppeliaSim_tutorial`) you must be its owner (Kavinda) or be added as a collaborator.
> Not the owner? Create your own repository instead: click **+** (top right) → **New repository** → name it `coppeliasim-tutorial` → **Create repository** — and use **your** address in step 7.4 below.

## 7.4 Save & upload (the 5 magic commands)

In your terminal, **inside the tutorial folder** (where `GUIDE.md` is), type these one by one:

```bash
git init                                              # 1. turn on the "save system"
git add .                                             # 2. put all files on the save list
git commit -m "My first CoppeliaSim project"          # 3. make a save point
git remote add origin https://github.com/Kavinda-Wickramasinghe/CoppeliaSim_tutorial.git   # 4. point to the cloud
git push -u origin main                               # 5. upload everything
```

In plain English:

| Command | Meaning |
| ------- | ------- |
| `git init` | "Start saving my files" |
| `git add .` | "Save-list all files" (`.` = all) |
| `git commit -m "..."` | "Save now, with this note" |
| `git remote add origin ...` | "My cloud lives at this address" |
| `git push` | "Upload to the cloud" |

**First time pushing — what happens:**

- 🪟 **Windows:** a GitHub login window pops up → click **Sign in with your browser** → log in → done.
- 🍎 **macOS:** a window may pop up asking to sign in to GitHub → follow it. If it asks for a password in the terminal instead, it wants a **token**, not your password — create one at <https://github.com/settings/tokens> and paste it.

Now refresh the GitHub page in your browser. **Your files are online.** 🎉

## 7.5 Your new daily habit (3 commands)

After you change or add code:

```bash
git add .
git commit -m "What I changed"
git push
```

Save point → upload. That's the whole habit.

## 7.6 What should NOT be uploaded

The file `.gitignore` in this project tells Git to skip junk (like your `.venv` folder — thousands of files you never want online).

- **Never delete `.gitignore`.** Never upload a `.venv` folder.
- Check any time with `git status` — `.venv` should **not** appear in the list.

## 7.7 If you make a mistake

| Situation | Fix |
| --------- | --- |
| "I broke a file, want it back" | `git restore file.py` |
| "I want to undo my last save point" | `git reset --soft HEAD~1` |
| "I saved but forgot to upload" | `git push` |
| "GitHub has newer files than me" | `git pull` (download first, then work) |

---

# PART 8 — Problems & Fixes 🔧

Find your problem in the left column, apply the fix:

| Problem | What it means | Fix |
| ------- | ------------- | --- |
| `Connection refused` | CoppeliaSim is closed, or its bridge is off | Open CoppeliaSim → menu `Modules → Connectivity → ZMQ remote API server` → run your script again |
| `ModuleNotFoundError: coppeliasim_zmqremoteapi_client` | The talking package isn't installed (or you're outside `.venv`) | Check that `(.venv)` is visible in your terminal. If not, activate it (Part 2.4). Then: `python -m pip install -r requirements.txt` |
| 🪟 `'python' is not recognized` | Python isn't in PATH | Reinstall Python and **tick "Add python.exe to PATH"** (Part 2.2). Then open a **new** terminal |
| 🪟 `running scripts is disabled on this system` | PowerShell blocks `.venv` activation | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` then activate again |
| 🍎 `python: command not found` | Mac needs the `3` | Use `python3` and `python3 -m pip ...` |
| 🍎 macOS blocks CoppeliaSim | "Unidentified developer" | Right-click (Ctrl+click) the app → **Open** → **Open** |
| Nothing appears when a script runs | Script finished too fast | Open `scripts/01_first_simulation.py`, change `DURATION = 5.0` to `15.0`, save, run again |
| 🪟 Windows firewall popup during scripts | Windows asks if Python may talk on your network | Click **Allow access** (Python is just talking to CoppeliaSim on your own computer) |
| Script hangs forever (nothing happens) | In stepping mode the simulation **waits** for `sim.step()` | Make sure your loop calls `sim.step()` each round |
| `git push` asks for a password | GitHub wants a **token**, not your account password | On the password prompt, paste a token from <https://github.com/settings/tokens>, or use the browser sign-in popup |
| `git push` says "failed to push some refs" | GitHub has files you don't have yet | `git pull` first, then `git push` again |

---

# PART 9 — What to learn next 🧭

You now know the small core that everything else is built on. Try these, in order:

1. **Drive a real robot model:** in CoppeliaSim's model browser (left side), open `robots/mobile/Pioneer 3-DX` and drag it into the scene. Find its wheel names in the scene list (right side), then spin them with `sim.setJointTargetVelocity()` — you already know how.
2. **Read positions:** `sim.getObjectPosition(handle, sim.handle_world)` gives you where an object **is** (we only *set* positions so far). Try printing it.
3. **Make a robot follow something:** read a position → compare it to a target → nudge a joint toward it → repeat.
4. **Official manual** (when you want to go deeper): <https://manual.coppeliarobotics.com/>

**The golden rules, one last time:**

- 🟢 CoppeliaSim **open first**, Python script second
- 🟢 In stepping mode, the simulation **waits** for `sim.step()`
- 🟢 `git add` → `git commit` → `git push`, **often**

Enjoy — you just built your first robot simulations. 🤖🎉
