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

