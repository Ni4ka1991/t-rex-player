# module test_detect

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image

#NUMPY
import random
import numpy as np
from helper_func import *
from data import *
from os import system
def detectStatusGame( tensor, weights ):
    tensor = invert( tensor.unsqueeze(0))
    getConvTensor = nn.Conv2d( 1, 1, ( 22, 200 ))
    getConvTensor.weight = nn.Parameter( weights )
    conv_result = getConvTensor( tensor ).detach()
    sq = torch.squeeze( conv_result )
    item = sq.item()/100
    print( ">"*20, item )

    '''
    if item > 1.5:
        print( "GAME OVER!!!" )
    else:
        print( f" <<< CONTINUE >>>" )
    '''
