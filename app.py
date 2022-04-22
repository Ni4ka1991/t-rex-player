#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision.io import read_image
from PIL import Image, ImageOps

#PLOT
import matplotlib.pyplot as plt


#LOAD IMAGE AS TENSOR
tensor = invert( rgb_to_grayscale(
        read_image( "images/t-rex-up-1.jpg" )
)).type(torch.float32)

print( tensor )
print( tensor.shape )
tensor2 = tensor.unsqueeze_(0)


#plt.imshow( tensor.permute( 1, 2, 0 ), cmap='gray' )
#plt.show()


cnn = nn.Conv2d( 1, 1, 40 )

filtered_img = cnn( tensor2 )

plt.figure()

plt.imshow( filtered_img.detach().permute( 1, 2, 0 ), interpolation='nearest', cmap = 'gray' )
plt.show()





#model = nn.Sequential(
#        nn.Conv2d( 1, 1, 40 ),
#)

#y = model( tensor )
#plt.imshow( y.detach().permute( 1, 2, 0 ), cmap='gray' )
#plt.show()
