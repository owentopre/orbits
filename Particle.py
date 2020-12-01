import math
import numpy as np
import copy
G = 6.67408E-11

class Particle:
    '''
    A class representing a particle.
    
    Inputs
    ------
    position : array
          A numpy array with 3 floats representing the particle's starting position in 3d space
    velocity : array
        A numpy array with 3 floats representing the particle's starting velocity through 3d space
    acceleration : array
        A numpy array with 3 floats representing the particle's starting acceleration through 3d space
    name : str
        A string that is used as a name for the particle
    mass : float
        A floating point number used as the particle's mass
    G : float
        The universal gravitational constant

    Methods:
    update
    updateGravitationalAcceleration
    kineticEnergy

    '''
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name='Ball',
        mass=1.0,
        index = 0
        ):
        """
        Construsts the parameters of the particle, and gives defaults unless they are overwritten

        Parameters
        ----------
            position : array
                A numpy array with 3 floats representing the particle's starting position in 3d space
            velocity : array
                A numpy array with 3 floats representing the particle's starting velocity through 3d space
            acceleration : array
                A numpy array with 3 floats representing the particle's starting acceleration through 3d space
            name : str
                A string that is used as a name for the particle
            mass : float
                A floating point number used as the particle's mass
            G : float
                The universal gravitational constant
            
        """
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.G = G
        self.index = index
        
        

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def update(self, deltaT):
        #temporary as is only Euler algorithm  
        self.position = self.position + self.velocity*deltaT
        self.velocity = self.velocity + self.acceleration*deltaT

    def updateGravitationalAcceleration(self, body):  
        
        # dist = np.sqrt(((self.position[0]-body.position[0])**2)+((self.position[1]-body.position[1])**2)+((self.position[2]-body.position[2])**2))
        # if(dist != 0):
        #     self.acceleration = (-self.G*body.mass*(self.position-body.position))/(dist**3)
        dist = np.sqrt(((self.position[0]-body.position[0])**2)+((self.position[1]-body.position[1])**2)+((self.position[2]-body.position[2])**2))
        self.acceleration[0] += (-self.G*body.mass*(self.position[0]-body.position[0]))/(dist**3)
        self.acceleration[1] += (-self.G*body.mass*(self.position[1]-body.position[1]))/(dist**3)
        self.acceleration[2] += (-self.G*body.mass*(self.position[2]-body.position[2]))/(dist**3)
        

    def kineticEnergy(self):
        K_Energy = 0.5*self.mass*(np.linalg.norm(self.velocity))**2
        return K_Energy
