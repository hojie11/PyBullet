import pybullet as p
import time # for sleep function
import pybullet_data

pysicsClinet = p.connect(p.GUI) # make simulation world _ graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8) # set gravity vector to z-axis
p.setTimeStep(1/200) # update per 200 frames

planeID = p.loadURDF("plane.urdf") # load .urdf file
cubeStartPos = [2, -1, 1] # set position of object
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 3.14]) # set rotation of object 
                                                                                                # should convert euler to Quaternion
robotID = p.loadURDF("r2d2.urdf", cubeStartPos, cubeStartOrientation) # load robot .urdf file by using parameters you set

for i in range(10000):
    p.stepSimulation()
    time.sleep(1/200)

p.disconnect(physicsClient)