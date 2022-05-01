#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torch.nn.functional import normalize
from torchvision.io import read_image
from PIL import Image, ImageOps
from os import system

#OTHER
import matplotlib.pyplot as plt
import numpy
from os import system


#LOAD IMAGE AS TENSOR
system( "clear" )

def view_img( img ):
    img_sqz = img.squeeze(0)
    plt.figure()
    plt.imshow( img_sqz.detach().permute( 1, 2, 0 ), interpolation='nearest', cmap = 'gray' )
    plt.show()

def loadImageAsTensor( path ):
    tensor = ( normalize( invert( rgb_to_grayscale(
        read_image( path ))).type(torch.float32))
    ).unsqueeze_(0)
    return tensor

tensor_cactus  = loadImageAsTensor( "images/two-1.jpg" )
weights_cactus = loadImageAsTensor( "images/cactus-weights.jpg" )


def detectImminentThreat( tensor, weights ):
    model = nn.Sequential(
            nn.Conv2d( 1, 1, ( 46, 46 )),  # >>> exit 113x19 img
    )

    model[0].weight = nn.Parameter( weights ) 
    y = model( tensor )
    
    #tensor as numpy 2d array
    y = y.detach()
    ny = y.numpy()
    y2d = ny[0][0]

    #search left border
    print( f"\ny2d[0] >>> {y2d[0]}\n" )
    border = 0
    y_mean = numpy.mean( y2d[0] )
    for i in y2d[0]:
        if i >= y_mean:
            border = i
            print( f"border = {border}" )
            break
#    return y_mean

y = detectImminentThreat( tensor_cactus, weights_cactus )
print(y)
