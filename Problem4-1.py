import math as mt
import numpy as np
import sys
import matplotlib.pyplot as plt

def PlotTrajectory (ho,vo,theta,ax,ay):
    
    if ay == 0:
        sys.exit('Please input a non zero vertical acceleration component. Thank you')

    realth= mt.radians(theta)
    vox = vo*mt.cos(realth)
    voy = vo*mt.sin(realth)
    d = mt.sqrt(voy**2 - 4*(1/2*-ay)*ho)
    t1 = (-voy + d )/ -ay
    t2 = (-voy - d )/ -ay
    
    if t1 <= 0:
        t1 = t2
        x = vox*(np.linspace(0,t1)) + 1/2*ax*np.linspace(0,t1)**2
        y = voy*np.linspace(0,t1) + 1/2*-ay*np.linspace(0,t1)**2
    else:
        x = vox*(np.linspace(0,t1)) + 1/2*ax*np.linspace(0,t1)**2
        y = voy*np.linspace(0,t1) + 1/2*-ay*np.linspace(0,t1)**2
        
    plt.plot(x,y)
    plt.xlabel('Trajectory as it goes in the X direction')
    plt.ylabel('Trajectory as it goes in the Y direction')
    plt.grid()
    plt.show()