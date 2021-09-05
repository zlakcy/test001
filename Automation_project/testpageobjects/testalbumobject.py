from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select

class Testalbum:
    def __init__(self,driver):
        self.browser=driver
        self.album=By.LINK_TEXT,'相册'
        self.createalbum=By.LINK_TEXT,'新建相册'
        self.album_name=By.ID,'album_name'
        self.album_des=By.ID,'album_information'
        self.album_label=By.ID,'tag'
        self.setting=By.ID,'isns_album::'
        self.only=By.NAME,'all'
        self.friends=By.NAME,'friends'
        self.define=By.CSS_SELECTOR,'[onclick="expression()"]'
        self.cancel=By.CSS_SELECTOR,'[onclick="menu_pop_cancel()"]'
        self.create=By.NAME,'action'
        self.message=By.ID,'_DialogTable_0'
        self.my_album=By.LINK_TEXT,'我的相册'
        self.new_album=By.LINK_TEXT,'new'

        self.upload_photos=By.LINK_TEXT,'上传相片'
        self.select_album=By.NAME,'album_name'
        self.swich=By.LINK_TEXT,'切换上传方式'
        self.sel_file=By.ID,'attach[]'
        self.upload=By.NAME,'submit'
        self.photo_name=By.NAME,'photo_name[]'
        self.photo_des=By.NAME,'photo_information[]'
        self.submit=By.NAME,'action'
        self.new_photo=By.ID,'isns_photo:1589:'

    def click_album(self):
        self.browser.find_element(*self.album).click()

    def click_createalbum(self):
        self.browser.find_element(*self.createalbum).click()

    def add_album_name(self,album_name):
        self.browser.find_element(*self.album_name).send_keys(album_name)

    def add_album_des(self,album_des):
        self.browser.find_element(*self.album_des).send_keys(album_des)

    def add_album_label(self,album_label):
        self.browser.find_element(*self.album_label).send_keys(album_label)

    def click_setting(self):
        self.browser.find_element(*self.setting).click()

    def click_only(self):
        self.browser.find_element(*self.only).click()

    def click_friends(self):
        self.browser.find_element(*self.friends).click()

    def click_define(self):
        self.browser.find_element(*self.define).click()

    def click_cancel(self):
        self.browser.find_element(*self.cancel).click()

    def click_create(self):
        self.browser.find_element(*self.create).click()

    def click_my_album(self):
        self.browser.find_element(*self.my_album).click()

    def get_new_album(self):
        b=self.browser.find_element(*self.new_album).text
        return b

    def get_message(self):
        c=self.browser.find_element(*self.message).test
        return c

    def click_upload_photos(self):
        self.browser.find_element(*self.upload_photos).click()

    def select(self):
        Select(self.select_album).select_by_value(*self.select_album)

    def swich_mode(self):
        self.browser.find_element(*self.swich).click()

    def click_selfile(self):
        self.browser.find_element(*self.sel_file).click()

    def click_upload(self):
        self.browser.find_element(*self.upload).click()

    def add_photo_name(self,photo_name):
        self.browser.find_element(*self.photo_name).send_keys(photo_name)

    def add_photo_des(self,photo_des):
        self.browser.find_element(*self.photo_des).send_keys(photo_des)

    def click_submit(self):
        self.browser.find_element(*self.submit).click()

    def click_new_album(self):
        self.browser.find_element(*self.new_album).click

    def get_new_photo(self):
        m=self.browser.find_element(*self.new_photo).text
        return m