# browser_check.py module

import logging
from selenium import webdriver

logger = logging.Logger('catch_all')

def getChromeVersion():
    global browser_version_number
    try:
        browser_version_driver = webdriver.Chrome("drivers/chromedriver.exe")
        browser_version_number = (browser_version_driver.capabilities['browserVersion'])
        browser_version_number = browser_version_number.split(".")[0]

        chromedriverversion = browser_version_driver.capabilities['chrome']['chromedriverVersion'].split('.')[0]
                                                        
        print( f"Browser Version Number >>> {browser_version_number}" )
        print( f"Chrome Driver Version >>>  {chromedriverversion}" )
                                                                                
        if browser_version_number != chromedriverversion:
            updateChromeVersion()
                                                                                                                
            browser_version_driver.quit()

###############---------------REALLY IMPORTANT PART BELOW---------------###############
    except Exception as e:
        e = str(e) # Saves exception to a variable. Most importantly, converts to string to allow me to manipulate it.
        print( f"Be attention!!! >>> {e}" )
        linesplit = e.split('This version of ChromeDriver only supports Chrome version ')[1]
        checking_driverversion = linesplit.split('\n')[0]
        print( f"Chrome Driver Version >>>  {checking_driverversion}" ) # prints '105' which is my chromedriver right now
                                
        checking_browserversion = linesplit.split('\n')[1]
        checking_browserversion = checking_browserversion.split('Current browser version is ')[1]
        checking_browserversion = checking_browserversion.split('.')[0]
        print( f"Browser Version Number >>> {checking_browserversion}" ) # prints '107' which is my browser version right now
        browser_version_number = checking_browserversion

        if checking_browserversion != checking_driverversion:
            updateChromeVersion()



def updateChromeVersion():
    pass


