import requests
import re

class SitePage():

    def __init__(self, url):
        self.url = url
        self.response = self.response()
        if self.response.status_code == 200:
            self.html = self.response.text
            self.emails = self.emails(self.html)
            self.links = self.links(self.html)
            self.forms = self.forms(self.html)

    def response(self):
        return requests.request('GET', self.url)

    @staticmethod
    def emails(text):
        pattern = r'[A-Za-z0-9+%.-]+@[A-Za-z0-9.-]+\.[A-Za-z]+'
        return set(re.findall(pattern, text))

    @staticmethod
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
        return urls-bad_result

    @staticmethod
    def forms(text):
        form_attr = ('name', 'method', 'action')
        forms = dict()
        pattern = r'<form\s(.+?)>.*?</form>'
        for form_id, form in enumerate(re.findall(pattern, text, re.DOTALL)):
            forms[form_id] = dict()
            for attr in form_attr:
                match = re.search(attr + r'=["\'](.*?)["\']', form)
                if match:
                    forms[form_id][attr] = match.group(1)
        pattern = r'<form\s.+?>(.*?)</form>'
        for form_id, form in enumerate(re.findall(pattern, text, re.DOTALL)):
            forms[form_id]['content'] = form
        return forms


def hr():
    print('*'*100)

url = 'http://evil.bigazzzz.ru:15073/test.html'
test_page = SitePage(url)

hr()
print(test_page.emails)
