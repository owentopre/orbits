import numpy as np
from Particle import Particle
import copy

earthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass
)
satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    position=[satPosition, 0, 0],
    velocity=[0, satVelocity, 0],
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=100.
)

time=0
n=0
Data = []

for a in range(200000):
    time=time+6
    for b in [Earth, Satellite]:
        for c in [Earth, Satellite]:
            b.updateGravitationalAcceleration(c)
        b.update(6)
    #print(n)
    #print(time)
    if (n%100 == 0) or (n == 0):
        Data.append([time, copy.deepcopy(Earth), copy.deepcopy(Satellite)])
    n=n+1
np.save("TwoBodyTest", Data, allow_pickle=True)
