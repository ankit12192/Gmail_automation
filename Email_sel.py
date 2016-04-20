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
import matplotlib.pyplot as plt
#n=raw_input("How many Mail ?")

Time_list=[]

browser = webdriver.Firefox()
Ac =ActionChains(browser).key_down(Keys.COMMAND+Keys.TAB)
ActionChains.send_keys(Ac)
asa = browser.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")

def login_gmail():
	start_time = time.time()
	inputElement = browser.find_element_by_name('Email')
	#phone =raw_input("Enter email - > ")
	inputElement.send_keys('ank9222')
	inputElement.send_keys(Keys.ENTER)
	time.sleep(2)
	inputElement3 = browser.find_element_by_name('Passwd')
	inputElement3.send_keys('qwer12192')
	inputElement3.send_keys(Keys.ENTER)
	time.sleep(2)
	if browser.find_element_by_xpath("//*[@class='aos T-I-J3 J-J5-Ji']").is_displayed()==True:
		s0=time.time()-start_time
		print("--- %s seconds ---" % (time.time() - start_time))
		print s0
		Time_list.append(s0)

def send_mail():
 start_time = time.time()
 try:
  for i in xrange(int(1)):
   inputElement4=browser.find_element_by_xpath('//*[@id=":jb"]/div').click()
   time.sleep(3)
   inputElement5=browser.find_element_by_tag_name("textarea").send_keys("anktest12192@outlook.com",Keys.ENTER)
   #inputElement6=browser.find_element_by_class_name('aoT').send_keys("Testing Automation "+str(random.randint(1, 1000000)))#NON THERADED
   inputElement6=browser.find_element_by_class_name('aoT').send_keys("Testing Automation ") #THREADED
   inputElement7=browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys("This is message number "+str(random.randint(1,999922922)),Keys.COMMAND+Keys.ENTER)
   #print browser.find_element_by_xpath("//div[@aria-label='Message Body']").text
   #,Keys.COMMAND+Keys.ENTER)
   s0=time.time()-start_time
   Time_list.append(s0)
 finally:
  time.sleep(1)
  browser.delete_all_cookies()
  browser.close()

login_gmail()

def open_compose():
	inputElement4=browser.find_element_by_xpath('//*[@id=":jb"]/div').click()

def star_email():
	inputElement4=browser.find_element_by_xpath('//div[@aria-label="Advanced search options"]').click()

def Adv_search_email():
	inputElement4=browser.find_element_by_xpath('//div[@aria-label="Advanced search options"]').click()

def Basic_search():
	inputElement4=browser.find_element_by_id('gbqfq').send_keys("ank9222@gmail.com",Keys.ENTER)
	time.sleep(4)
	browser.find_element_by_xpath('//div[@aria-label="pp"])').click()


def Select_all():
	inputElement4=browser.find_element_by_css_selector('//div[@aria-label="Select"]').click()

def tap_setting():
	browser.find_element_by_xpath("//*[@class='aos T-I-J3 J-J5-Ji']").click()




def change_sinnature():
	#browser.find_element_by_css_selector('.ash.T-I').click()
	asa=browser.get("https://mail.google.com/mail/u/0/#settings/general")
	time.sleep(3)
	xt=browser.find_element_by_xpath("//div[@aria-label='Signature']").send_keys("Ankit 1111")
	#print browser.find_element_by_xpath("//div[@aria-label='Signature']").text
	time.sleep(2)
	print browser.find_element_by_tag_name("button").get_attribute("guidedhelpid")

def selecting_random_email(num):

	for i in xrange(int(num)):
		time.sleep(3)
		m=random.randint(1,10)
		print("Mail Number "+str(m)+" is selected")
		browser.find_element_by_xpath("//div[@role='tabpanel'][1]//table//tr"+str([m])).click()
		time.sleep(3)


#tap_setting()

time.sleep(3)
def lang():
	a=browser.find_element_by_xpath("//*[@class='a5p']")
	#print a.get_attribute(a)
	a.send_keys("English (UK)")

send_mail()

print Time_list

def Plot_graph():

	D = {u'Login Module ':Time_list[0], u'Send Email module':Time_list[1]}
	plt.bar(range(len(D)), D.values(), align='center')
	plt.xticks(range(len(D)), D.keys())
	plt.xlabel("Modules")
	plt.ylabel("Time in seconds")
	plt.show()

Plot_graph()
