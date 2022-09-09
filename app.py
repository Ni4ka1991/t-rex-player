#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
import time
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
    
## detect numbers
getConvTensor = nn.Conv2d( 1, 1, ( 11, 13 ))
n_1 = int( input( "Enter the number_1 from the range 0...9 >>>" ))
#n_1 = 0
getConvTensor.weight = nn.Parameter( weights_list[ n_1 ])
n_2 = int( input( "Enter the number_2 from the range 0...9 >>>" ))
#n_2 = 2
conv_result = getConvTensor( tensors_list[ n_2 ] ).detach()
sq = torch.squeeze( conv_result )
item = sq.item()*10
print( f" item >>> {item}" )
if item <= 109:
    print( "Numbers are different " )
else:
    print( "Numbers match" )
'''

## detect score
   ### Caution! Number ONE is 8 pixels wide, another numbers has 9 pixels wide
print( f"tensor_score 00362       >>> {tensor_score}" )
print( f"tensor_score 00362 shape >>> {tensor_score.shape}" )

### tensor to array
tensor_score_np_array = tensor_score.detach().to('cpu').numpy().squeeze()  # 

digit = tensor_score_np_array[ 0, 10 ]
input( "Hit ENTER ..." )
print( f"first digit     >>> {digit}" )


getConvTensor = nn.Conv2d( 1, 1, ( 55, 13 ))
getConvTensor.weight = nn.Parameter( weights_list[ 0 ])            #image with dimensions 11x13

conv_result = getConvTensor( tensor_score ).detach()               #score image 00362.jpg

#print( conv_result )





