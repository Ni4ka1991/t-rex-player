# module detect

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image

#NUMPY
import time
import random
import numpy as np
from helper_func import *
from data import *
from os import system

#def detectImminentThreatSize
def detectPlayerPosition( tensor, weights ):
    model = nn.Sequential(
        nn.Conv2d( 1, 1, ( 40,40 )),
        nn.MaxPool2d(( 1, 19 ))
    )
    model[0].weight = nn.Parameter( weights ) 

    y = model( tensor )
    y_pos = torch.argmax( y )

    return y_pos
