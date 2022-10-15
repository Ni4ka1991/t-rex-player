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
from copy import deepcopy

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
np_img = np.array( frame_png )                  # transform img to array
image = deepcopy( np_img )                      # get a copy 

rgb_img = np.delete( image, 3, 0 )              # remove alpha channel from RGBA image
plt.imshow( rgb_img )
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
