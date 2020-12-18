import numpy as np
from Particle import Particle
import copy
import scipy.constants as const
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from poliastro import constants
from spiceypy import sxform, mxvg

# get the time at 5pm on 27th Nov 2019
t = Time("2019-11-27 17:00:00.0", scale="tdb")

G = const.G
body_counter = 0
bodies = []

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
#venus
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