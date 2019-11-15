#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import html5lib
except ImportError as error:
    print('Please install '+error.name)
    print('For example: pip install '+error.name)

import sitepage

class SitePageHtml5(sitepage.SitePage):

    def __init__(self,url):
        super().__init__(url)
        self.soap = html5lib.parse(self.html)
