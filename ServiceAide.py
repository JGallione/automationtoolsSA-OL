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

def SA_Browser_Setup(SA_Website):
    SA_browser = webdriver.Chrome()
    SA_browser.implicitly_wait(10)
    SA_browser.get(SA_Website)
    return SA_browser

def SA_Login_Function(browser, UserName_Input, PassWord_Input):    
    USERNAME = browser.find_element(By.ID, "textfield-1016-inputEl")
    USERNAME.send_keys(UserName_Input + Keys.TAB)
    time.sleep(1)

    PASSWORD = browser.find_element(By.ID, "textfield-1017-inputEl")
    PASSWORD.send_keys(PassWord_Input)
    time.sleep(1)
    
    Login_Click = ActionChains(browser)
    LOGIN_BUTTON = browser.find_element(By.ID, "button-1021-btnEl")
    Login_Click.move_to_element(LOGIN_BUTTON).perform()
    LOGIN_BUTTON.click()
    time.sleep(2)

def SA_Logout_Function(browser):
    #Click Profile Button in upper right hand corner
    Profile_Click = ActionChains(browser)
    PROFILE_BUTTON = browser.find_element(By.ID, "headerprofileicon-btnIconEl")
    Profile_Click.move_to_element(PROFILE_BUTTON).perform()
    PROFILE_BUTTON.click()
    time.sleep(2)

    #Click Logout Button from drop down menu from Profile Button
    Logout_Click = ActionChains(browser)
    LOGOUT_BUTTON = browser.find_element(By.ID, "menuitem-1036-textEl")
    Logout_Click.move_to_element(LOGOUT_BUTTON).perform()
    LOGOUT_BUTTON.click()
    time.sleep(2)

def SA_Download_CSV_Function(browser):
    CSV_Click = ActionChains(browser)
    Download_CSV = browser.find_element(By.ID, "tabButton-1115-btnInnerEl")
    CSV_Click.move_to_element(Download_CSV).perform()
    Download_CSV.click()
    time.sleep(2)

def SA_Refresh_Funtion(browser):
    browser.refresh()
    time.sleep(2)

def SA_Browser_Quit_Function(browser):
    browser.quit()

def SA_Change_View_thin(browser):
    Change_View_Click = ActionChains(browser)
    Chnage_View_Button = browser.find_element(By.ID, "toggleButton-1122-btnIconEl")
    Change_View_Click.move_to_element(Chnage_View_Button).perform()
    Chnage_View_Button.click()
    time.sleep(2)

def SA_Open_Top_Ticket(browser):
    Dropdown_click = ActionChains(browser)
    Dropdown_BUTTON = browser.find_element_by_xpath("//button[starts-with(@id, 'tab-1')]")
    Dropdown_click.move_to_element(Dropdown_BUTTON).perform()
    Dropdown_BUTTON.click()
    Dropdown_BUTTON.send_keys(Keys.TAB * 53)

