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

# You must have Firefox installed (For now I am using firefox web driver )

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
from selenium.webdriver.common.action_chains import ActionChains
#n=raw_input("How many Mail ?")

browser = webdriver.Firefox()
Ac =ActionChains(browser).key_down(Keys.COMMAND+Keys.TAB)
ActionChains.send_keys(Ac)
browser.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")

def login_gmail():
	inputElement = browser.find_element_by_name('Email')
	#phone =raw_input("Enter email - > ")
	inputElement.send_keys('atp12192')
	inputElement.send_keys(Keys.ENTER)
	time.sleep(3)
	inputElement3 = browser.find_element_by_name('Passwd')
	inputElement3.send_keys('qwer12192')
	inputElement3.send_keys(Keys.ENTER)

def send_mail():
 try:
  for i in xrange(int(4)):
   inputElement4=browser.find_element_by_xpath('//*[@id=":jb"]/div').click()
   time.sleep(3)
   inputElement5=browser.find_element_by_tag_name("textarea").send_keys("anktest12192@outlook.com",Keys.ENTER)
   #inputElement6=browser.find_element_by_class_name('aoT').send_keys("Testing Automation "+str(random.randint(1, 1000000)))#NON THERADED
   inputElement6=browser.find_element_by_class_name('aoT').send_keys("Testing Automation ") #THREADED
   inputElement7=browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys("This is message number "+str(random.randint(1,999922922)),Keys.COMMAND+Keys.ENTER)
 finally:
  time.sleep(1)
  browser.delete_all_cookies()
  browser.close()

"""
9721457945
rameshtrph@gmail.com
"""

login_gmail()
time.sleep(10)
#//*[@id="yui_3_12_0_1_1459855716082_1505"]




#//*[@id=":uw"]
#//*[@id=":vg"]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/div/span

def open_compose():
	inputElement4=browser.find_element_by_xpath('//*[@id=":jb"]/div').click()

#open_compose()

def star_email():
	inputElement4=browser.find_element_by_xpath('//div[@aria-label="Advanced search options"]').click()



def Adv_search_email():
	inputElement4=browser.find_element_by_xpath('//div[@aria-label="Advanced search options"]').click()



def Basic_search():
	inputElement4=browser.find_element_by_id('gbqfq').send_keys("spt12192@gmail.com",Keys.ENTER)
	time.sleep(4)
	browser.find_element_by_xpath('//div[@aria-label="pp"])').click()


#Basic_search()


def Select_all():
	inputElement4=browser.find_element_by_xpath('//div[@aria-label="Select"]').click()

#Select_all()
#Basic_search()


send_mail()
