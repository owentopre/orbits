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

hours = 240 #change this value to affect the size of deltaT
days = 365*100 #change this value to affect the simulation time
approximation = 1 #1=Euler 2=Euler-Cromer 3=Verlet

Data = []
deltaT = 60*60*hours
day = ((60*60*24)/deltaT)
sim_time = int(days*day)

for a in range(sim_time):
    time=time+deltaT
    items = [time]
    for b in bodies:
        b.acceleration = np.array([0,0,0], dtype=float)
        for c in bodies:
            if b.index != c.index:
                b.updateGravitationalAcceleration(c)
        if approximation == 1:
            b.update_1(deltaT) 
        if approximation == 2:
            b.update_2(deltaT)
        if approximation == 3:
            b.update_1(deltaT)
            for c in bodies:
                if b.index != c.index:
                    b.updateGravitationalAcceleration(c)
            b.update_3(deltaT)
        #print(time)
    for d in bodies:
        items.append(copy.deepcopy(d))
    n=n+1
    Data.append(items)

np.save("SimulationLog", Data, allow_pickle=True)

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
