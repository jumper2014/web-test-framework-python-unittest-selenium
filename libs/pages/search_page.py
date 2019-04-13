#!/usr/bin/env python
# author: zengyuetian

from selenium.webdriver.common.by import By
from libs.pages.base_page_object import BasePage
from libs.pagefactory.pagefactory_support import callable_find_by as find_by
from selenium import webdriver


class SearchPage(BasePage):

    search_box = find_by(id_="kw")
    search_button = find_by(id_='su')

    def search(self, keywords):
        self.search_box().clear()
        self.search_box().send_keys(keywords)
        self.search_button().click()
