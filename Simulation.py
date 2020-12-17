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
deltaT = 60*30
days = int((60*60*24)/deltaT)

for a in range(365*days):
    time=time+deltaT
    items = [time]
    for b in bodies:
        b.acceleration = np.array([0,0,0], dtype=float)
        for c in bodies:
            if b.index != c.index:
                b.updateGravitationalAcceleration(c)
        b.update_2(deltaT)
        print(time)
    for d in bodies:
        items.append(copy.deepcopy(d))
    n=n+1
    Data.append(items)

np.save("TwoBodyTest", Data, allow_pickle=True)

Data = np.load("TwoBodyTest.npy", allow_pickle=True)  

names = []

for a in range(len(bodies)):
    names.append(bodies[a].name)

planets = [3, 4]

x = []
y = []

for a in planets:
    for b in range(len(Data)):
        x.append(Data[b][a + 1].position[0])
        y.append(Data[b][a + 1].position[1])
    plt.plot(
        x,
        y,
        label = bodies[a].name
    )
    x = []
    y = []
plt.legend()
plt.show()

#print(Data[0][1].kineticEnergy())