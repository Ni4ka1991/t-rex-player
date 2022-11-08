#!/usr/bin/env python3

#TORCH
import torch
from torch import nn
from torchvision import transforms
from torch.nn.functional import normalize
from torchvision.transforms.functional import invert, to_tensor


#PROJECT MODULES
from data import *
from client import *
from browser_check import *

#OTHER
import struct
import base64
import numpy as np
from os import system
from matplotlib import pyplot as plt
from matplotlib.image import imread
from PIL import Image, ImageOps 
import io

getChromeVersion()


'''
system( "clear" )


browser, canvas = connectToClient() 

#get the image from the canvas
frame_base64 = browser.execute_script( "return arguments[0].toDataURL('image/png').substring(22)", canvas )
frame_binary = base64.b64decode( frame_base64 ) # decode base64 into bytes
frame_buffer = io.BytesIO( frame_binary )
frame_png    = Image.open( frame_buffer )       # get PIL image in RGBA (4 channel)
frame_gray   = ImageOps.grayscale( frame_png )  # get a grayscale image with 1 channel
frame_tensor = normalize( invert( to_tensor( frame_gray).type( torch.float32 )))
#print( frame_tensor )
#print( frame_tensor.shape )

#viewImg( frame_tensor )
zone_A = frame_tensor[0][:,0:48]
#print( zone_A )
#print( zone_A.shape )
zone_A = zone_A.unsqueeze(0)
viewImg( zone_A )
'''
