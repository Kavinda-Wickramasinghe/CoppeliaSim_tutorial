"""
00 - Hello CoppeliaSim
======================

Your very first Python <-> CoppeliaSim connection test.

BEFORE RUNNING:
1. Start CoppeliaSim (Edu edition) and keep it open.
2. Make sure the ZMQ remote API server is running:
      Menu bar -> Modules -> Connectivity -> ZMQ remote API server
   (it normally auto-starts and listens on port 23000)
3. Install the client package:
      python -m pip install coppeliasim-zmqremoteapi-client

RUN (from the repository root):
      python scripts/00_hello_coppelia.py

If you see "Connected to CoppeliaSim!" you are ready for the next script.
"""

from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Connect to CoppeliaSim running on this computer, port 23000 (defaults).
client = RemoteAPIClient()

# The 'sim' object is your remote control: every sim.xxx() call is
# executed inside CoppeliaSim.
sim = client.require("sim")

print("Connected to CoppeliaSim!")
print(f"Simulation time: {sim.getSimulationTime():.2f} s")

# List the shape objects that currently exist in the scene.
shapes = sim.getObjectsInTree(sim.handle_scene, sim.sceneobject_shape)
print(f"Found {len(shapes)} shape object(s) in the scene.")
for handle in shapes[:5]:
    name = sim.getObjectName(handle)
    print(f"  - {name}")

print("\nNext step: python scripts/01_first_simulation.py")
