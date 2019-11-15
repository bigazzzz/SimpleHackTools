import requests
import re

def emails(text):
    pattern = r'[A-Za-z0-9+%-.]+@[A-Za-z0-9-.]+\.[A-Za-z]+'
    return set(re.findall(pattern, text))

def links(text):
    bad_result = set()
    pattern = r'href="(.+)"'
    bad_urls = [
        'mailto:(.+)',
        'tel:(.+)',
        'javascript:(.*)',
        '#(.*)'
    ]
    urls = set(re.findall(pattern, text))
    for url in urls:
        for bad_url in bad_urls:
            if re.fullmatch(bad_url, url) != None:
                bad_result.add(url)
    return urls - bad_result

def forms(text):
    pattern = r'<form\s(.+?)>(.*?)</form>'
    return re.findall(pattern,text,re.DOTALL)


def hr():
    print('*'*100)

url = 'http://evil.bigazzzz.ru:15073/test.html'
html_response = requests.request('GET', url)
''' в html_response.text - текст html-документа'''
hr()
print(emails(html_response.text))
hr()
print(links(html_response.text))
hr()
print(forms(html_response.text))
