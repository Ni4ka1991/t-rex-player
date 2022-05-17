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
def detectImminentThreat( tensor, weights, arr_dim ):         #arr_dim => filter dimentions
    
    ##convolution the image 
    filteredImg = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))      #( 1 -> grey scale input, 1 -> grey scale output, arr_dim -> filter dimentions ) 
    
    filteredImg.weight = nn.Parameter( weights )              #use predefined filter names "weights_vertical" in this case

    y_filtered = filteredImg( tensor )                        # >>> y 
    y_shape = y_filtered.shape                                # >>> torch.Size([1, 1, 134, 40]) 

    ##average pooling convolution
    avgImg = nn.AvgPool2d(( 1, y_shape[3] ))
    
    y_avg = avgImg( y_filtered ) 

    ##
    y = y_filtered.detach()
    print( y )
#    view_img( y_avg )
    


np_array = detectImminentThreat( tensor_cactus, weights_vertical, arr_dim )
