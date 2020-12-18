import matplotlib.pyplot as plt 
import numpy as np

Data = np.load("SimulationLog.npy", allow_pickle=True)  

planets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #List bodies to be plotted here, using their index in the bodies array, ie. their index particle attribute

x = []
y = []

for a in planets:
    for b in range(len(Data)):
        x.append(Data[b][a + 1].position[0])
        y.append(Data[b][a + 1].position[1])
    plt.plot(
        x,
        y,
        label = Data[1][a + 1].name
    )
    x = []
    y = []
plt.legend()
plt.show()