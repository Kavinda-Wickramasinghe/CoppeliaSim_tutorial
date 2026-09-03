# 🤖 CoppeliaSim Tutorial

**One guide, everything inside:** installing CoppeliaSim, running your first Python simulation, and pushing your code to GitHub.

## 👉 Start here

📖 **[GUIDE.md](GUIDE.md)** — the beginner guide (follow it from Part 1 to Part 9)

## ⚡ Quick commands

```bash
# 1. install the Python package (inside the project folder)
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate        # Linux / macOS
python -m pip install -r requirements.txt

# 2. open CoppeliaSim, then run:
python scripts/00_hello_coppelia.py
python scripts/01_first_simulation.py
python scripts/02_spin_the_joint.py
```

## 📂 Files

| File | Purpose |
| ---- | ------- |
| `GUIDE.md` | ⭐ The complete beginner guide |
| `scripts/00_hello_coppelia.py` | Test: connect Python ⇄ CoppeliaSim |
| `scripts/01_first_simulation.py` | Moving cube (first simulation) |
| `scripts/02_spin_the_joint.py` | Rotating arm (joints) |
| `requirements.txt` | Python packages |
| `.gitignore` | Files Git should ignore |

Made for beginners — no robotics or programming experience needed.
