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
from Bodies import (pos_marsT_2, vel_marsT_2)

#-------------------

P_EnergyList1 = []
K_EnergyList1 = []
EnergyTot1 = 0.0
momentum1 = np.array([0,0,0], dtype=float)

for a in bodies:
    K_EnergyList1.append(a.kineticEnergy())

for a in bodies:
    a.P_Energy = 0.0
    for b in bodies:
        if a.index != b.index:
            a.potentialEnergy(b)
    P_EnergyList1.append(a.P_Energy)

for a in range(len(K_EnergyList1)):
    EnergyTot1 += K_EnergyList1[a]+P_EnergyList1[a]

for a in bodies:
    momentum1 += a.momentum()

#Finding the inital Energy and Momentum of the system before the simulation

#-------------------

time=0 #starting the simulation from 0 seconds
n=0 #starting the simulation from 0 steps

Data = []
deltaT = 60*60*12
days = ((60*60*24)/deltaT)
sim_time = int(50*days)

for a in range(sim_time):
    time=time+deltaT
    items = [time]
    for b in bodies:
        b.acceleration = np.array([0,0,0], dtype=float)
        for c in bodies:
            if b.index != c.index:
                b.updateGravitationalAcceleration(c)
        b.update_1(deltaT) #change to b.update_2(deltaT) for Euler-Cromer approximation
        #print(time)
    for d in bodies:
        items.append(copy.deepcopy(d))
    n=n+1
    Data.append(items)

np.save("TwoBodyTest", Data, allow_pickle=True)

Data = np.load("TwoBodyTest.npy", allow_pickle=True)  

#-------------------

planets = [] #List bodies to be plotted here, using their index in the bodies array, ie. their index particle attribute

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

#-------------------

P_EnergyList2 = []
K_EnergyList2 = []
EnergyTot2 = 0.0
momentum2 = np.array([0,0,0], dtype=float)

for a in bodies:
    K_EnergyList2.append(a.kineticEnergy())

for a in bodies:
    a.P_Energy = 0.0
    for b in bodies:
        if a.index != b.index:
            a.potentialEnergy(b)
    P_EnergyList2.append(a.P_Energy)

for a in range(len(K_EnergyList2)):
    EnergyTot2 += K_EnergyList2[a]+P_EnergyList2[a]

for a in bodies:
    momentum2 += a.momentum()

#Finding Energy and Momentum after the simulation


print(bodies[5].position)
print(bodies[5].velocity)

print(pos_marsT_2)
print(vel_marsT_2)
