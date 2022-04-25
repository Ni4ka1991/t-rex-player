#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torch.nn.functional import normalize
from torchvision.io import read_image
from PIL import Image, ImageOps
from os import system


#PLOT
import matplotlib.pyplot as plt


#LOAD IMAGE AS TENSOR
system( "clear" )

tensor = ( normalize( invert( rgb_to_grayscale(
    read_image( "images/t-rex-up-1.jpg" ))).type(torch.float32))
).unsqueeze_(0)

model = nn.Sequential(
        nn.Conv2d( 1, 1, (40,40))
)

y = model( tensor )
print(y.shape)
img_sqz = y.squeeze(0)
plt.imshow( img_sqz.detach().permute( 1, 2, 0 ), interpolation='nearest', cmap = 'gray' )
plt.show()
'''
'''
