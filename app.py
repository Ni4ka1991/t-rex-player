#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
import random
import numpy as np
from helper_func import *
from data import *
from detect2 import *
from os import system

#system( "clear" )

#class initialization 
ds = detectSomething()


#DETECTING
'''
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
    print( f" <<< CONTINUE >>>" )
    
'''
## detect numbers
for i in range( 1, 16 ):
    getConvTensor = nn.Conv2d( 1, 1, ( 13, 22 ))
    getConvTensor.weight = nn.Parameter( weights_list[random.randint( 0, len(tensors_list)-1)] )
    conv_result = getConvTensor( tensors_list[random.randint( 0, len(weights_list)-1)] ).detach()
    sq = torch.squeeze( conv_result )
    item = sq.item()*10
    print( f"tensor, weights  >>> {item}" )













