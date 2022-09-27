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
frame_png = base64.b64decode( frame_base64 )

'''
# Convert to PIL Image
frame = io.BytesIO( frame_png )
frame = Image.open( frame )

# Transform to torch tensor
toTensor = transforms.ToTensor()
frameTensor = toTensor( frame )

print( frameTensor.shape )
'''
print( tensor_frame )

