import numpy as np
from Particle import Particle

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

for a in range(2000):
    for b in [Earth, Satellite]:
        for c in [Earth, Satellite]:
            b.updateGravitationalAcceleration(c)
        b.update(6)

        



#================
'''
print("The Earth and Satellites Location after {0} seconds is:".format((2000*6)))
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!
'''
