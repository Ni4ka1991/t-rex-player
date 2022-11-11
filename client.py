# client.py module

#TORCH
import torch
from torch import nn
from torchvision import transforms
from torch.nn.functional import normalize
from torchvision.transforms.functional import invert, to_tensor

#OTHER
import io
import struct
import base64
from PIL import Image, ImageOps 
from selenium import webdriver
from selenium.webdriver.common.by import By

##Connect to browser
def connectToClient():
    browser = webdriver.Chrome( './drivers/chromedriver.exe' )
    browser.get('https://www.trex-game.skipser.com/')

    # find canvas element by class selector
    canvas = browser.find_element(  By.CLASS_NAME, 'runner-canvas' )
    
    return ( browser, canvas )

def getCanvasTensor( browser, canvas ):
    #get the image from the canvas
    frame_base64 = browser.execute_script( "return arguments[0].toDataURL('image/png').substring(22)", canvas )
    frame_binary = base64.b64decode( frame_base64 ) # decode base64 into bytes
    frame_buffer = io.BytesIO( frame_binary )
    frame_png    = Image.open( frame_buffer )       # get PIL image in RGBA (4 channel)
    frame_gray   = ImageOps.grayscale( frame_png )  # get a grayscale image with 1 channel
    frame_tensor = normalize( invert( to_tensor( frame_gray).type( torch.float32 )))
    
    return frame_tensor
'''
# browser_check.py module

import logging
import requests as r
from selenium import webdriver

logger = logging.Logger('catch_all')

def getChromeVersion():
    
    global browser_version_number
    
    try:
        browser_version_driver = webdriver.Chrome("drivers/chromedriver.exe")
        browser_version_number = (browser_version_driver.capabilities['browserVersion'])
        browser_version_number = browser_version_number.split(".")[0]

        chromedriverversion = browser_version_driver.capabilities['chrome']['chromedriverVersion'].split('.')[0]
                                                        
                                                                                
        if browser_version_number != chromedriverversion:
            updateChromeVersion()
                                                                                                                
            browser_version_driver.quit()
    
        return browser_version_number, chromedriverversion

###############---------------REALLY IMPORTANT PART BELOW---------------###############
    except Exception as e:
        e = str(e) # Saves exception to a variable. Most importantly, converts to string to allow me to manipulate it.
        linesplit = e.split('This version of ChromeDriver only supports Chrome version ')[1]
        checking_driverversion = linesplit.split('\n')[0]
                                
        checking_browserversion = linesplit.split('\n')[1]
        checking_browserversion = checking_browserversion.split('Current browser version is ')[1]
        checking_browserversion = checking_browserversion.split('.')[0]
        browser_version_number = checking_browserversion

        if checking_browserversion != checking_driverversion:
            updateChromeVersion()

    return checking_browserversion, checking_driverversion

def updateChromeVersion():
    LINK = 'https://chromedriver.chromium.org/downloads'
    try:
        html = r.get(LINK)
    except r.ConnectionError as e:
        print("Error in connecting")
'''
