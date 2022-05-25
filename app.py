#!/usr/bin/env python3

#TORCH
import torch
from torch import nn

#OTHER
from helper_func import *
from os import system

system( "clear" )
arr_dim = 25


#LOAD IMAGE AS TENSOR
tensor_cactus  = loadImageAsTensor( "images/mid-3.jpg" )
weights_cactus = loadImageAsTensor( "images/cactus-weights.jpg" )

#CREATE OUN CONVOLUTION NEURON
weights_vertical =  weightsCreator( arr_dim )
#print( weightsCreator( arr_dim ))
#weightsCreator( arr_dim )

#VIEW IMG
#view_img( tensor_cactus  )
#view_img( weights_cactus )






#MODEL
class detectImminentThreat():
    
    def getFilteredImg( self, arr_dim, weights, tensor ):
        
        ##convolution the image 
        filteredImg = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))      #( 1 -> grey scale input, 1 -> grey scale output, arr_dim -> filter dimentions ) 
        filteredImg.weight = nn.Parameter( weights )              #use predefined filter names "weights_vertical" in this case
        y_filtered = filteredImg( tensor )                        # >>> y 
        
        return y_filtered

    
    def getCoordinates( self, y ):
        
        shape = y.shape
        
        ##average pooling convolution
        maxImg = nn.MaxPool2d(( 1, shape ))
        y_max = maxImg( y ).detach().numpy()[0][0].squeeze()  # >>> one-dimensional numpy array of max values in each row of filtered photo
        Y_mean = np.mean( y_max )
        upper_limit = np.where( y_max > Y_mean )[0][0]
        
        return upper_limit
    



dit = detectImminentThreat()
y = dit.getFilteredImg( arr_dim, weights_vertical, tensor_cactus )
print( dit.getCoordinates( y ))
