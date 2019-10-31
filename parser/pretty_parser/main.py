#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
pip install bs4
'''
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import re

url = 'http://evil.bigazzzz.ru:15073/test.html' #url = input('url=>')
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features="html.parser")
#print(soup.prettify())
for link in soup.find_all('a'):
    print(link.contents[0] + ' => ' + link.get('href'))

emails = set(re.findall(r'[A-z0-9\.\-+_]+@[A-z0-9\.\-+_]+\.[A-z]+', html_doc))
print(emails)

