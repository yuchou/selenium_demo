#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from comm import html
from pages.home import homepage


class Test_Search(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.home_page = homepage.HomePage("chrome")

    @classmethod
    def tearDownClass(self):
        self.home_page.quit()

    def test_search(self):
        u"""测试百度搜索test"""
        self.home_page.input_search('test')
        self.home_page.waitElement()
        self.home_page.click_search()
        self.home_page.waitTime()
        self.assertIn('wd=test', self.home_page.getCurrentUrl())
