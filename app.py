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
'''
v_br, v_dr = getChromeVersion()
print( f"Browser version >>> {v_br}, \nDriver version  >>> {v_dr}" )

'''
system( "clear" )


browser, canvas = connectToClient() 
frame = getCanvasTensor( browser, canvas )
