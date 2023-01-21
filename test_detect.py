# module detect

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image

#NUMPY
import random
import numpy as np
from helper_func import *
from data import *
from os import system

class detectSomething():

    def getMaxpooledImg( self, arr_dim, weights, tensor, maxpool_axis ):
        filteredImg = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))
        filteredImg.weight = nn.Parameter( weights )

        y_filtered = filteredImg( tensor )
        shape = y_filtered.shape
#        print("conv2d cactus >>>>", shape )

        maxpoolingImg = nn.MaxPool2d(( 1, shape[2] ))
        y_max = maxpoolingImg( y_filtered )        

        print("maxpoolingImg >>>", y_max )
        return y_max
                
    def getCoordinates( self, y ):
 #       print( "input data - tensor >>>", y )
        y_np_arr = getDataArray( y )                              #get array from tensor
 #       print( "array printed here >>>\n", y_np_arr )
 #       input( "hit Enter to continue ..." )
        y_mean = np.mean( y_np_arr )
 #       print( "y_mean >>>", y_mean )
        y_max = np.max( y_np_arr )
 #       print( "y_max >>>", y_max )
        detect_limit = ( y_mean + y_max ) / 2
#        print( "detect_limit >>>", detect_limit )
        upper_limit = np.where( y_np_arr > detect_limit )[0][0]
        print( "upper_limit >>>", upper_limit )
        return upper_limit

#class initialization 
ds = detectSomething()

#DETECTING
def detectImminentThreat( tensor, weights ):

    arr_dim = weights.shape[3]                                               
#    print("arr_dim cactus >>>", arr_dim )
    cactus_max = ds.getMaxpooledImg( arr_dim, weights, tensor, "v" )   #get maxpooling tensor
    cactus_v_border = ds.getCoordinates( cactus_max )

    print( f"Imminent threat height. >>> {cactus_v_border}" )
    return cactus_v_border

