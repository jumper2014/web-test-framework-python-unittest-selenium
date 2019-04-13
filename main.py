#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from libs.pages.search_page import *

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    SearchPage(driver).search("selenium")