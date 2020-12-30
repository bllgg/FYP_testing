import math
import madgwick
import numpy as np

def R_x(x):
    # body frame rotation about x axis
    return np.array([[1,      0,       0],
                     [0,np.cos(x),-np.sin(x)],
                     [0,np.sin(x), np.cos(x)]])
def R_y(y):
    # body frame rotation about y axis
    return np.array([[np.cos(y),0,np.sin(y)],
                    [0,      1,        0],
                    [-np.sin(y), 0, np.cos(y)]])
def R_z(z):
    # body frame rotation about z axis
    return np.array([[np.cos(z),-np.sin(z),0],
                     [np.sin(z), np.cos(z),0],
                     [0,      0,       1]])

roll = 0 #math.pi/2
pitch = 0
yaw = 0
R = R_x(roll) @ R_y(pitch) @ R_z(yaw)

print (R)

sensorfusion = madgwick.Madgwick(0.5)

# no rotation
quatarian = [ 1, 0, 0, 0 ]
Rq = sensorfusion.getRotationMat(quatarian)

print (Rq)

sa = [0, 1, 9.8]
print (Rq @ sa)

# 90 yaw angle
quatarian = [ 0.7071068, 0, 0, 0.7071068 ]
Rq = sensorfusion.getRotationMat(quatarian)

print (Rq)

sa = [1, 0, 9.8]
print (Rq @ sa)

# 180 yaw angle
quatarian = [ 0, 0, 0, 1 ]
Rq = sensorfusion.getRotationMat(quatarian)

print (Rq)

sa = [0, -1, 9.8]
print (Rq @ sa)
