#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sitepage import SitePage

def hr():
    print('*'*100)

test_page = SitePage('http://evil.bigazzzz.ru:15073/test.html')

hr()
print(test_page.emails)
hr()
print(test_page.links)
hr()
print(test_page.forms)
