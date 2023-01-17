# module detect

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image

#NUMPY
import time
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

        maxpoolingImg = nn.MaxPool2d(( 1, shape[3] ))
        y_max = maxpoolingImg( y_filtered )        
                
        return y_max


#class initialization 
ds = detectSomething()


#DETECTING

##detect t-rex
def detectPlayerPosition( tensor, weights ):
    arr_dim = weights.shape[3]
    t_rex_max = ds.getMaxpooledImg( arr_dim, weights, tensor, "v" )
    t_rex_pos = torch.argmax( t_rex_max )

    return t_rex_pos
#    print( f"t_rex_position >>> {t_rex_pos}" )

def detectPlayerPosition_D( tensor, weights ):
    model = nn.Sequential(
            nn.Conv2d( 1, 1, ( 40,40 )),
            nn.MaxPool2d(( 1, 19 ))
    )
    model[0].weight = nn.Parameter( weights ) 

    y = model( tensor )
    y_pos = torch.argmax( y )
                        
    return y_pos
