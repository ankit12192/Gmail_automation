"""
This Script can be used to send email  by just using python command line
prerequisite : The following libraries should be installed
1. urllib
2. getpass
3. selenium
4. requests
step to run
python facebooklogin.py
"""

#---------------------------
#	Importing Modules
#---------------------------

__author__ = 'Ankit'
import  requests
import requests.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests.exceptions import ConnectionError
import getpass
import time

#Will be converting into modules
browser = webdriver.Firefox()
browser.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")

inputElement = browser.find_element_by_name('Email')
#phone =raw_input("Enter email - > ")
inputElement.send_keys('ank9222')
inputElement.send_keys(Keys.ENTER)
time.sleep(1)
inputElement3 = browser.find_element_by_name('Passwd')
inputElement3.send_keys('qwer12192')
inputElement3.send_keys(Keys.ENTER)
time.sleep(5)
inputElement4=browser.find_element_by_xpath('//*[@id=":jb"]/div').click()

inputElement5=browser.find_element_by_tag_name("textarea").send_keys("ank9222@gmail.com",Keys.ENTER)
inputElement6=browser.find_element_by_class_name('aoT').send_keys("Testing Automation2",Keys.COMMAND+Keys.ENTER)
#inputElement7=browser.find_element_by_name("Message ").send_keys("j")#\3a q5

"""
start_time = time.time()
browser.find_element_by_tag_name('textarea').is_displayed()
print("Logged in !")
print("total --- %s seconds --- taken to login " % (int(time.time() - start_time)*100))

"""


#//*[@id=":jk"]/div/div

