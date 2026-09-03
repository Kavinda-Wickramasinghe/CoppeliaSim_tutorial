# 🤖 CoppeliaSim Tutorial for Beginners

A step-by-step, beginner-friendly guide to:

1. ✅ **Install and launch CoppeliaSim** (the free **Edu** version)
2. ✅ **Run your first simulation** from **Python** (ZeroMQ Remote API)
3. ✅ **Set up Git** from zero and push your code to **GitHub**

No robotics or programming experience required — every step is explained.

---

## 🚀 Quick Start (5 minutes)

### Step 1 — Install CoppeliaSim

Download the **CoppeliaSim Edu** version for your operating system:

- Windows / macOS / Linux download: <https://www.coppeliarobotics.com/downloads>

Full details (installation + first GUI simulation):  
📖 [`docs/01-coppeliasim-setup.md`](docs/01-coppeliasim-setup.md)

### Step 2 — Install the Python client

Open a terminal and run:

```bash
# optional but recommended: create a virtual environment
python -m venv .venv

# activate it
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# install the CoppeliaSim Python client
python -m pip install -r requirements.txt
```

### Step 3 — Run your first script

1. **Start CoppeliaSim** (keep it open).
2. Make sure the **ZMQ remote API server** is running:
   `Modules → Connectivity → ZMQ remote API server` (it usually auto-starts).
3. In another terminal, run:

```bash
python scripts/00_hello_coppelia.py
```

If you see `Connected to CoppeliaSim!` — congratulations, you are connected! 🎉

Then try your **first real simulation**:

```bash
python scripts/01_first_simulation.py
```

A cube will appear in CoppeliaSim and move in a circle. Full walkthrough:  
📖 [`docs/02-first-python-simulation.md`](docs/02-first-python-simulation.md)

---

## 📂 What's in this repository

| File / folder                     | What it is                                        |
| --------------------------------- | ------------------------------------------------- |
| `README.md`                       | This page — overview + quick start                |
| `docs/01-coppeliasim-setup.md`    | Install CoppeliaSim + take a tour of the GUI      |
| `docs/02-first-python-simulation.md` | Write and run your first Python simulation     |
| `docs/03-git-basics.md`           | Learn Git from zero (init, commit, push to GitHub)|
| `scripts/00_hello_coppelia.py`    | Test: connect Python ⇄ CoppeliaSim                |
| `scripts/01_first_simulation.py`  | Create a cube and animate it with Python          |
| `scripts/02_spin_the_joint.py`    | Create a rotating arm and control a joint         |
| `requirements.txt`                | The Python packages you need                      |
| `.gitignore`                      | Files Git should ignore (explained in Git guide)  |

---

## 🗺️ Learning path

```
Install CoppeliaSim ──► Run it in the GUI ──► Connect Python ──► First simulation
        │                    │                    │                      │
  docs/01-coppeliasim   docs/01-coppeliasim   scripts/00_hello     scripts/01_first_simulation
                        (play button)         + docs/02            scripts/02_spin_the_joint
```

Then keep your work safe with Git (and publish it on GitHub):  
📖 [`docs/03-git-basics.md`](docs/03-git-basics.md)

---

## ❓ Troubleshooting (the 3 most common problems)

| Problem                                       | Fix                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------- |
| `Connection refused` when running the script  | CoppeliaSim is not running, or the ZMQ server is off → start it (`Modules → Connectivity → ZMQ remote API server`) |
| `ModuleNotFoundError: coppeliasim_zmqremoteapi_client` | You didn't install the package: `python -m pip install -r requirements.txt` |
| Nothing moves / no cube appears               | Run the script **after** starting CoppeliaSim, and wait at least 5 seconds for it to finish |

More fixes in [`docs/02-first-python-simulation.md`](docs/02-first-python-simulation.md#troubleshooting).

---

## 📜 Notes on licensing

- **CoppeliaSim Edu** is free for **educational and non-commercial** purposes.
  For commercial use, Coppelia Robotics offers paid licenses (Pro / Lite).
- The Python example code in this repository is free to use, modify, and learn from.

---

## 📚 Official links

- CoppeliaSim download: <https://www.coppeliarobotics.com/downloads>
- User manual: <https://manual.coppeliarobotics.com/>
- ZeroMQ remote API docs: <https://manual.coppeliarobotics.com/en/zmqRemoteApiOverview.htm>
- Community forum: <https://forum.coppeliarobotics.com/>
- Python client package: <https://pypi.org/project/coppeliasim-zmqremoteapi-client/>
