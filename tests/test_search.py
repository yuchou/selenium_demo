#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium_demo.pages.home import homepage


class Test_Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        self.driver.get(self.base_url)
        home_page = homepage.HomePage(self.driver)
        home_page.input_search('test')
        home_page.click_search()


if __name__ == '__main__':
    unittest.main()