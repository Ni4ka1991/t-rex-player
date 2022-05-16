#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
from helper_func import *
from os import system

system( "clear" )
arr_dim = 25

#LOAD IMAGE AS TENSOR
tensor_cactus  = loadImageAsTensor( "images/mid-3.jpg" )
weights_cactus = loadImageAsTensor( "images/cactus-weights.jpg" )

#CREATE OUN CONVOLUTION NEURON
weights_vertical =  weightsCreator( arr_dim )
#print( weightsCreator( arr_dim ))
#weightsCreator( arr_dim )

#VIEW IMG
#view_img( tensor_cactus  )
#view_img( weights_cactus )






#MODEL
def detectImminentThreat( tensor, weights, arr_dim ):     #arr_dim => filter dimentions
    
    filtered_img = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))      #( 1 -> grey scale input, 1 -> grey scale output, arr_dim -> filter dimentions ) 
    
    filtered_img.weight = nn.Parameter( weights ) 
    
    y = filtered_img( tensor )
    view_img( y )
#    avg_img = nn.AvgPool2d(( 1, 40 ))
    


np_array = detectImminentThreat( tensor_cactus, weights_vertical, arr_dim )
