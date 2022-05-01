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

def searchBorders( np_array ):
    print( np_array.shape ) # ( 113, 19 )
    tr_array = np_array.transpose()
    print( tr_array )
    print( tr_array.shape ) # ( 19, 113 )
#    np_mean = numpy.mean( np_array[0] )
    #1. np_array.shape
    #2. search column borders
    #3. search string borders
    #4. intersection points

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
#    y = normalize( y )    

    #tensor as numpy 2d array
    y = y.detach()
    ny = y.numpy()
    y2d = ny[0][0]
    return y2d     #return 2d np_array




np_array = detectImminentThreat( tensor_cactus, weights_cactus )
#print( np_array )
searchBorders( np_array )










