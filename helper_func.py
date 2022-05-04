#helper_func.py module

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert
from torch.nn.functional import normalize
from torchvision.io import read_image
from os import system

#OTHER
import matplotlib.pyplot as plt
import numpy as np
from os import system


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


def searchBorders( np_array ):
    print( np_array.shape ) # ( 113, 19 )
    tr_array = np_array.transpose()
    print( tr_array )
    print( tr_array.shape ) # ( 19, 113 )
    shape = tr_array.shape


'''
    for i in range( 0, shape[0] ):
        mean_str = numpy.mean( tr_array[i] )
        print( f"mean in str {i} >>> {mean_str}" )    
'''

    #1. np_array.shape
    #2. search column borders
    #3. search string borders
    #4. intersection points

def weightsCreator( n ):
    ##create an 2d array x*x
    pattern_list = [i % 2 for i in range( n )]
    arr = np.array( pattern_list, dtype = np.float32 )
    arr = np.broadcast_to( arr, (n, n) )
    
    ##add two axis in position 0 ant 1
    arr = arr[np.newaxis, np.newaxis, :, : ]  # add axis=0 and axis=1
            
    ##numpy to torch.tensor
    arr = torch.tensor( arr )
                        
    return arr

































