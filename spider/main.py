#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sitepagehtml5 import SitePageHtml5

def hr():
    print('*'*100)

test_page = SitePageHtml5('http://evil.bigazzzz.ru:15073/test.html')

hr()
print(test_page.soup)
