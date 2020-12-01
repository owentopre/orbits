import numpy as np
from Particle import Particle
import copy

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

satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    [satPosition, 0, 0],
    [0, satVelocity, 0],
    np.array([0, 0, 0]),
    "Satellite",
    100.0,
    body_counter
)
bodies.append(Satellite)

time=0
n=0
Data = []

for a in range(200000):
    time=time+6
    for b in bodies:
        b.acceleration = 0
        for c in bodies:
            if b.index != c.index:
                b.updateGravitationalAcceleration(c)
        b.update(6)
    print(n)
    print(time)
    if (n%100 == 0) or (n == 0):
        Data.append([time, copy.deepcopy(Earth), copy.deepcopy(Satellite)])
    n=n+1

np.save("TwoBodyTest", Data, allow_pickle=True)

def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


print("The Earth and Satellites Location after {0} seconds is:".format((2000*6)))
print_particle(Earth)
print_particle(Satellite)
if path.exists("TwoBodyTest.npy"):
    print("The file TwoBodyTest.npy has been created.")

print("testing reading it back in")
DataIn = np.load("TwoBodyTest.npy", allow_pickle=True)

print("Printing First Entry")
print("{}".format(int(DataIn[0][0])))  #time
print_particle(DataIn[0][1])  # Earth
print_particle(DataIn[0][2])  # Satellite

print("Printing Fifth Entry")
print("{}".format(int(DataIn[4][0])))  #time
print_particle(DataIn[4][1])  # Earth
print_particle(DataIn[4][2])  # Satellite

print("Printing Last Entry")
print("{}".format(int(DataIn[-1][0])))  #time
print_particle(DataIn[-1][1])  # Earth
print_particle(DataIn[-1][2])  # Satellite
