# module detect

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image

#NUMPY
import numpy as np
from helper_func import *

class detectSomething():

    def getMaxpooledImg( self, arr_dim, weights, tensor, maxpool_axis ):
        
        filteredImg = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))
        filteredImg.weight = nn.Parameter( weights )
        y_filtered = filteredImg( tensor )
        shape = y_filtered.shape

        ###select maxpooling axis
        if maxpool_axis == "v":
            pass
        elif maxpool_axis == "h":
            y_filtered = y_filtered.permute( 0, 1, 3, 2 )
            shape = y_filtered.shape


        maxpoolingImg = nn.MaxPool2d(( 1, shape[3] ))
        y_max = maxpoolingImg( y_filtered )        
                
        return y_max


                
    def getCoordinates( self, y ):
        y_np_arr = getDataArray( y )
        y_mean = np.mean( y_np_arr )
#        viewData( y_np_arr, y_mean, "data visualization" )
#        print( np.where( y_np_arr > y_mean ))
        upper_limit = np.where( y_np_arr > y_mean )[0][0]
#        print( f"upper_limit >>> {upper_limit}" )
#        return y_np_arr        
        return upper_limit

