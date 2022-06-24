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
    plt.title( "Image view >>>" )
    plt.show()

def loadImageAsTensor( path ):
    tensor = ( normalize( invert( rgb_to_grayscale(
        read_image( path ))).type(torch.float32))
    ).unsqueeze_(0)
    return tensor


def weightsCreator( n ):
    ##create an 2d array x*x
#    pattern_list = [i % 2 for i in range( n )]
    pattern_list = [0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0] #25 the best result  


    arr = np.array( pattern_list, dtype = np.float32 )
    arr = np.broadcast_to( arr, (n, n) )
    sh = arr.shape
    if sh[0] != sh[1]:
        print("Error! Result array is't Square matrix")

    ##add two axis in position 0 ant 1
    arr = arr[np.newaxis, np.newaxis, :, : ]  # add axis=0 and axis=1
            
    ##numpy to torch.tensor
    torch_arr = torch.tensor( arr )
                        
    return torch_arr

def getNumpyArray( tensor ):
    return tensor.detach().numpy()[0][0].squeeze()  # >>> one-dimensional numpy array of max values in each row of filtered photo


def viewData( data, title ):
    plt.plot( data, color = "green", linestyle="solid", linewidth = 1, marker = "x")
    plt.title( title )
    plt.show()




























