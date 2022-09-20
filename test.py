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

system("clear")
'''
print( f"number_list >>> ls -l >>> {numbs_list}"  )
print( f"len of numds_list => {len(numbs_list)}" )
print( f"len of tensors_list >> {len(tensors_list)}"  )
print( f"tensors_list[4] vvv\n {tensors_list[4]}" )
input( "Hit Enter ..." )
print( f"\nlen of weights_list => {len(weights_list)}" )
print( f"weights_list[4] vvv\n {weights_list[4]}" )
#x = torch.zeros( 2, 1, 2, 1, 2 )
x = torch.ones( 2, 1 )   # 2 >>> rows, 4 >>> colums
print( f" x >>> \n{x}" )
y = torch.squeeze( x )
print( f" y >>> \n{y}" )
print( "*"*10 )
x = torch.ones( 2, 4 )   # 2 >>> rows, 4 >>> colums
print( f" x >>> \n{x}" )
y = torch.squeeze( x )
print( f" y >>> \n{y}" )
x = torch.zeros( 2, 1, 2 )
print( f" x >>> \n{x}" )
y = torch.squeeze(x)
'''

a = 4
b = 6
c = 8
d = 1
e = 2
# >>>> 46812
print( f" number >> 46812" )
score = 0
score = score + a * 10 ** 4
print(score)
score = score + b * 10 ** 3    
print(score)
score = score + c * 10 ** 2
print(score)
score = score + d * 10 ** 1
print(score)
score = score + e * 10 ** 0
print(score)

#for i in range(5):
#    score += x * 10 ** ( 5 - 1 - i )



