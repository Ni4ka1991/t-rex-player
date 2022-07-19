#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
import numpy as np
from helper_func import *
from detect2 import *
from os import system

#system( "clear" )

#SEARCING DATA
## where are we loking for 
tensor_cactus      = loadImageAsTensor( "images/cacti/mid-3.jpg" )
tensor_t_rex       = loadImageAsTensor( "images/t-rex/t-rex-top-1.jpg" )
tensor_distance    = loadImageAsTensor( "images/distance/none-N.jpg" )
tensor_go          = loadImageAsTensor( "images/GO/go_none.jpg" )
### number_tensors
tensor_0          = loadImageAsTensor( "images/numbers/0.jpg" )
tensor_1          = loadImageAsTensor( "images/numbers/1.jpg" )
tensor_2          = loadImageAsTensor( "images/numbers/2.jpg" )
tensor_3          = loadImageAsTensor( "images/numbers/3.jpg" )
tensor_4          = loadImageAsTensor( "images/numbers/4.jpg" )
tensor_5          = loadImageAsTensor( "images/numbers/5.jpg" )
tensor_6          = loadImageAsTensor( "images/numbers/6.jpg" )
tensor_7          = loadImageAsTensor( "images/numbers/7.jpg" )
tensor_8          = loadImageAsTensor( "images/numbers/8.jpg" )
tensor_9          = loadImageAsTensor( "images/numbers/9.jpg" )

## what are we loking for
weights_t_rex  = loadImageAsTensor( "images/masks/t-rex-weights.jpg" )
weights_cactus = loadImageAsTensor( "images/masks/cactus-weights.jpg" )
weights_go     = loadImageAsTensor( "images/masks/go.jpg" )
### number_weights
weights_0     = loadImageAsTensor( "images/masks/numbers/0.jpg" )
weights_1     = loadImageAsTensor( "images/masks/numbers/1.jpg" )
weights_2     = loadImageAsTensor( "images/masks/numbers/2.jpg" )
weights_3     = loadImageAsTensor( "images/masks/numbers/3.jpg" )
weights_4     = loadImageAsTensor( "images/masks/numbers/4.jpg" )
weights_5     = loadImageAsTensor( "images/masks/numbers/5.jpg" )
weights_6     = loadImageAsTensor( "images/masks/numbers/6.jpg" )
weights_7     = loadImageAsTensor( "images/masks/numbers/7.jpg" )
weights_8     = loadImageAsTensor( "images/masks/numbers/8.jpg" )
weights_9     = loadImageAsTensor( "images/masks/numbers/9.jpg" )


#class initialization 
ds = detectSomething()


#DETECTING

##detect t-rex
arr_dim = weights_t_rex.shape[3]
t_rex_max = ds.getMaxpooledImg( arr_dim, weights_t_rex, tensor_t_rex, "v" )
t_rex_pos = torch.argmax( t_rex_max )
print( f"t_rex_position >>> {t_rex_pos}" )

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

## detect status game
getConvTensor = nn.Conv2d( 1, 1, ( 22, 200 ))
getConvTensor.weight = nn.Parameter( weights_go )
conv_result = getConvTensor( tensor_go ).detach()
sq = torch.squeeze( conv_result )
item = sq.item()/100
if item > 1.5:
    print( "GAME OVER!!!" )
else:
    print( f"item >>> {item}" )
    

## detect numbers
getConvTensor = nn.Conv2d( 1, 1, ( 13, 22 ))
getConvTensor.weight = nn.Parameter( weights_0 )
conv_result = getConvTensor( tensor_0 ).detach()
sq = torch.squeeze( conv_result )
item = sq.item()/100
if item > 1.5:
    print( "number was detected correct" )
else:
    print( f"item >>> {item}" )


