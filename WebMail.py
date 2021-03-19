#By JG
#A Series of Scripts To Help Automate The Assistance of Associates @ JCREW 
#Based On ServiceAides Ticket System and Built on Pythons flavor of Selenium
#OBOR this down the road. Many of these blocks can be made into funtions  

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def WM_Browser_Setup(WM_Website):
    WM_browser = webdriver.Chrome()
    WM_browser.implicitly_wait(10)
    WM_browser.get(WM_Website) 
    return WM_browser

def WM_Browser_Quit_Function(browser):
    browser.quit()

def WM_Refresh_Function(browser):
        browser.refresh()
        time.sleep(2)    
