import urllib.robotparser as urobot
import urllib.request
from bs4 import BeautifulSoup


import re
import mechanize
from mechanize import Browser


import os
result = os.popen("curl https://www.leonard-de-vinci.net/robots.txt").read()
result_data_set = {"Disallowed":[], "Allowed":[]}

for line in result.split("\n"):
    if line.startswith('Allow'):    # this is for allowed url
        result_data_set["Allowed"].append(line.split(': ')[1].split(' ')[0])    # to neglect the comments or other junk info
    elif line.startswith('Disallow'):    # this is for disallowed url
        result_data_set["Disallowed"].append(line.split(': ')[1].split(' ')[0])    # to neglect the comments or other junk info

print (result_data_set)


>>> urllib.robotparser.RobotFileParser()
>>> urllib.robotparser.RobotFileParser().set_url("https://www.leonard-de-vinci.net/robots.txt")
>>> urllib.robotparser.RobotFileParser().read()
>>> rrate = urllib.robotparser.RobotFileParser().request_rate("*")
>>> rrate.requests

>>> rrate.seconds

>>> urllib.robotparser.RobotFileParser().crawl_delay("*")

>>> urllib.robotparser.RobotFileParser().can_fetch("*", "https://www.leonard-de-vinci.net/student/presences/")


"""br = mechanize.Browser()
br.open("https://www.leonard-de-vinci.net/")

print(br.title())
soup = BeautifulSoup(html_doc, 'html.parser') """