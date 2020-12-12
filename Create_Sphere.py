# Example : create a ball by pressing a button
import pybullet as p
import time
import pybullet_data

# Make simulation world
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

plainID = p.loadURDF('plane.urdf')

# Set gravity to z-axis
p.setGravity(0, 0, -9.8)


# Sphere parametre
mass = 1
sphereR = 0.3
visualSphereID = -1

p.createCollisionShape(p.GEOM_PLANE)
SphereID = p.createCollisionShape(p.GEOM_SPHERE, radius=sphereR)
sphereStartPos = [0, 0, 0.5]
SphereStartOrientation = p.getQuaternionFromEuler([0, 0, 0])

while True:
    p.stepSimulation()

    # Press 'c' to create a ball
    # 'c' = create
    keys = p.getKeyboardEvents()
    for k, v in keys.items():
        #print(k, v)
        if (k == 99 and v & p.KEY_WAS_RELEASED):
            SphereUID = p.createMultiBody(mass, SphereID, 1, sphereStartPos, SphereStartOrientation)

    time.sleep(1/200)

p.disconnect()