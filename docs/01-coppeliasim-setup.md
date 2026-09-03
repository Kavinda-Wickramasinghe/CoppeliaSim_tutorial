# Step 1 — Install CoppeliaSim and run it in the GUI

> **Goal of this page:** install CoppeliaSim (free Edu version), get it running, and take a first look at the interface. No Python required yet.

---

## 1. What is CoppeliaSim?

CoppeliaSim (formerly called **V-REP**) is a popular 3D robot simulator. It lets you build scenes, add robots and sensors, run physics (gravity, collisions, joints), and control everything from code — Lua (built into CoppeliaSim) or your own Python scripts.

For beginners it has two great features:

- A **built-in library of ready-made robots** (UR5 arm, Pioneer, drones, etc.)
- A **remote API**: you control the simulation from Python, while the 3D view runs in CoppeliaSim.

---

## 2. Choose the right version

CoppeliaSim comes in three editions:

| Edition | Cost | Use it if... |
| ------- | ---- | ------------ |
| **Edu**  | **Free** | You are a student / teacher, or any non-commercial use ✅ (this tutorial) |
| Pro      | Paid (commercial) | You develop commercial products |
| Lite     | Paid (commercial) | Simplified commercial version |

> ⚠️ **Important:** The **Edu** version is free only for **educational and non-commercial use**. If you are a student or learner, you are fine — just don't use it to build commercial products.

---

## 3. Download CoppeliaSim Edu

1. Go to: <https://www.coppeliarobotics.com/downloads>
2. Scroll to **CoppeliaSim Edu** and choose your operating system:
   - **Windows** → setup file `.exe` (e.g. `CoppeliaSim_Edu_V4_10_0_rev0_Setup.exe`)
   - **macOS** → `.dmg` file
   - **Linux** → `.tar.gz` archive (choose Ubuntu 20.04 or 22.04 depending on your system)

> The latest version at the time of writing is **V4.10.0 rev0**. Any version **4.4 or newer** works for this tutorial.

---

## 4. Install it

### 🪟 Windows

1. Double-click the downloaded `.exe` file.
2. Follow the installer (default settings are fine).
3. If Windows asks you to install the **Microsoft Visual C++ Redistributable**, click **Yes** and let it finish.
4. Launch **CoppeliaSim** from the Start menu or desktop icon.

### 🍎 macOS

1. Open the `.dmg` file and drag the **CoppeliaSim** app into the **Applications** folder.
2. If macOS blocks it ("unidentified developer" warning), **right-click** the app → **Open** → **Open** again.
3. Launch it from Applications.

### 🐧 Linux

```bash
# 1. Download the .tar.gz file, then unpack it:
tar -xzf CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu22_04.tar.gz

# 2. Go into the unpacked folder:
cd CoppeliaSim_Edu_V4_10_0_rev0_Ubuntu22_04

# 3. Run it:
./coppeliasim.sh
```

> First launch on Linux may ask you to install OpenGL/OpenAL libraries — the error message tells you exactly which `apt install ...` command to run.

---

## 5. First look at the GUI

When CoppeliaSim opens, you should see the **default demo scene** (a mobile robot driving around). Take a moment to find these areas:

| Area | What it is |
| ---- | ---------- |
| **Large 3D view** | The scene itself. Drag with the mouse to orbit the camera |
| **Left panel — Model browser** | Ready-made robots/objects you can drag into the scene |
| **Right panel — Scene hierarchy** | A tree of all objects: `robot_joint1`, `cuboid`, etc. |
| **Top toolbar** | ▶️ Play sim, ⏸ Pause, ⏹ Stop sim, and undo/redo |
| **Bottom — Lua console / status bar** | Where messages are printed. You'll use it later to see the ZMQ server status |

### 🖱️ Camera controls (default)

| Action | Mouse / keyboard |
| ------ | ---------------- |
| Rotate camera | Left-drag |
| Pan camera | Ctrl + left-drag |
| Zoom | Mouse wheel |
| Select object | Left-click object |

---

## 6. Run your first simulation — inside the GUI only

No code yet — just press buttons:

1. Click ▶️ **Play** (top toolbar, or `Simulation → Start`)
2. Watch the demo robot drive and avoid obstacles.
3. Click ⏹ **Stop** (or `Simulation → Stop`).

> 💡 **Do NOT use Pause now.** Pause freezes the simulation; Stop ends it and resets objects to their initial state.

If that works, CoppeliaSim is ready. ✅

---

## 7. Check the "ZMQ remote API server" (needed for Python later)

The Python client talks to CoppeliaSim through a small server called the **ZMQ remote API server**. It normally **auto-starts** when CoppeliaSim launches, but let's verify:

1. In the menu bar: **Modules → Connectivity → ZMQ remote API server** (it should say it is running, and usually listens on port **23000**).
2. If it is not running, click it to **start/restart** it.
3. Watch the bottom console — you should see something like:
   `ZMQ remote API server started on port 23000`.

Now go to the next page:

📖 **[Step 2 — Run your first simulation with Python](02-first-python-simulation.md)**

---

## ❗ Common problems and fixes

| Problem | Fix |
| ------- | --- |
| CoppeliaSim won't start on macOS | Right-click the app → **Open** (to bypass quarantine) |
| Windows asks for the C++ redistributable | Install it and rerun the setup |
| Linux shows missing library errors | Run the `apt install ...` command shown in the terminal |
| Scene is black / 3D view is empty | Press 📷 **camera fit** in the toolbar, or reload the default scene |
| No ZMQ server line in console | Open `Modules → Connectivity → ZMQ remote API server` and start it |
