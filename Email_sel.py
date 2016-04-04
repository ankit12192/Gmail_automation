"""
This Script can be used to send email  by just using python command line
prerequisite : The following libraries should be installed
1. urllib
2. getpass
3. selenium
4. requests
step to run
python Email_sel.py
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
import random

#Will be converting into modules
browser = webdriver.Firefox()
browser.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")

inputElement = browser.find_element_by_name('Email')
#phone =raw_input("Enter email - > ")
inputElement.send_keys('ank9222')
inputElement.send_keys(Keys.ENTER)
time.sleep(3)
inputElement3 = browser.find_element_by_name('Passwd')
inputElement3.send_keys('qwer12192')
inputElement3.send_keys(Keys.ENTER)
time.sleep(2)
for i in range(1,3):
    inputElement4=browser.find_element_by_xpath('//*[@id=":jb"]/div').click()
    time.sleep(2)
    inputElement5=browser.find_element_by_tag_name("textarea").send_keys("ankit.tiwari12192@gmail.com",Keys.ENTER)
    inputElement6=browser.find_element_by_class_name('aoT').send_keys("Testing Automation "+str(random.randint(1, 1000000)))
    inputElement7=browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys("This is message number "+str(random.randint(1,999922922)),Keys.COMMAND+Keys.ENTER)
