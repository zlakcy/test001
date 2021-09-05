from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select

class Testaddlog:
    def __init__(self,driver):
        self.browser=driver
        self.log=By.LINK_TEXT,'日志'
        self.createlog=By.LINK_TEXT,'新建日志'
        self.title=By.NAME,'blog_title'
        self.classification=By.NAME,'blog_sort_list'
        self.label=By.NAME,'tag'
        self.content=By.ID,'KINDEDITORBODY'
        self.Select_album=By.NAME,'album_name'
        self.submit=By.CSS_SELECTOR,'[onclick="javascript:is_submit=1;"]'
        self.newlog=By.LINK_TEXT,'123'
        self.message=By.ID,'_DialogTable_0'
        #分类元素
        self.addcategory=By.LINK_TEXT,'添加分类'
        self.class_name=By.NAME,'new_sort_name'
        self.preservation=By.CSS_SELECTOR,'[onclick="saveNowSort();"]'
        self.logclassifiction=By.LINK_TEXT,'日志分类'
        self.new_class=By.LINK_TEXT,'日常'
        self.click_edit=By.CSS_SELECTOR,'[href="javascript:edit_sort(&quot;info_2187&quot;);"]'
        self.click_affirm=By.CSS_SELECTOR,'[onclick="save_sort(&quot;2187&quot;,&quot;change_sort_2187&quot;);"]'
        self.cancel=By.CSS_SELECTOR,'[onclick="exit_sort(&quot;info_2187&quot;,&quot;show_info_2187&quot;,&quot;change_sort_2187&quot;);"]'

    def click_log(self):
        self.browser.find_element(*self.log).click()

    def click_createlog(self):
        self.browser.find_element(*self.createlog).click()

    def add_title(self,title):
        self.browser.find_element(*self.title).send_keys(title)

    def add_classification(self):
        Select(self.classification).select_by_value(*self.classification)

    def add_label(self,label):
        self.browser.find_element(*self.label).send_keys(label)

    def add_content(self,content):
        self.browser.find_element(*self.content).send_keys(content)

    def select_album(self):
        Select(self.Select_album).select_by_value(*self.Select_album)

    def click_submit(self):
        self.browser.find_element(*self.submit).click()

    def get_newlog(self):
        value=self.browser.find_element(*self.newlog).text
        return value

    def get_message(self):
        msg=self.browser.find_element(*self.message).text
        return msg
    #添加分类
    def click_add_category(self):
        self.browser.find_element(*self.addcategory).click()

    def add_class_name(self,class_name):
        self.browser.find_element(*self.class_name).send_keys(class_name)

    def click_preservation(self):
        self.browser.find_element(*self.preservation).click()

    def click_logclassifiction(self):
        self.browser.find_element(*self.logclassifiction).click()

    def get_newclass(self):
        a=self.browser.find_element(*self.new_class).text
        return a
    #编辑分类
    def click_edit_class(self):
        self.browser.find_element(*self.click_edit).click()

    def rename(self,new_class):
        self.browser.find_element(*self.new_class).send_keys(new_class)

    def click_confirm(self):
        self.browser.find_element(*self.click_affirm).click()

    def click_cancel(self):
        self.browser.find_element(*self.cancel).click()
