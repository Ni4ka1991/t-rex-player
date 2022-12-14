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


def viewImg( img ):
#    img_sqz = img.squeeze(0)
    img_usqz = img.unsqueeze(0)  # if need to view a Zones with shape [x,y] 
    plt.figure()
#    plt.imshow( img_sqz.detach().permute( 1, 2, 0 ), interpolation='nearest', cmap = 'gray' )
    plt.title( "Image view >>>" )
#    plt.imshow( img, cmap = plt.get_cmap( 'gray' ))                     #for display PIL img
    plt.imshow( img_usqz.permute( 1, 2, 0 ), cmap = plt.get_cmap( 'gray' ))   # for display img from tensor
    plt.show()

def loadImageAsTensor( path ):
    tensor = ( normalize( invert( rgb_to_grayscale( read_image( path ))).type(torch.float32) ) ).unsqueeze_(0)
    return tensor

def weightsCreator( row, col ):#22*200
    
    ##create an 2d array 
    pattern_list = [i % 2 for i in range( col )]
    a = np.zeros(( row, col ), dtype = np.float32 )
    arr = a + pattern_list
    
    ##add two axis in position 0 ant 1
    arr = arr[np.newaxis, np.newaxis, :, : ]  # add axis=0 and axis=1
            
    ##numpy to torch.tensor
    torch_arr = torch.tensor( arr )
#    print(torch_arr.type)                    
#    input("hit enter to continue ...")
    return torch_arr

def getDataArray( tensor ):
    arr = tensor.detach().numpy()[0][0].squeeze()  # >>> one-dimensional numpy array of max values in each row of filtered photo
    return arr


def viewData( data_1, data_2, title ):
    plt.plot( data_1, color = "green", linestyle="solid", linewidth = 1, marker = "x")
    
    ###a line viewer
    data = []
    ###loop to view a full lenght line 
    for i in range( 0, len(data_1)):
        data.append(data_2)

    plt.plot( data, color = "red",   linestyle="dashdot", linewidth = 2)
    plt.title( title )
    plt.show()

def splitTensorToZones( frame_tensor ):
    
    zoneA = frame_tensor[0][:, 18:68]  #dino right in the frame
    zoneB = frame_tensor[0][:, 48:96]
    zoneC = frame_tensor[0][:, 96:]
    zoneD = frame_tensor[0][10:21, 577:632]
    zoneE = frame_tensor[0][16:40, 200:400]
    
    return ( zoneA, zoneB, zoneC, zoneD, zoneE )



def catZonesToTensor( zoneA, zoneB, zoneC, zoneD, zoneE ):
    
    zA = torch.clone( zoneA )
    zB = torch.clone( zoneB )
    zC = torch.clone( zoneC )
    zD = torch.clone( zoneD )
    zE = torch.clone( zoneE )

    zA[:, -1] = 1
    zB[:, -1] = 1
    zC[:, -1] = 1
    zD[:, -1] = 1
    zE[:, -1] = 1














