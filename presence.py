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

br.open("https://www.leonard-de-vinci.net/student/presences/")

print(br.geturl())