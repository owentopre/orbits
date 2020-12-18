Particle.py - Class containing methods for updating the various parameters of the particle (see included docstring)
Bodies.py - File containing the initial conditions of all bodies to be simulated, passed to other files as the array: 'bodies'
Plot.py - Script the can show a graph of any set of bodies simulated
Simulation.py - Script that runs a simulation on the bodies in the 'bodies' array with a number of variables on the parameters of this simulation (see guide below to run)

To run the simulation you must first run the bodies.py file to load the initial conditions from JPL Horizons (if using the bodies already supplied in the file)

Then the Simulation.py file should be run with time scale, step and approximation method (1 for Euler, 2 for Euler-Cromer and 3 for Verlet)  selected beforehand

Then list the bodies you wish to plot in the Plot.py 'planets' array (using their index in the 'bodies' array from Bodies.py)

Run Plot.py to show a graph of the xy positions of the bodies supplied
