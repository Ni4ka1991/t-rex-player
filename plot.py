#plot.py module

import matplotlib.pyplot as plt
from time import time, sleep 

def plotData( frame_tensor ):
#    fig = plt.figure( figsize = ( 30, 20 ))
    plt.axis( "off" )
    img = plt.imshow( frame_tensor[0].numpy() )

    time_1 = time()
    for i in range(10):
        img.set_data( frame_tensor[0].numpy())
    time_2 = time()
    
    plt.show()
    print( time_2 - time_1 )

