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

def weightsCreator( x ):
    ##create an 2d array x*x
    arr = np.zeros(( x , x ), dtype = np.float32 )

    ##search for the middle of an axis=1
    midd = round( int( x/2 ))

    ##view result
#    print( f"midd = {midd}" )
    
    ##zeros padding in column[midd]
    arr[0:x, (midd + 0)] = 1.
    arr[0:x, (midd - 2)] = 1.
    arr[0:x, (midd + 2)] = 1.
    arr[0:x, (midd - 4)] = 1.
    arr[0:x, (midd + 4)] = 1.
    
    ##add two axis in position 0 ant 1
    arr = arr[np.newaxis, np.newaxis, :, : ]  # add axis=0 and axis=1
    
    ##numpy to torch.tensor
    arr = torch.tensor( arr )
    
    return arr



































