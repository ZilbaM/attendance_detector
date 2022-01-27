import urllib.robotparser as urobot
import urllib.request
from bs4 import BeautifulSoup


import re
import mechanize
from mechanize import Browser

# Ignore robots.txt.  Do not do this without thought and consideration.


br = mechanize.Browser()
br.set_handle_robots(False)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


from selenium import webdriver 
driver = webdriver.Chrome('C:/Users/lucas/OneDrive/Documents/IIM/A2/crea-tech/attendance_detector/chromedriver.exe') 
driver.get("https://www.leonard-de-vinci.net/student/presences/27627136") 
html = driver.page_source 

presence_alert = driver.find_element_by_class_name('alert')
print(presence_alert.)

"""
br.open("https://www.leonard-de-vinci.net/")
response1 = br.follow_link(nr=2)
print(response1.geturl())
print(response1.info())


print(br.title()) """