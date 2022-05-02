#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
from helper_func import *
from os import system


#LOAD IMAGE AS TENSOR
tensor_cactus  = loadImageAsTensor( "images/stalk-1.jpg" )

weights_cactus = loadImageAsTensor( "images/cactus-weights.jpg" )
#weights_vertical = weightsCreator( 46, 46 )
print( weightsCreator( 46, 46 ))

#view_img( tensor_cactus  )
#view_img( weights_cactus )

def detectImminentThreat( tensor, weights ):
    model = nn.Sequential(
            nn.Conv2d( 1, 1, ( 46, 46 )),  # >>> exit 113x19 img
    )

    model[0].weight = nn.Parameter( weights ) 
    y = model( tensor )
#    y = normalize( y )    
    view_img( y )
    #tensor as numpy 2d array
#    y = y.detach()
#    ny = y.numpy()
#    y2d = ny[0][0]
#    return y2d     #return 2d np_array




#np_array = detectImminentThreat( tensor_cactus, weights_vertical )
#print( np_array )
#searchBorders( np_array )










