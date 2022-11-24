#!/usr/bin/env python3
#plot-test.py module


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time, sleep 
import numpy as np
from time import time

tensor = np.random.randn( 10, 10 )

def update( frame_i ):
    t = np.random.randn( 350, 700 )
    img.set_data( t )
#    img.set_array( t )
    return img, "figure 1"



img = plt.imshow( tensor )

animation = FuncAnimation( plt.gcf(), update, frames=range(100), interval = 1 )

plt.show()


