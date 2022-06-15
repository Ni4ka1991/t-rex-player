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

    
    def getFilteredImg( self, arr_dim, weights, tensor ):
        
        ##convolution the image 
        filteredImg = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))      #( 1 -> grey scale input, 1 -> grey scale output, arr_dim -> filter dimentions ) 
        filteredImg.weight = nn.Parameter( weights )              #use predefined filter names "weights_vertical" in this case
        y_filtered = filteredImg( tensor )                        # >>> y 
        
        return y_filtered

    
    def getCoordinates( self, y ):
        
        shape = y.shape
        
        ##pooling convolution
        maxImg = nn.MaxPool2d(( 1, shape[3] ))

        
        y_max = maxImg( y ).detach().numpy()[0][0].squeeze()  # >>>get one-dimensional numpy array of max values in each row of filtered photo
        print( y_max.shape )
        '''
        Y_mean = np.mean( y_max )
        upper_limit = np.where( y_max > Y_mean )[0][0]
        
        return upper_limit
        '''

