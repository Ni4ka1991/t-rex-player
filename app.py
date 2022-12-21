#!/usr/bin/env python3

#PROJECT MODULES
from data import *
from client import *

#OTHER
from os import system
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

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
    global zoneA, zoneB, zoneC, zoneD, zoneE
    img = plt.imshow( catZonesToTensor( zoneA, zoneB, zoneC, zoneD, zoneE ))
    
    animation = FuncAnimation( plt.gcf(), update, frames=10, interval = 1 )
    
    plt.show( ) 
#    return img

def update( frame_i ):
    global frame_tensor
    global zoneA, zoneB, zoneC, zoneD, zoneE
    
    frame_tensor    = getCanvasTensor( browser, canvas )
    zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )
    
    img.set_data( catZonesToTensor( zoneA, zoneB, zoneC, zoneD, zoneE ))
    return img, "figure 1"
    

plot_img = initPlot( )





