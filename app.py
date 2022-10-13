#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision import transforms


#PROJECT MODULES
from data import *

#OTHER
import struct
import base64
import numpy as np
from os import system
from selenium import webdriver
from selenium.webdriver.common.by import By
from matplotlib import pyplot as plt
from matplotlib.image import imread
from PIL import Image, ImageOps 
import io

system( "clear" )

##Connect to browser

browser = webdriver.Chrome( './drivers/chromedriver.exe' )
browser.get('https://www.trex-game.skipser.com/')

# find canvas element by class selector
canvas = browser.find_element(  By.CLASS_NAME, 'runner-canvas' )

#get the image from the canvas
frame_base64 = browser.execute_script( "return arguments[0].toDataURL('image/png').substring(22)", canvas )
frame_binary = base64.b64decode( frame_base64 ) # decode base64 into bytes
frame_buffer = io.BytesIO( frame_binary )
frame_png    = Image.open( frame_buffer )       # get PIL image
'''
print("#"*20 )
print(frame_png.format)
print(frame_png.size)
print(frame_png.mode)
print("#"*20 )
'''
np_img = np.array( frame_png )


'''
print( f"shape of np_array =>>> {np_img.shape}" )
print( f"dimention of np_array =>>> {np_img.ndim}" )
'''
from copy import deepcopy
image = deepcopy( np_img )
#image[ :, :, 1 ] = 255      #the visible layer come to be green
#image[ :, :, 0 ] = 255      #the visible layer come to be red
#image[ :, :, 2 ] = 255      #the visible layer come to be blue
#image[ :, :, 3 ] = 255       #alpha layer come to be black

plt.imshow( image )
#plt.title( ' image ' )
plt.show()
'''
toTensor = transforms.ToTensor()
frame_tensor = toTensor( ImageOps.grayscale( frame_png ))
print( frame_tensor.shape )


#pil_img =  invert(Image.open( 'images/frames/frame.jpg' ))
#plt.imshow( image_without_alpha )
#img = imread( file_name)
plt.imshow( frame_png )
#plt.title( ' PIL image invert' )
plt.show()
#tensor = normalize( rgb_to_grayscale( pil_img ))

#tensor = ( normalize( invert( pil_img ))).type(torch.float32).unsqueeze_(0)
#tensor = normalize( invert( pil_img ))

#print( tensor )
'''
