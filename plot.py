#plot.py module

import matplotlib.pyplot as plt
from time import time, sleep 

def initPlot( frame_tensor ):
#    fig = plt.figure( figsize = ( 30, 20 ))
    
    plt.axis( "off" )
    img = plt.imshow( frame_tensor[0].numpy() )
    plt.show()

    return img

    

def updatePlot( frame_tensor, img ):
    img.set_data( frame_tensor[0].numpy())
