"""
01 - Your first real simulation
===============================

This script:
  1. Reuses an existing cube called 'MyFirstCube' or creates one.
  2. Switches CoppeliaSim into STEPPING mode, so the simulation only
     advances when we call sim.step().
  3. Moves the cube in a circle (x = 0.5*sin(2t), y = 0.5*cos(2t))
     for 5 seconds, printing its position every step.
  4. Stops the simulation. The cube remains in the scene for you to see.

BEFORE RUNNING: start CoppeliaSim and make sure the ZMQ remote API
server is running (Modules -> Connectivity -> ZMQ remote API server).

RUN (from the repository root):
      python scripts/01_first_simulation.py

WATCH: the CoppeliaSim window while the terminal prints positions!
"""

import math

from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# --- 1. Connect to CoppeliaSim -----------------------------------------
client = RemoteAPIClient()
sim = client.require("sim")

CUBE_NAME = "MyFirstCube"

# --- 2. Create (or find) a cube ----------------------------------------
try:
    cube = sim.getObject(CUBE_NAME)
    print(f'Found existing object "{CUBE_NAME}" (handle {cube}).')
except Exception:
    # Create a 20 cm x 20 cm x 20 cm cube in the scene.
    cube = sim.createPrimitiveShape(sim.primitiveshape_cuboid, [0.2, 0.2, 0.2])
    sim.setObjectAlias(cube, CUBE_NAME)
    # Put the cube 0.3 m above the ground (world coordinates).
    sim.setObjectPosition(cube, sim.handle_world, [0.0, 0.0, 0.3])
    print(f'Created object "{CUBE_NAME}" (handle {cube}).')

# --- 3. Run the simulation ---------------------------------------------
# Stepping mode: CoppeliaSim ONLY advances when we call sim.step().
sim.setStepping(True)
sim.startSimulation()

try:
    DURATION = 5.0            # seconds (simulation time)
    t0 = sim.getSimulationTime()

    while sim.getSimulationTime() - t0 < DURATION:
        t = sim.getSimulationTime()

        # Simple circular path (change these 2 lines to try something new!)
        x = 0.5 * math.sin(2.0 * t)
        y = 0.5 * math.cos(2.0 * t)
        z = 0.3

        sim.setObjectPosition(cube, sim.handle_world, [x, y, z])
        print(f"t = {t:4.2f} s  ->  cube at ({x:5.3f}, {y:5.3f}, {z:5.3f})")

        # Tell CoppeliaSim to advance exactly one time step.
        sim.step()

finally:
    # Always clean up, even if something goes wrong above.
    sim.stopSimulation()
    sim.setStepping(False)

print("\nSimulation finished. Look for 'MyFirstCube' in the scene tree!")
