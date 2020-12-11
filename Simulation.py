import numpy as np
from Particle import Particle
import copy
import scipy.constants as const
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from poliastro import constants
from spiceypy import sxform, mxvg
import matplotlib.pyplot as plt 
from Bodies import bodies

time=0
n=0
Data = []
deltaT = 60*60*24 

for a in range(1000):
    time=time+deltaT
    items = [time]
    for b in bodies:
        b.acceleration = np.array([0,0,0], dtype=float)
        for c in bodies:
            if b.index != c.index:
                b.updateGravitationalAcceleration(c)
        b.update_1(deltaT)
        print(time)
    #print(n)
    #print(time)
    #if (n%100 == 0) or (n == 0):
        # print(n)
        # print(time)
        # print(b.acceleration)
    for d in bodies:
        items.append(copy.deepcopy(d))
    n=n+1
    Data.append(items)

np.save("TwoBodyTest", Data, allow_pickle=True)

Data = np.load("TwoBodyTest.npy", allow_pickle=True)  

sun_x = []
sun_y = []
print(Data[2])
print(Data[0][1].name)

for i in range(len(Data)):
    #print(i)
    sun_x.append(Data[i][1].position[0])
    sun_y.append(Data[i][1].position[1])

plt.plot(sun_x, sun_y, label='trajectory')
plt.xlabel('sun x')
plt.ylabel('sun y')
plt.legend()
plt.show()


mercury_x = []
mercury_y = []

for l in range(len(Data)):
    print(l)
    mercury_x.append(Data[l][2].position[0])
    mercury_y.append(Data[l][2].position[1])


plt.plot(mercury_x, mercury_y, label='trajectory')
plt.xlabel('mer x')
plt.ylabel('mer y')
plt.legend()
plt.show()


#print(Data[0][1].kineticEnergy())