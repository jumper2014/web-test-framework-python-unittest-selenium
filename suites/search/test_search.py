#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import unittest
from libs.pages.search_page import *


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearchOk(self):
        self.driver.get("https://www.baidu.com")
        SearchPage(self.driver).search("selenium")

    def tearDown(self):
        self.driver.close()




