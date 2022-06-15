#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
from helper_func import *
from detect import *
from os import system

system( "clear" )

#SEARCING DATA
## where are we loking for 
tensor_cactus  = loadImageAsTensor( "images/cacti/mid-3.jpg" )
tensor_t_rex   = loadImageAsTensor( "images/t-rex/t-rex-top-1.jpg" )
## what are we loking for
weights_t_rex  = loadImageAsTensor( "images/masks/t-rex-weights.jpg" )
weights_cactus = loadImageAsTensor( "images/masks/cactus-weights.jpg" )


#class initialization 
ds = detectSomething()


#DETECTING

##detect t-rex
arr_dim = weights_t_rex.shape[3]
<<<<<<< HEAD
t_rex_filt = ds.getFilteredImg( arr_dim, weights_t_rex, tensor_t_rex )
t_rex_pos = ds.getCoordinates( t_rex_filt )



'''
=======
t_rex_pos = ds.getMaxpooledImg( arr_dim, weights_t_rex, tensor_t_rex, "v" )



>>>>>>> 41e6e4e0f639d47534fd8d34cbd5b63f59edf17b







'''

## detect imminent threat
arr_dim = 25

###use oun convolution neuron
weights_vertical =  weightsCreator( arr_dim )

y = ds.getFilteredImg( arr_dim, weights_vertical, tensor_cactus )
vert_limit = ds.getCoordinates( y )
print( f"The vertical border has coordinates: {vert_limit}" )


y_prm = torch.permute( y, ( 0, 1, 3, 2 ))
hor_limit = ds.getCoordinates( y_prm )
print( f"The left horisontal border has coordinates: {hor_limit}" )
'''




























