from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select

class Testgroup:
    def __init__(self,driver):
        self.browser=driver
        self.group=By.LINK_TEXT,'群组'
        self.creategroup=By.LINK_TEXT,'创建群组'
        self.groupname=By.NAME,'group_name'
        self.group_intro=By.NAME,'group_resume'
        self.join_method=By.NAME,'group_join_type'
        self.label=By.NAME,'tag'
        self.category=By.NAME,'group_type_id'
        self.group_logo=By.ID,'group_logo'
        self.establish=By.ID,'UploadButton'
        self.new_group=By.LINK_TEXT,'new_group'
        self.message=By.ID,'_DialogTable_0'

        self.search_group=By.LINK_TEXT,'搜索群组'
        self.byname=By.NAME,'group_name'
        self.bylabel=By.NAME,'tag'
        self.byclass=By.NAME,'group_type_id'
        self.search=By.NAME,'submit'
        self.result=By.LINK_TEXT,'new_group'

    def click_group(self):
        self.browser.find_element(*self.group).click()

    def click_creategroup(self):
        self.browser.find_element(*self.creategroup).click()

    def add_groupname(self,groupname):
        self.browser.find_element(*self.groupname).send_keys(groupname)

    def add_group_intro(self,group_intro):
        self.browser.find_element(*self.group_intro).send_keys(group_intro)

    def sel_joinmethod(self):
        Select(self.join_method).select_by_value(*self.join_method)

    def add_label(self,label):
        self.browser.find_element(*self.label).send_keys(label)

    def sel_category(self):
        Select(*self.category).select_by_value(*self.category)

    def click_group_logo(self):
        self.browser.find_element(*self.group_logo).click()

    def click_establish(self):
        self.browser.find_element(*self.establish).click()

    def get_new_group(self):
        n=self.browser.find_element(*self.new_group).text
        return n

    def get_message(self):
        x=self.browser.find_element(*self.message).test
        return x
    #搜索
    def click_search_group(self):
        self.browser.find_element(*self.search_group).click()

    def add_byname(self,byname):
        self.browser.find_element(*self.byname).send_keys(byname)

    def add_bylabel(self,bylabel):
        self.browser.find_element(*self.bylabel).send_keys(bylabel)

    def click_search(self):
        self.browser.find_element(*self.search).click()

    def get_result(self):
        y=self.browser.find_element(*self.result).text
        return y
