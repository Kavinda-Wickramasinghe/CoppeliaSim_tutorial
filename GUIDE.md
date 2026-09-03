# 🚀 CoppeliaSim for Complete Beginners — The One Guide

This is **the only guide you need**. It takes you from **zero** to:

1. Running CoppeliaSim
2. Controlling it with **Python**
3. Saving your code on **GitHub** with **Git**

Follow the parts **in order**. Every step tells you **exactly** what to click or type. If something doesn't work, jump to **Part 8 (Problems & Fixes)**.

---

## What you will make (in 30–45 minutes)

| What | Where | What you'll see |
| ---- | ----- | --------------- |
| ✅ A connection test | `scripts/00_hello_coppelia.py` | Python says "Connected to CoppeliaSim!" |
| ✅ A moving cube | `scripts/01_first_simulation.py` | A blue-ish cube **circles around** for 5 seconds in CoppeliaSim |
| ✅ A spinning robot arm | `scripts/02_spin_the_joint.py` | A rod **rotates in circles** like a clock hand |
| ✅ Your code on GitHub | Part 7 | Your scripts saved online |

---

## Checklist before you start

- [ ] A computer (Windows / macOS / Linux) — no special hardware needed
- [ ] Internet (to download 2 things: CoppeliaSim + one Python package)
- [ ] About 30–45 minutes

---

# PART 1 — Install CoppeliaSim ⏱️ 5 minutes

## 1.1 Go to the download page

Open this link in your browser:

**<https://www.coppeliarobotics.com/downloads>**

Find the section called **CoppeliaSim Edu** (it is the free one for learning).

## 1.2 Download the file for your computer

| Your computer | Click on | You get a file like |
| ------------- | -------- | ------------------- |
| **Windows** | Windows | `CoppeliaSim_Edu_V4_10_0_rev0_Setup.exe` |
| **macOS** | macOS | `CoppeliaSim_Edu_V4_10_0_rev0.dmg` |
| **Linux** | Ubuntu 20.04 / 22.04 | `CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu22_04.tar.gz` |

> Don't worry about the exact version number — any version 4.4 or newer works.

## 1.3 Install and open it

**Windows:** double-click the `.exe` → click Next, Next, Install → open **CoppeliaSim** from the Start menu.

**macOS:** open the `.dmg` → drag the **CoppeliaSim** icon into **Applications** → open it.
> If macOS says "unidentified developer": **right-click** the app icon → **Open** → **Open** again.

**Linux:** open a terminal and type:

```bash
tar -xzf CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu22_04.tar.gz
cd CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu22_04
./coppeliasim.sh
```

## 1.4 You should now see this

A 3D scene with a small robot driving around. That's it — CoppeliaSim works! 🎉

## 1.5 The only 4 buttons you need for now

In the top toolbar:

| Button | What it does |
| ------ | ------------ |
| ▶️ **Play** | Starts the simulation |
| ⏸ **Pause** | Freezes it |
| ⏹ **Stop** | Resets everything |
| 🖱️ **Mouse drag** | Rotates the camera around the scene |

**Try it:** click ▶️ Play, watch the robot, click ⏹ Stop.

## 1.6 Turn on the "bridge" to Python (one click)

Python talks to CoppeliaSim through a small helper called the **ZMQ remote API server**. It normally starts by itself, but let's make sure:

In the CoppeliaSim menu bar:

**`Modules → Connectivity → ZMQ remote API server`**

Look at the small console at the bottom. You should see something like:

```
ZMQ remote API server started on port 23000
```

CoppeliaSim is ready. Keep it **open** — we'll come back to it.

---

# PART 2 — Install the Python piece ⏱️ 5 minutes

Python is the "brain" that will control CoppeliaSim. We need one small package so they can talk.

## 2.1 Open a terminal

- **Windows:** press `Windows key`, type `powershell`, press Enter.
- **macOS:** press `Cmd + Space`, type `terminal`, press Enter.
- **Linux:** press `Ctrl + Alt + T`.

## 2.2 Go to this project folder

```bash
cd CoppeliaSim_tutorial
```

(If you downloaded this guide from GitHub, first run `git clone <your-repo-url>` — Part 7 explains it, or just put your scripts in any folder and `cd` into it.)

## 2.3 Make a private "room" for Python (recommended)

```bash
python -m venv .venv
```

This creates a folder called `.venv` — a private room for our packages so we never mess up other projects. You only do this **once**.

## 2.4 Enter the room

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` appear at the start of your command line. That means it worked.

## 2.5 Install the package (one command)

```bash
python -m pip install -r requirements.txt
```

This installs `coppeliasim-zmqremoteapi-client` — the package that lets Python "call" CoppeliaSim.

**Check it worked:**
```bash
python -c "from coppeliasim_zmqremoteapi_client import RemoteAPIClient; print('OK')"
```

If it prints `OK`, you're ready. ✅

---

# PART 3 — Your first connection test ⏱️ 2 minutes

## 3.1 Do this in this exact order

1. Make sure **CoppeliaSim is open** (from Part 1).
2. In your terminal, run:

```bash
python scripts/00_hello_coppelia.py
```

## 3.2 You should see

```
Connected to CoppeliaSim!
Simulation time: 0.00 s
Found 21 shape object(s) in the scene.
  - cuboid
  - ...
```

If you see `Connected to CoppeliaSim!` — **you did it!** Python and CoppeliaSim are now talking. 🎉

> **The golden rule:** CoppeliaSim must be running **before** you run any Python script. If you close CoppeliaSim, Python loses connection.

---

# PART 4 — Your first real simulation: a moving cube ⏱️ 5 minutes

This is the fun part. Run:

```bash
python scripts/01_first_simulation.py
```

**Watch the CoppeliaSim window!** A **cube appears** and moves in a **circle** for 5 seconds, while the terminal prints its position:

```
t = 0.00 s  ->  cube at (0.000, 0.500, 0.300)
t = 0.05 s  ->  cube at (0.050, 0.499, 0.300)
t = 0.10 s  ->  cube at (0.099, 0.495, 0.300)
...
Simulation finished.
```

After it ends, find the cube in the scene list on the right — it's called `MyFirstCube`. It stays there so you can look at it.

## 4.1 What the script does (the whole idea in 4 lines)

Think of it like a phone call between two people:

| Code | Meaning (simple version) |
| ---- | ------------------------ |
| `client = RemoteAPIClient()` | **Dial the phone** — connect to CoppeliaSim |
| `sim = client.require("sim")` | **Get the remote control** — now `sim` controls the simulation |
| `sim.setStepping(True)` | **"Don't move until I say so"** — the simulation waits for us each step |
| `sim.step()` | **"Move one tiny step"** — the simulation advances a little |

Then the loop repeats 100 times, **telling the cube where to go** with:

```python
sim.setObjectPosition(cube, sim.handle_world, [x, y, z])
```

That's it. You are a robot programmer now. 🎓

## 4.2 The 5 most-used commands (memory helpers)

| Command | Memory helper |
| ------- | ------------- |
| `sim.startSimulation()` | Press ▶️ Play |
| `sim.stopSimulation()` | Press ⏹ Stop |
| `sim.createPrimitiveShape(...)` | "Make me a box" |
| `sim.setObjectPosition(...)` | "Cube, go there" |
| `sim.step()` | "Take one step" |

---

# PART 5 — Your first robot arm: spin a joint ⏱️ 5 minutes

Run:

```bash
python scripts/02_spin_the_joint.py
```

A **joint** (a little hinge) appears, a **rod** is attached to it, and the rod **spins in circles** at 2 radians per second.

The terminal prints the angle:

```
t = 0.00 s  ->  joint angle = 0.00 rad
t = 0.05 s  ->  joint angle = 0.10 rad
...
```

## 5.1 The 3 lines that do all the work

```python
sim.createJoint(sim.joint_revolute, sim.jointmode_kinematic, 0)  # 1. make a hinge
sim.setObjectParent(arm, joint, True)                             # 2. stick the arm on it
sim.setJointTargetVelocity(joint, 2.0)                            # 3. spin it at 2 rad/s
```

A **joint** is how real robots move — every robot arm, wheel, and gripper uses them. You've just done real robotics.

---

# PART 6 — Make it yours (try these) 🧪 5 minutes

Open `scripts/01_first_simulation.py` in any text editor and change one number:

| Change | Line | Result |
| ------ | ---- | ------ |
| Bigger circle | `0.5 * math.sin(...)` → `1.0 * math.sin(...)` | Cube circles further out |
| Faster movement | `2.0 * t` → `4.0 * t` | Faster circle |
| Longer show | `DURATION = 5.0` → `DURATION = 10.0` | Moves for 10 seconds |

Then run it again: `python scripts/01_first_simulation.py`

> Break it, fix it, change it — **that's how you learn.** (The script creates the cube fresh if it's missing, so reruns are safe.)

---

# PART 7 — Save your work with Git & GitHub ⏱️ 10 minutes

**Why?** Git is like **save points in a video game**. Every `commit` is a save point. **GitHub** is your save file in the cloud, so your code can never be lost — and anyone can see it.

## 7.1 Install Git

| Computer | What to do |
| -------- | ---------- |
| **Windows** | Download from <https://git-scm.com/download/win>, run the installer, click Next all the way |
| **macOS** | In Terminal: `xcode-select --install` |
| **Linux** | In Terminal: `sudo apt install git` |

Check it works:
```bash
git --version
```

## 7.2 Tell Git who you are (one time)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 7.3 Create your free GitHub account & repository

1. Go to <https://github.com> and sign up (free).
2. Click **+** (top right) → **New repository**.
3. Name it, e.g. `coppeliasim-tutorial`. Click **Create repository**.
4. Copy the address it shows, like: `https://github.com/YOUR-NAME/coppeliasim-tutorial.git`

## 7.4 Type these 5 commands (the whole magic ✨)

In your terminal, inside the project folder:

```bash
git init                                  # 1. turn on the "save system"
git add .                                 # 2. choose all files to save
git commit -m "My first CoppeliaSim project"   # 3. make a save point
git remote add origin https://github.com/YOUR-NAME/coppeliasim-tutorial.git   # 4. point to your cloud
git push -u origin main                   # 5. upload everything to GitHub
```

**What the 5 lines mean (very simple):**

| Command | Plain English |
| ------- | ------------- |
| `git init` | "Start saving my files" |
| `git add .` | "Put these files in the save list" (the `.` means "all files") |
| `git commit -m "..."` | "Save now, with this note" |
| `git remote add origin ...` | "My cloud storage is at this address" |
| `git push` | "Upload to the cloud" |

Now refresh your GitHub page. **Your files are online.** 🎉

## 7.5 Your new daily habit (3 commands)

After you change or add code:

```bash
git add .
git commit -m "What I changed"
git push
```

That's it. Save point → upload.

## 7.6 What should NOT be uploaded (very important)

You will see a file called `.gitignore` in this project. It tells Git to skip things like your `.venv` folder (thousands of junk files). **Never delete it, and never upload a `.venv` folder.**

```bash
git status   # this shows what Git sees — .venv should NOT appear
```

If a big `__pycache__` or `.venv` folder shows up, add its name to `.gitignore`.

## 7.7 If you make a mistake

| Situation | Command |
| --------- | ------- |
| "I broke a file and want it back" | `git restore file.py` |
| "I want to un-save the last commit" | `git reset --soft HEAD~1` |
| "I saved, but never pushed" | `git push` |
| "GitHub has newer files than me" | `git pull` (download first, then edit) |

---

# PART 8 — Problems & fixes 🔧

| Problem | What it means | Fix |
| ------- | ------------- | --- |
| `Connection refused` when running Python | CoppeliaSim isn't running or its bridge is off | Open CoppeliaSim, then `Modules → Connectivity → ZMQ remote API server` |
| `ModuleNotFoundError: coppeliasim_zmqremoteapi_client` | Package not installed | `python -m pip install -r requirements.txt` (make sure `(.venv)` is visible!) |
| Nothing appears when script runs | Script finished too fast | Change `DURATION = 5.0` to `15.0` and rerun |
| `git push` asks for a password | GitHub wants a token, not your password | Create one at <https://github.com/settings/tokens> and paste it |
| `git push` says "failed to push some refs" | GitHub has files you don't have | `git pull` first, then `git push` |
| Windows firewall popup | Windows is blocking Python | Click **Allow access** |
| CoppeliaSim won't open on macOS | macOS blocks unknown apps | Right-click app → **Open** |
| Script hangs forever | The simulation waits for `sim.step()` | Add `sim.step()` at the end of your loop |

---

# PART 9 — What to learn next 🧭

You now know the 20% that gives 80% of the results. Next steps:

1. **Drive a real robot model:** in CoppeliaSim's left panel, open `robots → mobile → Pioneer 3-DX` and drag it into the scene. Find its wheel names in the right panel, then use `sim.setJointTargetVelocity()` on them (you already know how!).
2. **Read an object's position:** `sim.getObjectPosition(handle, sim.handle_world)` — try printing the cube's position instead of setting it.
3. **Make a robot follow a path:** combine what you learned — read position, compare to a target, nudge a joint toward it.
4. **Keep exploring** the official manual: <https://manual.coppeliarobotics.com/>

**Remember the golden rules:**
- 🟢 CoppeliaSim must be **open** before your Python script runs
- 🟢 In stepping mode, the simulation **waits** for `sim.step()`
- 🟢 Commit your work **often**, and push it to GitHub

Enjoy — you've just completed your first robot simulation. 🤖🎉
