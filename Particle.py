import math
import numpy as np
import copy

class Particle:
    '''
    placeholder docstring
    '''
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name='Ball',
        mass=1.0,
        G = 6.67408E-11
        ):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.G = G
        

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def update(self, deltaT):
        self.position = self.position + self.velocity*deltaT
        self.velocity = self.velocity + self.acceleration*deltaT

    def updateGravitationalAcceleration(self, body):    
        dist = np.sqrt(((self.position[0]-body.position[0])**2)+((self.position[1]-body.position[1])**2)+((self.position[2]-body.position[2])**2))
        if(dist != 0):
            self.acceleration = (-self.G*body.mass*(self.position-body.position))/(dist**3)

    def kineticEnergy(self):
        K_Energy = 0.5*self.mass*(np.linalg.norm(self.velocity))**2
        return K_Energy
