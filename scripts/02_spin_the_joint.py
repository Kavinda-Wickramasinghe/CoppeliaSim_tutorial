"""
02 - Control a joint (your first taste of robotics!)
====================================================

This script:
  1. Creates a revolute joint (hinge) called 'MyFirstJoint'.
  2. Creates a long cuboid arm called 'MyArm' and attaches it to the joint.
  3. Commands the joint to rotate at 2 rad/s for 5 seconds, printing
     the joint angle every step.

BEFORE RUNNING: start CoppeliaSim and make sure the ZMQ remote API
server is running (Modules -> Connectivity -> ZMQ remote API server).

RUN (from the repository root):
      python scripts/02_spin_the_joint.py
"""

from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# --- 1. Connect ---------------------------------------------------------
client = RemoteAPIClient()
sim = client.require("sim")

# --- 2. Create the joint ------------------------------------------------
# sim.joint_revolute      = hinge joint (spins around one axis)
# sim.jointmode_kinematic = code drives the joint (no complex physics)
joint = sim.createJoint(sim.joint_revolute, sim.jointmode_kinematic, 0)
sim.setObjectAlias(joint, "MyFirstJoint")
sim.setObjectPosition(joint, sim.handle_world, [0.0, 0.0, 0.3])

# --- 3. Create the arm and attach it to the joint -----------------------
# A long, thin cuboid: 60 cm long, 4 cm x 4 cm cross-section.
arm = sim.createPrimitiveShape(sim.primitiveshape_cuboid, [0.6, 0.04, 0.04])
sim.setObjectAlias(arm, "MyArm")
# Attach arm to joint. True = keep the arm visually where it is now.
sim.setObjectParent(arm, joint, True)
# Place the arm 0.3 m along the joint's local x-axis, so it hangs off the hinge.
sim.setObjectPosition(arm, joint, [0.3, 0.0, 0.0])

# --- 4. Run the simulation ----------------------------------------------
sim.setStepping(True)
sim.startSimulation()

try:
    # Command the joint to rotate at 2 rad/s (about 114 degrees per second).
    sim.setJointTargetVelocity(joint, 2.0)

    DURATION = 5.0
    t0 = sim.getSimulationTime()

    while sim.getSimulationTime() - t0 < DURATION:
        t = sim.getSimulationTime()
        angle = sim.getJointPosition(joint)  # radians
        print(f"t = {t:4.2f} s  ->  joint angle = {angle:6.2f} rad")
        sim.step()

finally:
    sim.stopSimulation()
    sim.setStepping(False)

print("\nSimulation finished. Find 'MyFirstJoint' and 'MyArm' in the scene tree!")
