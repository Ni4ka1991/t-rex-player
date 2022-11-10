# client.py module

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
    #print( frame_tensor )
    #print( frame_tensor.shape )

    #viewImg( frame_tensor )
    zone_A = frame_tensor[0][:,0:48]
    #print( zone_A )
    #print( zone_A.shape )
    zone_A = zone_A.unsqueeze(0)
    viewImg( zone_A )

