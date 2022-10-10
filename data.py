# data module

from helper_func import *
import os

from PIL import Image, ImageOps

#SEARCING DATA
## where are we loking for 
tensor_cactus      = loadImageAsTensor( "images/cacti/mid-3.jpg" )
tensor_t_rex       = loadImageAsTensor( "images/t-rex/t-rex-top-1.jpg" )
tensor_distance    = loadImageAsTensor( "images/distance/none-N.jpg" )
tensor_go          = loadImageAsTensor( "images/GO/go_none.jpg" )
tensor_score       = loadImageAsTensor( "images/scores/00042.jpg" )
#tensor_frame       = loadImageAsTensor( "images/frames/frame.jpeg" )


### number_tensors
path_numbers = "images/numbers/"
numbs_list = os.listdir( path_numbers )                                         #len( numbs_list ) => 12
tensors_list = []
for i in range( 0 , len( numbs_list )):                                         #range( 0, 12 )
    tensors_list.append( loadImageAsTensor( f"{path_numbers}{numbs_list[i]}" ))

## what are we loking for
weights_t_rex  = loadImageAsTensor( "images/masks/t-rex-weights.jpg" )
weights_cactus = loadImageAsTensor( "images/masks/cactus-weights.jpg" )
weights_go     = loadImageAsTensor( "images/masks/go.jpg" )

### number_weights
path_weights_numbers = "images/masks/numbers/"
numbs_list = os.listdir( path_weights_numbers )
weights_list = []

for i in range( 0 , len( numbs_list )):
    weights_list.append( loadImageAsTensor( f"{path_numbers}{numbs_list[i]}" ))

