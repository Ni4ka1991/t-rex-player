# module detect

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image

#NUMPY
import numpy as np


class detectSomething():

    
    def getMaxpooledImg( self, arr_dim, weights, tensor, "maxpool_axis" ):
         
         model = nn.Sequential(
                nn.Conv2d( 1, 1, ( arr_dim, arr_dim )),
                nn.MaxPool2d(( a, b )),
        )
        
        model[0].weight = nn.Parameter( weights ) 
        
        if "maxpool_axis" == "v":
            a = 1 and b = shape[3]
        elif "maxpool_axis" == "h":
            a = shape[3] and b = 1
        
        y = model( tensor )
        return y
    
    def getCoordinates( self, y ):
        
        y_max = maxImg( y ).detach().numpy()[0][0].squeeze()  # >>> one-dimensional numpy array of max values in each row of filtered photo
        Y_mean = np.mean( y_max )
        upper_limit = np.where( y_max > Y_mean )[0][0]
        
        return upper_limit
        

