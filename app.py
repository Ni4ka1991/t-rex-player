#!/usr/bin/env python3

#PROJECT MODULES
from data import *
from client import *

#OTHER
from os import system
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
'''
v_br, v_dr = getChromeVersion()
print( f"Browser version >>> {v_br}, \nDriver version  >>> {v_dr}" )

'''
system( "clear" )

img          = None
frame_tensor = None
animation    = None
browser, canvas = connectToClient() 
frame_tensor    = getCanvasTensor( browser, canvas )
zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )

def initPlot(): 
    global img
    global animation
    global frame_tensor
    img = plt.imshow( frame_tensor[0].numpy() )
    
    animation = FuncAnimation( plt.gcf(), update, frames=10, interval = 1 )
    
    plt.show( ) 
#    return img

def update( frame_i ):
    global frame_tensor
    global zoneA, zoneB, zoneC, zoneD, zoneE
    
    frame_tensor    = getCanvasTensor( browser, canvas )
    zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )
    
    img.set_data( zoneA[0].numpy() )
    return img, "figure 1"
    

plot_img = initPlot( )





