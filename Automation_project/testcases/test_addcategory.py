from Automation_project.testpageobjects.testlogobject import Testaddlog
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testaddcategory:
    @pytest.mark.iwebsns
    def test_1_addcategory(self,test_edit):
        self.page3=Testaddlog(test_edit)
        self.page3.click_log()
        time.sleep(3)
        self.page3.click_createlog()
        self.page3.click_add_category()
        try:
            self.page3.add_class_name('日常')
            self.page3.click_preservation()
            self.page3.click_logclassifiction()
            print(self.page3.get_newclass())
            assert self.page3.get_newclass()=='日常'
            print('添加分类成功')
        except AssertionError:
            print('添加分类失败')

    @pytest.mark.iwebsns
    def test_2_addcategory(self,test_edit):
        self.page3=Testaddlog(test_edit)
        self.page3.click_log()
        time.sleep(3)
        self.page3.click_createlog()
        self.page3.click_add_category()
        try:
            self.page3.add_class_name()
            self.page3.click_preservation()
            self.page3.click_logclassifiction()
            print(self.page3.get_message())
            assert '请填写信息' in self.page3.get_message()
            print('无效类名验证成功')
        except AssertionError:
            print('无效类名验证失败')
