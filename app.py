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
fig          = None
frame_tensor = None
animation    = None
plot         = None

browser, canvas = connectToClient() 
frame_tensor    = getCanvasTensor( browser, canvas )
zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )

data_x = [ i for i in range(150) ]
data_y = [ i for i in range(150) ]

def initPlot(): 
    global img
    global fig
    global animation
    global frame_tensor
    global zoneA, zoneB, zoneC, zoneD, zoneE
    global data_x, data_y
    global plot
    
    fig = plt.figure(figsize = ( 5, 5 ))
    rows = 3
    cols = 1

    fig.add_subplot( rows, cols, 1 )
    img = plt.imshow( catZonesToTensor( zoneA, zoneB, zoneC, zoneD, zoneE )) #var "img" save the link to the image

    fig.add_subplot( rows, cols, 2 )
    plot, = plt.plot( data_x, data_y )                                       #var "plot" save 2 links

    animation = FuncAnimation( plt.gcf(), update, frames=10, interval = 1 )
    
    plt.show( ) 
#    return img

def update( frame_i ):
    global frame_tensor
    global zoneA, zoneB, zoneC, zoneD, zoneE
    
    frame_tensor    = getCanvasTensor( browser, canvas )
    zoneA, zoneB, zoneC, zoneD, zoneE = splitTensorToZones( frame_tensor )
    
    img.set_data( catZonesToTensor( zoneA, zoneB, zoneC, zoneD, zoneE ))
    plot.set_data( data_x, data_y )
    return img, "figure 1"
    

plot_img = initPlot( )





