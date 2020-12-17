import math
import numpy as np
import copy
import scipy.constants as const

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
        index = 0,
        G = float(const.G),
        P_Energy=0.0
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
            
            
        """
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.index = index
        self.G = G
        self.P_Energy = P_Energy
        

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def update_1(self, deltaT):
        #Euler Approximation
        
        self.position = self.position + self.velocity*deltaT
        self.velocity = self.velocity + self.acceleration*deltaT

    def update_2(self, deltaT):
        #Euler-Cromer Approximation
        self.velocity = self.velocity + self.acceleration*deltaT
        self.position = self.position + self.velocity*deltaT
        
    def updateGravitationalAcceleration(self, body):
        dist = np.sqrt(((self.position[0]-body.position[0])**2)+((self.position[1]-body.position[1])**2)+((self.position[2]-body.position[2])**2))
        self.acceleration += (-self.G*body.mass*(self.position-body.position))/(dist**3)       

    def kineticEnergy(self):
        K_Energy = 0.5*self.mass*(np.linalg.norm(self.velocity))**2 
        return K_Energy

    def potentialEnergy(self, body):
        dist = np.sqrt(((self.position[0]-body.position[0])**2)+((self.position[1]-body.position[1])**2)+((self.position[2]-body.position[2])**2))
        self.P_Energy += (-self.G*body.mass*self.mass)/dist

    def momentum(self):
        momentum = self.mass*self.velocity
        return momentum