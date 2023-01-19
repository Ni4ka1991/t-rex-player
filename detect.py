# module detect

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image

#NUMPY
import random
import numpy as np
from helper_func import *
from data import *
from os import system

class detectSomething():

    def getMaxpooledImg( self, arr_dim, weights, tensor, maxpool_axis ):
        filteredImg = nn.Conv2d( 1, 1, ( arr_dim, arr_dim ))
        filteredImg.weight = nn.Parameter( weights )

        y_filtered = filteredImg( tensor )
        shape = y_filtered.shape

        ###select maxpooling axis
        if maxpool_axis == "v":
            pass
        elif maxpool_axis == "h":
            y_filtered = y_filtered.permute( 0, 2, 1 )
            shape = y_filtered.shape


        maxpoolingImg = nn.MaxPool2d(( 1, shape[2] ))
        y_max = maxpoolingImg( y_filtered )        

        return y_max

                
    def getCoordinates( self, y ):
        y_np_arr = getDataArray( y )
        y_mean = np.mean( y_np_arr )
        y_max = np.max( y_np_arr )
#        viewData( y_np_arr, y_mean, "data visualization" )
#        print( np.where( y_np_arr > y_mean ))
        detect_limit = ( y_mean + y_max ) / 2
        upper_limit = np.where( y_np_arr > detect_limit )[0][0]
#        return y_np_arr        
        return upper_limit

#class initialization 
ds = detectSomething()

#DETECTING
def detectPlayerPosition( tensor, weights ):
    arr_dim = weights.shape[3]
    t_rex_max = ds.getMaxpooledImg( arr_dim, weights, tensor, "v" )
    t_rex_pos = torch.argmax( t_rex_max )

    return t_rex_pos

def detectImminentThreat( tensor, weights ):

    arr_dim = weights.shape[3]                                               
    print("arr_dim cactus >>>", arr_dim )
    cactus_max = ds.getMaxpooledImg( arr_dim, weights, tensor, "v" )
    cactus_v_border = ds.getCoordinates( cactus_max )

    print( f"Imminent threat height. >>> {cactus_v_border}" )
#    return cactus_v_border

'''
## detect dictance to cactus
arr_dim = weights_cactus.shape[3]
cactus_max = ds.getMaxpooledImg( arr_dim, weights_cactus, tensor_distance, "h" )
cactus_first_threat = ds.getCoordinates( cactus_max )
print( f"Position of first threat >>> {cactus_first_threat}" )

## detect status game
getConvTensor = nn.Conv2d( 1, 1, ( 22, 200 ))
getConvTensor.weight = nn.Parameter( weights_go )
conv_result = getConvTensor( tensor_go ).detach()
sq = torch.squeeze( conv_result )
item = sq.item()/100
if item > 1.5:
    print( "GAME OVER!!!" )
else:
    print( f" <<< CONTINUE >>>" )
    
## detect numbers
getConvTensor = nn.Conv2d( 1, 1, ( 13, 11 ))
n_1 = int( input( "Enter the number_1 from the range 0...9 >>>" ))
#n_1 = 0
getConvTensor.weight = nn.Parameter( weights_list[ n_1 ])
n_2 = int( input( "Enter the number_2 from the range 0...9 >>>" ))
#n_2 = 2
conv_result = getConvTensor( tensors_list[ n_2 ] ).detach()
sq = torch.squeeze( conv_result )
item = sq.item()*10
print( f" item >>> {item}" )
if item <= 109:
    print( "Numbers are different " )
else:
    print( "Numbers match" )



#def ...
## detect score
   ### Caution! Number ONE is 8 pixels wide, another numbers has 9 pixels wide
tensor_score_np_array = tensor_score.detach().to('cpu').numpy().squeeze()              #transform score tensor to numpy array 

sc = 0
for i in range( 5 ):
    
    digit = tensor_score_np_array[ :, i * 11: ( i + 1 ) * 11 ]                         #isolate first difit from score tensor
    x_digit = torch.from_numpy( digit ).unsqueeze(0).unsqueeze(0)                      #transform numpy digit to 4-dimention tensor
    getConvTensor = nn.Conv2d( 1, 1, ( 13, 11 ))
    
    for k in range( 10 ):
        getConvTensor.weight = nn.Parameter( weights_list[ k ])                     
        conv_result = getConvTensor( x_digit ).detach().squeeze()          
        if conv_result > 10:
            sc = sc + k * 10 ** ( 5 - 1 - i )
print(sc)
'''


