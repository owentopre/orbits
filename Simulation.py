import numpy as np
from Particle import Particle
import copy
from poliastro import constants
from astropy import constants as const
G = float(const.G)
body_counter = 0
bodies = []

earthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    np.array([0, 0, 0]),
    np.array([0, 0, 0]),
    np.array([0, 0, 0]),
    "Earth",
    earthMass,
    body_counter 
)
bodies.append(Earth)
body_counter = body_counter + 1

satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    [satPosition, 0, 0],
    [0, satVelocity, 0],
    np.array([0, 0, 0]),
    "Satellite",
    100.0,
    body_counter 
)
bodies.append(Satellite)
body_counter = body_counter + 1

Mars = Particle(
    [1.423799882991461E+08, 1.678375078328744E+08, -3.706714322030544E+03],
    [1.747282532351254E+01, 1.784027466311700E+01, 8.027751608403317E-01],
    np.array([0, 0, 0]),
    "Mars",
    6.4171e+23,
    body_counter 
)
bodies.append(Mars)
body_counter = body_counter + 1

# Mars = Particle(
#     [1.423799882991461E+08, 1.678375078328744E+08, -3.706714322030544E+03],
#     [1.747282532351254E+01, 1.784027466311700E+01, 8.027751608403317E-01],
#     np.array([0, 0, 0]),
#     "Mars",
#     6.4171e+23,
#     body_counter 
# )
# bodies.append(Mars)
# body_counter = body_counter + 1

time=0
n=0
Data = []

for a in range(60*60*24*60):
    time=time+6
    for b in bodies:
        b.acceleration = np.array([0,0,0], dtype=float)
        for c in bodies:
            if b.index != c.index:
                b.updateGravitationalAcceleration(c)
        b.update_1(6)
    #print(n)
    #print(time)
    if (n%100 == 0) or (n == 0):
        print(n)
        print(time)
        print(b.acceleration)
        Data.append([time, copy.deepcopy(Earth), copy.deepcopy(Satellite)])
    n=n+1

np.save("TwoBodyTest", Data, allow_pickle=True)

Data = np.load("TwoBodyTest.npy", allow_pickle=True)  
print(Data[0][1].kineticEnergy())
