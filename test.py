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
print( f"number_list >>> ls -l >>> {numbs_list}"  )
print( f"len of numds_list => {len(numbs_list)}" )
print( f"len of tensors_list >> {len(tensors_list)}"  )
print( f"tensors_list[4] vvv\n {tensors_list[4]}" )
input( "Hit Enter ..." )
print( f"\nlen of weights_list => {len(weights_list)}" )
print( f"weights_list[4] vvv\n {weights_list[4]}" )
