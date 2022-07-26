# data module

from helper_func import *

#SEARCING DATA
## where are we loking for 
tensor_cactus      = loadImageAsTensor( "images/cacti/mid-3.jpg" )
tensor_t_rex       = loadImageAsTensor( "images/t-rex/t-rex-top-1.jpg" )
tensor_distance    = loadImageAsTensor( "images/distance/none-N.jpg" )
tensor_go          = loadImageAsTensor( "images/GO/go_none.jpg" )
### number_tensors
tensor_none       = loadImageAsTensor( "images/numbers/none.jpg" )
tensor_0          = loadImageAsTensor( "images/numbers/0.jpg" )
tensor_1          = loadImageAsTensor( "images/numbers/1.jpg" )
tensor_2          = loadImageAsTensor( "images/numbers/2.jpg" )
tensor_3          = loadImageAsTensor( "images/numbers/3.jpg" )
tensor_4          = loadImageAsTensor( "images/numbers/4.jpg" )
tensor_5          = loadImageAsTensor( "images/numbers/5.jpg" )
tensor_6          = loadImageAsTensor( "images/numbers/6.jpg" )
tensor_7          = loadImageAsTensor( "images/numbers/7.jpg" )
tensor_8          = loadImageAsTensor( "images/numbers/8.jpg" )
tensor_9          = loadImageAsTensor( "images/numbers/9.jpg" )

## what are we loking for
weights_t_rex  = loadImageAsTensor( "images/masks/t-rex-weights.jpg" )
weights_cactus = loadImageAsTensor( "images/masks/cactus-weights.jpg" )
weights_go     = loadImageAsTensor( "images/masks/go.jpg" )
### number_weights
weights_0     = loadImageAsTensor( "images/masks/numbers/0.jpg" )
weights_1     = loadImageAsTensor( "images/masks/numbers/1.jpg" )
weights_2     = loadImageAsTensor( "images/masks/numbers/2.jpg" )
weights_3     = loadImageAsTensor( "images/masks/numbers/3.jpg" )
weights_4     = loadImageAsTensor( "images/masks/numbers/4.jpg" )
weights_5     = loadImageAsTensor( "images/masks/numbers/5.jpg" )
weights_6     = loadImageAsTensor( "images/masks/numbers/6.jpg" )
weights_7     = loadImageAsTensor( "images/masks/numbers/7.jpg" )
weights_8     = loadImageAsTensor( "images/masks/numbers/8.jpg" )
weights_9     = loadImageAsTensor( "images/masks/numbers/9.jpg" )
