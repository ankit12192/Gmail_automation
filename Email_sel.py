"""
This Script can be used for performing various action on gmail
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from requests.exceptions import ConnectionError
import getpass
import time
import random
import matplotlib.pyplot as plt
Time_list=[]
browser = webdriver.Firefox()
browser.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier")
x='No messages matched your search'

def login_gmail(email,password):

  start_time = time.time()
  browser.find_element_by_name('Email').send_keys(email+Keys.ENTER)
  time.sleep(2)
  browser.find_element_by_name('Passwd').send_keys(password+Keys.ENTER)
  total_time=time.time()-start_time
  print("--- %s seconds ---" % (time.time() - start_time))
  Time_list.append(total_time)

def send_mail(n,to,ch):
    start_time = time.time()
    for i in xrange(int(n)):
        browser.find_element_by_xpath("//*[@gh='cm']").click()
        time.sleep(2)
        browser.find_element_by_tag_name("textarea").send_keys(to,Keys.ENTER)
        if ch =='NT':
            browser.find_element_by_class_name('aoT').send_keys("Testing Automation "+str(random.randint(1, 1000000)))#NON THERADED
        elif ch=="TH":
            browser.find_element_by_class_name('aoT').send_keys("Testing Automation ") #THREADED
        browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys("This is message number "
        +str(random.randint(1,999922922)),Keys.COMMAND+Keys.ENTER)
    total_time=time.time()-start_time
    Time_list.append(total_time)

def open_compose():
    start_time = time.time()
    browser.find_element_by_xpath("//*[@class='T-I J-J5-Ji T-I-KE L3']").click()
	#browser.find_element_by_xpath('//*[@class=":aic"]/div').click()

def Adv_search_email(to,subject):
    start_time = time.time()
    browser.find_element_by_xpath('//div[@aria-label="Advanced search options"]').click()
    time.sleep(3)
    #browser.find_element_by_class_name('ZH nr aQf').send_keys("HEYY")
    browser.find_element_by_xpath("//*[@class='ZH nr aQa']").send_keys(to,Keys.TAB)
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class='ZH nr aQd']").send_keys(subject)
    browser.find_element_by_xpath("//*[@data-tooltip='Search Mail']").click()
    time.sleep(2)
    a= browser.find_element_by_xpath("//*[@class='ae4 UI']").text
    if x in a:
        print "NO messege"
    else:
        print "There are messages "
    total_time=time.time()-start_time
    Time_list.append(total_time)

def Basic_search(key):
    start_time = time.time()
    browser.find_element_by_xpath("//*[@aria-owns='gs_sbt50']").send_keys(key,Keys.ENTER)
    a= browser.find_element_by_xpath("//*[@class='ae4 UI']").text
    print a
    if x in a:
        print "NO mail found"
    else:
        print "Mails found"
    total_time=time.time()-start_time
    Time_list.append(total_time)

def Select_all():
	start_time = time.time()
	browser.find_element_by_css_selector('//div[@aria-label="Select"]').click()

def tap_setting():
	browser.find_element_by_xpath("//*[@class='aos T-I-J3 J-J5-Ji']").click()

def change_signature (signature):
    start_time = time.time()
    #browser.find_element_by_css_selector('.ash.T-I').click()
    browser.get("https://mail.google.com/mail/u/0/#settings/general")
    time.sleep(3)
    print browser.find_element_by_xpath("//div[@aria-label='Signature']").text
    browser.find_element_by_xpath("//div[@aria-label='Signature']").clear()
    browser.find_element_by_xpath("//div[@aria-label='Signature']").send_keys(signature)
    browser.find_element_by_xpath(".//*[@guidedhelpid='save_changes_button']").click()
    total_time=time.time()-start_time
    Time_list.append(total_time)

def selecting_random_email(num):
    start_time = time.time()
    for i in xrange(int(num)):
        time.sleep(3)
        m = random.randint(1, 10)
        print("Mail Number " + str(m) + " is selected")
        browser.find_element_by_xpath("//div[@role='tabpanel'][1]//table//tr" + str([m])).click()
        time.sleep(2)
        browser.find_element_by_xpath("//*[@class='ar6 T-I-J3 J-J5-Ji']").click()
        total_time = time.time() - start_time
        Time_list.append(total_time)


def Plot_graph():
	Data = {u'Login Module ':Time_list[0], u'Send':Time_list[1],
            u'Select email':Time_list[2],
            u'Signature ':Time_list[3],u' language':Time_list[4],u'filter':Time_list[5],
            u'label':Time_list[6],u'main module':Time_list[7],u'Star email':Time_list[8],u'remove star':Time_list[9]
            ,u'star':Time_list[10],u'Search':Time_list[11],u'Advance search':Time_list[12]}

	plt.bar(range(len(Data)), Data.values(), align='center')
	plt.xticks(range(len(Data)), Data.keys())
	plt.xlabel("Modules")
	plt.ylabel("Time in seconds")
	plt.show()

def create_filter(to,subject):
    start_time = time.time()
    browser.get("https://mail.google.com/mail/u/0/#settings/general")
    time.sleep(3)
    browser.find_element_by_link_text("Filters and Blocked Addresses").click()
    time.sleep(3)
    browser.find_element_by_xpath('//div[@aria-label="Advanced search options"]').click()
    time.sleep(3)
    #browser.find_element_by_class_name('ZH nr aQf').send_keys("HEYY")
    browser.find_element_by_xpath("//*[@class='ZH nr aQa']").send_keys(to,Keys.TAB)
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class='ZH nr aQd']").send_keys(subject)
    time.sleep(2)
    browser.find_element_by_class_name("acM").click()
    time.sleep(2)
    browser.find_element_by_class_name("aD").click()
    #browser.find_element_by_xpath(".//*[@id=':gi']").send_keys(Keys.ENTER,"Work")
   # time.sleep(2)
    browser.find_element_by_xpath("//*[@class='T-I J-J5-Ji Zx acL T-I-atl L3']").click()
    total_time=time.time()-start_time
    Time_list.append(total_time)

def create_label():
    start_time = time.time()
    browser.get("https://mail.google.com/mail/u/0/#settings/general")
    time.sleep(2)
    browser.find_element_by_link_text("Labels").click()
    browser.find_element_by_class_name("alZ").click()
    browser.find_element_by_class_name("xx").send_keys("Lable"+str(random.randint(1,100000)),Keys.COMMAND+Keys.ENTER)
    browser.find_element_by_name("ok").click()
    browser.find_element_by_link_text("Inbox").click()
    total_time=time.time()-start_time
    Time_list.append(total_time)

def lang():
    start_time = time.time()
    browser.get("https://mail.google.com/mail/u/0/#settings/general")
    time.sleep(2)
    a=browser.find_element_by_xpath("//*[@class='a5p']")
    a.send_keys("English (UK)",Keys.ENTER)
    browser.find_element_by_xpath(".//*[@guidedhelpid='save_changes_button']").click()
    total_time=time.time()-start_time
    Time_list.append(total_time)

def star_email(n):

    start_time = time.time()
    for i in xrange(n):
        a=browser.find_element_by_xpath("//div[@role='tabpanel'][1]//table//tr" + str([i+1]))
        a.send_keys("")
        browser.find_element_by_xpath("//*[@aria-label='Not starred']").click()
        time.sleep(2)
    total_time=time.time()-start_time
    Time_list.append(total_time)

def remove_star(n):
    start_time = time.time()
    for i in xrange(n):
        a=browser.find_element_by_xpath("//div[@role='tabpanel'][1]//table//tr" + str([i+1]))
        a.send_keys("h")
        browser.find_element_by_xpath("//*[@aria-label='Starred']").click()
        time.sleep(2)
    total_time=time.time()-start_time
    Time_list.append(total_time)

def check_star():
    start_time = time.time()
    browser.find_element_by_link_text("Starred").click()
    time.sleep(1)
    a=  browser.find_element_by_xpath("//*[@class='ae4 UI']").text
    if 'No starred messages.' in a:
        print "NO messages "
    else:
        print "There are messages"
    total_time=time.time()-start_time
    Time_list.append(total_time)

def del_particular_email(m):
    start_time = time.time()
    browser.find_element_by_xpath("//div[@role='tabpanel'][1]//table//tr" + str([m])).click()
    time.sleep(4)
    #s=browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[3]')
    s=browser.find_element_by_xpath('//div[@class="ar9 T-I-J3 J-J5-Ji"]')
    s.click()
    """time.sleep(1)
    s.send_keys("Reply")
    time.sleep(1)
    s.click()"""
    total_time = time.time() - start_time
    Time_list.append(total_time)


def main():
    start_time = time.time()
    time.sleep(2)
    login_gmail("ID","Password")
    time.sleep(6)
    send_mail(1,"ank9222@gmail.com")
    time.sleep(2)
    selecting_random_email(1)
    time.sleep(3)
    star_email(3)
    time.sleep(3)
    remove_star(2)
    time.sleep(3)
    check_star()
    time.sleep(3)
    change_signature("Ankit Tiwari")
    time.sleep(3)
    lang()
    time.sleep(3)
    create_filter("abc@gmail.com","HII")
    time.sleep(3)
    create_label()
    time.sleep(3)
    Basic_search("1234")
    time.sleep(3)
    Adv_search_email("ank","ank")
    total_time=time.time()-start_time
    Time_list.append(total_time)


main()