#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision import transforms


#PROJECT MODULES
from data import *

#OTHER
from os import system
from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
from matplotlib import pyplot as plt
from matplotlib.image import imread
from PIL import Image
import io

#system( "clear" )

##Connect to browser
browser = webdriver.Chrome( './drivers/chromedriver.exe' )

browser.get('https://www.trex-game.skipser.com/')

# find canvas element by class selector
canvas = browser.find_element(  By.CLASS_NAME, 'runner-canvas' )

#get the image from the canvas
frame_base64 = browser.execute_script( "return arguments[0].toDataURL('image/png').substring(22)", canvas )
frame_binary = base64.b64decode( frame_base64 )
file_name = 'images/frames/frame.jpg'

with open( file_name, "wb" ) as f:
    f.write( frame_binary )
  # f gets closed when exit the with statement


#image_without_alpha = file_name[:,:,:3]


#pil_img =  invert(Image.open( 'images/frames/frame.jpg' ))
#plt.imshow( image_without_alpha )
img = imread( file_name)
plt.imshow( img )
#plt.title( ' PIL image invert' )
plt.show()
#tensor = normalize( rgb_to_grayscale( pil_img ))

#tensor = ( normalize( invert( pil_img ))).type(torch.float32).unsqueeze_(0)
#tensor = normalize( invert( pil_img ))

#print( tensor )

