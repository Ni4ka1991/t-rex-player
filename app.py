#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
import numpy as np
from helper_func import *
from detect import *
from os import system

system( "clear" )

#SEARCING DATA
## where are we loking for 
tensor_cactus     = loadImageAsTensor( "images/cacti/mid-3.jpg" )
tensor_t_rex      = loadImageAsTensor( "images/t-rex/t-rex-top-1.jpg" )
tensor_distance   = loadImageAsTensor( "images/distance/near.jpg" )
#view_img( tensor_distance )

## what are we loking for
weights_t_rex  = loadImageAsTensor( "images/masks/t-rex-weights.jpg" )
weights_cactus = loadImageAsTensor( "images/masks/cactus-weights.jpg" )


#class initialization 
ds = detectSomething()


#DETECTING

'''
##detect t-rex
arr_dim = weights_t_rex.shape[3]
t_rex_max = ds.getMaxpooledImg( arr_dim, weights_t_rex, tensor_t_rex, "v" )
t_rex_pos = torch.argmax( t_rex_max )
print( f"t_rex_position >>> {t_rex_pos}" )

'''
## detect imminent threat
arr_dim = weights_cactus.shape[3]                                               
cactus_max = ds.getMaxpooledImg( arr_dim, weights_cactus, tensor_cactus, "v" )
cactus_v_border = ds.getCoordinates( cactus_max )
print( f"Imminent threat height. >>> {cactus_v_border}" )

## detect dictance to cactus
arr_dim = weights_cactus.shape[3]
cactus_max = ds.getMaxpooledImg( arr_dim, weights_cactus, tensor_distance, "h" )
cactus_first_threat = ds.getCoordinates( cactus_max )
print( f"Position of first threat >>> {cactus_first_threat}" )

