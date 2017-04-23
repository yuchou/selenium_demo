#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import os
from os.path import dirname, abspath

baseUrl = 'https://www.baidu.com'

def driverPath():
    if platform.system() == 'windows':
        return os.path.join(dirname(dirname(abspath(__file__))), 'tool\chromedriver')
    else:
        return os.path.join(dirname(dirname(abspath(__file__))), 'tool/chromedriver')
