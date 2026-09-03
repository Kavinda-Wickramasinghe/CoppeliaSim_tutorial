# Step 2 — Your first simulation with Python

> **Goal of this page:** connect Python to CoppeliaSim, then write and run your **first real simulation**: a cube that moves in a circle, and a rotating arm with a joint.

By the end you will understand every line — this is the core skill for all future robotics scripts.

---

## 1. What you need

| Requirement | How to check |
| ----------- | ------------ |
| CoppeliaSim installed and running | Guide: [01-coppeliasim-setup.md](01-coppeliasim-setup.md) |
| ZMQ remote API server running | `Modules → Connectivity → ZMQ remote API server` |
| Python 3.9+ installed | `python --version` |
| The `coppeliasim-zmqremoteapi-client` package | see below |

---

## 2. Set up the Python environment (one time)

Open a terminal and run:

```bash
# 1. go to this repository's folder
cd CoppeliaSim_tutorial

# 2. optional but recommended: isolated virtual environment
python -m venv .venv

# 3. activate the environment
#    Windows (PowerShell or cmd):
.venv\Scripts\activate
#    Linux / macOS:
source .venv/bin/activate

# 4. install the Python client (ZeroMQ + CBOR are installed automatically)
python -m pip install -r requirements.txt
```

> 💡 **Why a virtual environment?** It keeps this project's packages separate from your system Python, so installing things here can never break other projects.

Verify the install:

```bash
python -c "from coppeliasim_zmqremoteapi_client import RemoteAPIClient; print('OK')"
```

---

## 3. What is the ZeroMQ remote API?

CoppeliaSim runs a small server on **port 23000** (left running by default). Your Python program is a **client** that sends commands to that server:

```
┌────────────┐   commands (ZeroMQ / port 23000)   ┌───────────────┐
│  Python     │ ─────────────────────────────────► │  CoppeliaSim  │
│  (client)   │ ◄───────────────────────────────── │  (server)     │
└────────────┘      results (positions, time, …)   └───────────────┘
```

Because of this, **CoppeliaSim must be running before your Python script starts.**

---

## 4. Script 0 — "Hello CoppeliaSim" (connection test)

Run it from the `CoppeliaSim_tutorial` folder:

```bash
python scripts/00_hello_coppelia.py
```

**What you should see:**

```
Connected to CoppeliaSim!
Simulation time: 0.00 s
Found 21 shape objects in the scene
 - cuboid
 - cylinder
 - ...
```

### 🔍 Line-by-line explanation

```python
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
```
Import the client library.

```python
client = RemoteAPIClient()
```
Create a client that connects to `localhost`, port `23000` (the defaults). Use `RemoteAPIClient('192.168.1.50', 23000)` if CoppeliaSim runs on another computer.

```python
sim = client.require('sim')
```
Ask CoppeliaSim for its **`sim` object** — this is your remote control. Every function you call on `sim` (e.g. `sim.getSimulationTime()`) is executed inside CoppeliaSim.

```python
sim.getObjectsInTree(sim.handle_scene, sim.sceneobject_shape)
```
List all **shape objects** in the scene. `sim.handle_scene` means "the whole scene", `sim.sceneobject_shape` = "only shapes".

---

## 5. Script 1 — your first real simulation 🎉

```bash
python scripts/01_first_simulation.py
```

**What happens:**
1. Python creates a **cube** called `MyFirstCube` in the scene (if one is not already there).
2. Python switches CoppeliaSim to **stepping mode** (the simulation only moves when Python says `step()`).
3. For 5 seconds, Python tells the cube where to go: `x = 0.5·sin(2t)`, `y = 0.5·cos(2t)` — a circular path.
4. Python stops the simulation. The cube stays in the scene so you can look at it! 👀

Watch it live in the CoppeliaSim 3D view while the terminal prints the cube position.

**Why this is a "real" simulation:** you are a computer program making decisions and sending commands to a simulator every step — the exact same pattern you'll use later to drive a robot arm or a mobile robot.

### 🔍 The important new concepts

| Concept | Code | Meaning |
| ------- | ---- | ------- |
| Create an object | `sim.createPrimitiveShape(sim.primitiveshape_cuboid, [0.2, 0.2, 0.2])` | Make a 20 cm cube in the scene |
| Name it | `sim.setObjectName(cube, 'MyFirstCube')` | So you (and future scripts) can find it by name |
| Find a handle | `sim.getObject('MyFirstCube')` | Ask CoppeliaSim for the numeric handle of an object |
| **Stepping mode** | `sim.setStepping(True)` | The simulation advances **only** when you call `sim.step()` — this is the safest mode for beginners |
| Start/stop | `sim.startSimulation()` / `sim.stopSimulation()` | Like pressing the ▶️ / ⏹ buttons |
| Move an object | `sim.setObjectPosition(cube, sim.handle_world, [x, y, z])` | Set the cube's position in the world |
| Advance one step | `sim.step()` | Let CoppeliaSim move the physics forward one time step |
| Always clean up | `try: ... finally: sim.stopSimulation()` | Guarantees the simulation stops even if the script errors |

> 📌 **Old vs new API names:** In older scripts you'll see `sim.getObjectHandle(...)` and `sim.object_shape`. The names were modernised in CoppeliaSim 4.6+ (`sim.getObject(...)`, `sim.sceneobject_shape`). Both usually still work — this tutorial uses the modern names.

---

## 6. Script 2 — control a joint (basic robotics!)

Now let's build something closer to real robotics: a **revolute joint** with a **long arm**, and make it spin at a constant speed.

```bash
python scripts/02_spin_the_joint.py
```

**What happens:** Python creates a joint + arm, attaches the arm to the joint, then commands the joint to rotate at `2 rad/s` for 5 seconds while printing its angle.

### 🔍 New concepts

```python
sim.createJoint(sim.joint_revolute, sim.jointmode_kinematic, 0)
```
Create a revolute (hinge) joint in **kinematic** mode — the joint is moved by code, and physics is mostly bypassed (perfect for learning).

```python
sim.setObjectParent(arm, joint, True)
```
Attach the arm to the joint. `True` = "keep the arm where it is visually while re-parenting".

```python
sim.setJointTargetVelocity(joint, 2.0)
```
Order the joint to rotate at 2 rad/s (≈ 114°/s).

```python
sim.getJointPosition(joint)
```
Read the joint's current angle in radians (the "feedback" your program receives).

---

## 7. Try it yourself — 3 fun challenges 🧪

1. **Make the circle bigger:** in `01_first_simulation.py`, change `0.5` to `1.0` in `x` and `y` (cube circles further out).
2. **Spin faster:** in `02_spin_the_joint.py`, change `2.0` to `5.0` rad/s.
3. **Combine them:** create a second cube and give it a different path — or drive the joint so the arm follows a sine motion instead of constant speed:
   ```python
   sim.setJointTargetPosition(joint, 0.5 * math.sin(2.0 * t))
   ```
   (a tiny preview of **motion control**, the heart of robotics).

---

## 8. Troubleshooting

| Symptom | Cause | Fix |
| ------- | ----- | --- |
| `Connection refused` / `No route to host` | CoppeliaSim not running, or ZMQ server off | Start CoppeliaSim, then `Modules → Connectivity → ZMQ remote API server` |
| `ModuleNotFoundError: coppeliasim_zmqremoteapi_client` | Package not installed | `python -m pip install -r requirements.txt` (and make sure your venv is active) |
| Script connects but nothing appears | You ran it before the scene loaded, or the 5 s loop finished very fast | Raise the loop duration (e.g. `5.0` → `10.0`) and check the scene hierarchy for `MyFirstCube` |
| Everything works, but object names differ | Scene was modified | The scripts create objects by name if missing, so a second run reuses them |
| Port 23000 already in use | Another app/session uses it | Start CoppeliaSim with e.g. `-GzmqRemoteApi.rpcPort=23001` and connect with `RemoteAPIClient('localhost', 23001)` |
| Windows firewall popup | Windows blocks Python | Click **Allow access** |
| Script hangs forever | Simulation stopped but you forgot `sim.step()` in the loop | Make sure every loop ends with `sim.step()` |

---

## 9. Where to go next

- Walk through every command of the GUI (objects, model browser, scripts) in the [official manual](https://manual.coppeliarobotics.com/).
- Load a **robot model** from the left panel (`robots/mobile/...`), find its joint names in the scene tree, and drive those joints from Python — you already know all the functions you need (`getObject`, `setJointTargetVelocity`, `step`).
- Keep your code safe and share it: 📖 [Step 3 — Git basics](03-git-basics.md).
