#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
from helper_func import *
from detect import *
from os import system

system( "clear" )

#LOAD IMAGE AS TENSOR
tensor_cactus  = loadImageAsTensor( "images/mid-3.jpg" )
weights_cactus = loadImageAsTensor( "images/cactus-weights.jpg" )


#class initialization 
ds = detectSomething()


#DETECTING

##detect t-rex
arr_dim = 43
t_rex_pos = ds.getFilteredImg( arr_dim, XXX, XXX )






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





























