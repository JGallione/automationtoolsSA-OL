import os
import time

import ServiceAide
from ServiceAide import SA_Login_Function, SA_Logout_Function,\
SA_Download_CSV_Function, SA_Refresh_Funtion, SA_Browser_Quit_Function,\
SA_Change_View_thin, SA_Open_Top_Ticket, SA_Browser_Setup

import send_protocol
from send_protocol import send_msg

import WebMail
from WebMail import WM_Browser_Setup, WM_Browser_Quit_Function, WM_Refresh_Function

WM_Website = "https://smtp-mail.outlook.com"
SA_Website = "https://csm3.serviceaide.com/#login"
username = "joseph.gallione2@jcrew.com"
sender_user = "joseph.gallione@jcrew.com"   
password = "JCrew123!"
sender_pass = "Jcrew433866"


SA_browser = SA_Browser_Setup(SA_Website)
#WM_browser = WM_Browser_Setup(WM_Website)

SA_Login_Function(SA_browser, username, password)
SA_Download_CSV_Function(SA_browser)
SA_Refresh_Funtion(SA_browser)
#WM_Refresh_Function(WM_browser)
time.sleep(2)
SA_Change_View_thin(SA_browser)
SA_Open_Top_Ticket(SA_browser)
time.sleep(2)
SA_Logout_Function(SA_browser)
time.sleep(2)
SA_Browser_Quit_Function(SA_browser)
#WM_Browser_Quit_Function(WM_browser)

send_msg(sender_user, sender_pass, '9292817112@vtext.com', 'Test Complete Confirmation', 'hey, looks like attachments have been removed')