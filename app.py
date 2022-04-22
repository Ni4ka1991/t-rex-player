#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision.transforms.functional import rgb_to_grayscale, invert, normalize
from torchvision import transforms
from torchvision.io import read_image
from PIL import Image, ImageOps

#PLOT
import matplotlib.pyplot as plt


#LOAD IMAGE AS TENSOR
img = Image.open( 'images/t-rex-up-1.jpg' )
print( 'This is an original size of image >>>', img.size, '\n' )
img_gray = ImageOps.grayscale(img)

img_invert = invert(img_gray)

#plt.figure()
#plt.imshow( img_invert, interpolation='nearest', cmap = 'gray' )
#plt.show()

img_tensor = transforms.ToTensor()(img_invert).unsqueeze_(0)
print( img_tensor )
print( img_tensor.shape )



'''
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
