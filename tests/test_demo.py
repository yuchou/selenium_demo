#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from comm import html
from pages.home import homepage


class Test_Demo(unittest.TestCase):

    def setUp(self):
        self.home_page = homepage.HomePage("chrome")

    def tearDown(self):
        self.home_page.quit()

    def test_demo(self):
        u"""测试百度搜索demo"""
        self.home_page.input_search('demo')
        self.home_page.waitElement()
        self.home_page.click_search()
        self.home_page.waitTime()
        self.assertIn('wd=demo', self.home_page.getCurrentUrl())