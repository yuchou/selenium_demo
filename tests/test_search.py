#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pages.home import homepage
from pages import config


class Test_Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = config.baseUrl
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        self.driver.get(self.base_url)
        home_page = homepage.HomePage(self.driver)
        home_page.input_search('test')
        home_page.click_search()
        self.driver.implicitly_wait(10)
        self.assertIn('wd=test', self.driver.current_url)



if __name__ == '__main__':
    unittest.main(verbosity=2)
