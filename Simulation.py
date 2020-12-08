import numpy as np
from Particle import Particle
import copy
import scipy.constants as const
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from poliastro import constants
from spiceypy import sxform, mxvg
import matplotlib.pyplot as plt 

# get the time at 5pm on 27th Nov 2019
t = Time("2019-11-27 17:00:00.0", scale="tdb")

# get positions of velocities for the Sun
pos, vel = get_body_barycentric_posvel("sun", t, ephemeris="jpl")

G = const.G
body_counter = 0
bodies = []

bababbooe = 1
fafafooe = 2

if bababbooe == fafafooe:
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

def transformation(pos, vel):
    statevec = [
        pos.xyz[0].to("m").value,
        pos.xyz[1].to("m").value,
        pos.xyz[2].to("m").value,
        vel.xyz[0].to("m/s").value,
        vel.xyz[1].to("m/s").value,
        vel.xyz[2].to("m/s").value
    ]
    trans = sxform("J2000", "ECLIPJ2000", t.jd)
    statevececl = mxvg(trans, statevec, 6, 6)
    position = [statevececl[0], statevececl[1], statevececl[2]]
    velocity = [statevececl[3], statevececl[4], statevececl[5]]
    return (position, velocity)

m_sun = (constants.GM_sun / G).value
pos_sun, vel_sun = get_body_barycentric_posvel("sun", t, ephemeris="jpl")
(pos_sun_2, vel_sun_2) = transformation(pos_sun, vel_sun)
#sun
Sun = Particle(
    pos_sun_2,
    vel_sun_2,
    np.array([0,0,0]),
    'Sun',
    m_sun,
    body_counter
)
bodies.append(Sun)
body_counter = body_counter + 1

m_mercury = (constants.GM_mercury / G).value
pos_mercury, vel_mercury = get_body_barycentric_posvel("mercury", t, ephemeris="jpl")
#mercury
(pos_mercury_2, vel_mercury_2) = transformation(pos_mercury, vel_mercury)
Mercury = Particle(
    pos_mercury_2,
    vel_mercury_2,
    np.array([0,0,0]),
    'Mercury',
    m_mercury,
    body_counter
)
bodies.append(Mercury)
body_counter = body_counter + 1

m_venus = (constants.GM_venus / G).value
pos_venus, vel_venus = get_body_barycentric_posvel("venus", t, ephemeris="jpl")
(pos_venus_2, vel_venus_2) = transformation(pos_venus, vel_venus)
Venus = Particle(
    pos_venus_2,
    vel_venus_2,
    np.array([0,0,0]),
    'Venus',
    m_venus,
    body_counter
)
bodies.append(Venus)
body_counter = body_counter + 1

m_earth = (constants.GM_earth / G).value 
pos_earth, vel_earth = get_body_barycentric_posvel("earth", t, ephemeris="jpl")
#earth
(pos_earth_2, vel_earth_2) = transformation(pos_earth, vel_earth)
Earth = Particle(
    pos_earth_2,
    vel_earth_2,
    np.array([0,0,0]),
    'Earth',
    m_earth,
    body_counter
)
bodies.append(Earth)
body_counter = body_counter + 1

m_moon = (constants.GM_moon / G).value
pos_moon, vel_moon = get_body_barycentric_posvel("moon", t, ephemeris="jpl")
#moon
(pos_moon_2, vel_moon_2) = transformation(pos_moon, vel_moon)
Moon = Particle(
    pos_moon_2,
    vel_moon_2,
    np.array([0,0,0]),
    'Moon',
    m_moon,
    body_counter
)
bodies.append(Moon)
body_counter = body_counter + 1

m_mars = (constants.GM_mars / G).value
pos_mars, vel_mars = get_body_barycentric_posvel("mars", t, ephemeris="jpl")
#mars
(pos_mars_2, vel_mars_2) = transformation(pos_mars, vel_mars)
Mars = Particle(
    pos_mars_2,
    vel_mars_2,
    np.array([0,0,0]),
    'Mars',
    m_mars,
    body_counter
)
bodies.append(Mars)
body_counter = body_counter + 1

m_jupiter = (constants.GM_jupiter / G).value
pos_jupiter, vel_jupiter = get_body_barycentric_posvel("jupiter", t, ephemeris="jpl")
#jupiter
(pos_jupiter_2, vel_jupiter_2) = transformation(pos_jupiter, vel_jupiter)
Jupiter = Particle(
    pos_jupiter_2,
    vel_jupiter_2,
    np.array([0,0,0]),
    'Jupiter',
    m_jupiter,
    body_counter
)
bodies.append(Jupiter)
body_counter = body_counter + 1

m_saturn = (constants.GM_saturn / G).value
pos_saturn, vel_saturn = get_body_barycentric_posvel("saturn", t, ephemeris="jpl")
#saturn
(pos_saturn_2, vel_saturn_2) = transformation(pos_saturn, vel_saturn)
Saturn = Particle(
    pos_saturn_2,
    vel_saturn_2,
    np.array([0,0,0]),
    'Saturn',
    m_saturn,
    body_counter
)
bodies.append(Saturn)
body_counter = body_counter + 1

m_uranus = (constants.GM_uranus / G).value
pos_uranus, vel_uranus = get_body_barycentric_posvel("uranus", t, ephemeris="jpl")
#uranus
(pos_uranus_2, vel_uranus_2) = transformation(pos_uranus, vel_uranus)
Uranus = Particle(
    pos_uranus_2,
    vel_uranus_2,
    np.array([0,0,0]),
    'Uranus',
    m_uranus,
    body_counter
)
bodies.append(Uranus)
body_counter = body_counter + 1

m_neptune = (constants.GM_neptune / G).value
pos_neptune, vel_neptune = get_body_barycentric_posvel("neptune", t, ephemeris="jpl")
#neptune
(pos_neptune_2, vel_neptune_2) = transformation(pos_neptune, vel_neptune)
Neptune = Particle(
    pos_neptune_2,
    vel_neptune_2,
    np.array([0,0,0]),
    'Neptune',
    m_neptune,
    body_counter
)
bodies.append(Neptune)
body_counter = body_counter + 1

m_pluto = (constants.GM_pluto / G).value
pos_pluto, vel_pluto = get_body_barycentric_posvel("pluto", t, ephemeris="jpl")
#pluto
(pos_pluto_2, vel_pluto_2) = transformation(pos_pluto, vel_pluto)
Pluto = Particle(
    pos_pluto_2,
    vel_pluto_2,
    np.array([0,0,0]),
    'Pluto',
    m_pluto,
    body_counter
)
bodies.append(Pluto)
body_counter = body_counter + 1

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

