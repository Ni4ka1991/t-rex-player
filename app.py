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
t_rex_max = ds.getMaxpooledImg( arr_dim, weights_t_rex, tensor_t_rex, "v" )
t_rex_pos = torch.argmax( t_rex_max )
print( f"t_rex_position >>> {t_rex_pos}" )

## detect imminent threat
arr_dim = 25                                               
cactus_max = ds.getMaxpooledImg( arr_dim, weights_cactus, tensor_cactus, "v" )
input( "Hit enter to continue ..." )
print( cactus_max )





'''
###use oun convolution neuron
weights_vertical =  weightsCreator( arr_dim )

y = ds.getFilteredImg( arr_dim, weights_vertical, tensor_cactus )
vert_limit = ds.getCoordinates( y )
print( f"The vertical border has coordinates: {vert_limit}" )


y_prm = torch.permute( y, ( 0, 1, 3, 2 ))
hor_limit = ds.getCoordinates( y_prm )
print( f"The left horisontal border has coordinates: {hor_limit}" )
'''




























