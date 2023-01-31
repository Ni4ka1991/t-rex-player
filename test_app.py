#!/usr/bin/env python3

#PROJECT MODULES
from data import *
from helper_func import *
from client import *
#from detect import *
from test_detect import *

#OTHER
from os import system
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

system( "clear" )

img          = None
fig          = None
frame_tensor = None
animation    = None
plot         = None

browser, canvas = connectToClient() 
frame_tensor    = getCanvasTensor( browser, canvas )
zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )

def initPlot(): 
    global img
    global fig
    global animation
    global frame_tensor
    global zoneA, zoneB, zoneC, zoneD, zoneE
    global data_x, data_y
    global plot
    
    img = plt.imshow( zoneE ) #var "img" save the link to the image

    animation = FuncAnimation( plt.gcf(), update, frames=10, interval = 1 )
    
    plt.show( ) 

def update( frame_i ):
    global frame_tensor
    global zoneA, zoneB, zoneC, zoneD, zoneE
    
    frame_tensor    = getCanvasTensor( browser, canvas )
    zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )

    
    img.set_data( zoneE )
    
    detectStatusGame( zoneE, weights_go )

    return img, "figure 1"

plot_img = initPlot( )





