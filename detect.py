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

    
    def getMaxpooledImg( self, arr_dim, weights, tensor, maxpool_axis ):
        
        filteredImg = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))
        filteredImg.weight = nn.Parameter( weights )
        y_filtered = filteredImg( tensor )

        shape = y_filtered.shape

        ###select maxpooling axis
        if maxpool_axis == "v":
            a = 1
            b = shape[3]
        elif maxpool_axis == "h":
            b = 1
            a = shape[3]

        maxpoolingImg = nn.MaxPool2d(( a, b ))
        
        y_max = maxpoolingImg( y_filtered )        
        
        return y_max


        '''        
    def getCoordinates( self, y ):
        
        

        y_max = maxImg( y ).detach().numpy()[0][0].squeeze()  # >>> one-dimensional numpy array of max values in each row of filtered photo
        Y_mean = np.mean( y_max )
        upper_limit = np.where( y_max > Y_mean )[0][0]
        
        return upper_limit
        '''
