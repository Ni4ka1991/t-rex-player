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

def view_img( img ):
    img_sqz = img.squeeze(0)
    plt.figure()
    plt.imshow( img_sqz.detach().permute( 1, 2, 0 ), interpolation='nearest', cmap = 'gray' )
    plt.show()

def loadImageAsTensor( path ):
    tensor = ( normalize( invert( rgb_to_grayscale(
        read_image( path ))).type(torch.float32))
    ).unsqueeze_(0)
#    print( f"{path} >>> \n{tensor}" )
#    print( f"{path} >>> {tensor.shape}" )
    return tensor

tensor_cactus  = loadImageAsTensor( "images/two-1.jpg" )
weights_cactus = loadImageAsTensor( "images/cactus-weights.jpg" )

#view_img( tensor_cactus )
#view_img( weights_cactus )

def detectImminentThreat( tensor, weights ):
    model = nn.Sequential(
            nn.Conv2d( 1, 1, ( 46, 46 )),  # >>> exit 113x19 img
#            nn.AvgPool2d(( 113, 19 )),
    )

    model[0].weight = nn.Parameter( weights ) 
    y = model( tensor )
#    y_pos = torch.argmax( y )
#    print( f"y.shape >>> {y.shape}" )
#    view_img( y )
#    y = normalize( y )
#    print( y )
#    print( y.shape )
    print( f"y[0][0][0] >>> \n{y[0][0][0]}" )
    print( f"y[0][0][1] >>> \n{y[0][0][1]}" )
#    print( y[0][0][0][1] )
#    return y_pos    







print(detectImminentThreat( tensor_cactus, weights_cactus ))

