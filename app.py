#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torch.nn.functional import normalize
from torchvision.io import read_image
from PIL import Image, ImageOps
from os import system


#PLOT
import matplotlib.pyplot as plt


#LOAD IMAGE AS TENSOR
system( "clear" )

def loadImageAsTensor( path ):
    tensor = ( normalize( invert( rgb_to_grayscale(
        read_image( path ))).type(torch.float32))
    ).unsqueeze_(0)
    print( f"{path} >>> \n{tensor}" )
    print( f"{path} >>> {tensor.shape}" )
    return tensor

tensor_cactus  = loadImageAsTensor( "images/two-1.jpg" )
weights_cactus = loadImageAsTensor( "images/cactus-weights.jpg" )


def detectImminentThreat( tensor, weights ):
    model = nn.Sequential(
            nn.Conv2d( 1, 1, ( 46, 46 )),
            nn.MaxPool2d(( 1, 19 )),
    )

    model[0].weight = nn.Parameter( weights ) 
    y = model( tensor )
    y_pos = torch.argmax(y)









print(detectImminentThreat( tensor_cactus, weights_cactus ))

