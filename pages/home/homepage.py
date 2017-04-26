#!/usr/bin/env python
# -*- coding: utf-8 -*-
from comm import basepage, config


class HomePage(basepage.BasePage):

    kw = ('ID', 'kw')
    su = ('ID', 'su')

    def __init__(self, browser='chrome'):
        super().__init__(browser)
        self.open(config.baseUrl)
        self.waitElement()
        self.maximizeWindow()

    def input_search(self, kw):
        keyword = self.findElement(*HomePage.kw)
        self.type(keyword, kw)

    def click_search(self):
        search = self.findElement(*HomePage.su)
        self.click(search)
