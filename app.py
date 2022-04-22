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

img = read_image( "images/t-rex-up-1.jpg" )  #read image as tensor???
print( img )
print( img.shape )

img_gray = rgb_to_grayscale( img )
print( img_gray )
print( img_gray.shape )

img_invert = invert(img_gray)
print( img_invert )
print( img_invert.shape )


cnn = nn.Conv2d( 1, 1, 7 )
img_filtered = cnn( img_invert )
print( img_filtered )
print( img_filtered.shape )





'''
plt.imshow( img, interpolation = 'nearest', cmap='gray' )
plt.show()
img_gray = rgb_to_grayscale(img)
#plt.imshow( tensor.permute( 1, 2, 0 ), cmap='gray' )
#plt.show()


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
'''
