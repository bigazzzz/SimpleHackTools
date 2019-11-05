import requests
import re

def emails(text):
    pattern = '[A-Za-z0-9+%-.]+@[A-Za-z0-9-.]+\.[A-Za-z]+'
    return set(re.findall(pattern, text))

url = 'http://evil.bigazzzz.ru:15073/test.html'
html_response = requests.request('GET', url)
''' в html_response.text - текст html-документа'''
print(emails(html_response.text))
