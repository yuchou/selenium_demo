#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium_demo.pages import basepage


class HomePage(basepage.BasePage):

    kw = (By.ID, 'kw')
    click = (By.ID, 'su')

    def input_search(self, kw):
        keyword = self.driver.find_element(*HomePage.kw)
        keyword.send_keys(kw)

    def click_search(self):
        search = self.driver.find_element(*HomePage.click)
        search.click()
