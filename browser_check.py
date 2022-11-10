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
    '''
    LINK = 'https://chromedriver.chromium.org/downloads'
    try:
        html = r.get(LINK)
    except r.ConnectionError as e:
        print("Error in connecting")
    except r.Timeout as e:
        print("Timeout")
    except r.RequestException as e:
        print("Invalid URL")
    except (KeyboardInterrupt, SystemExit):
        print("System has quit")
        sys.exit(1)
    '''
    pass
