from Automation_project.testpageobjects.testlogobject import Testaddlog
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testeditclass:
    @pytest.mark.iwebsns
    def test_1_editclass(self,test_edit):
        self.page4=Testaddlog(test_edit)
        self.page4.click_log()
        time.sleep(3)
        self.page4.click_createlog()
        self.page4.click_logclassifiction()
        self.page4.click_edit_class()
        try:
            self.page4.rename('日常活动')
            self.page4.click_confirm()
            print(self.page4.get_newclass())
            assert self.page4.get_newclass()=='日常活动'
            print('编辑分类成功')
        except AssertionError:
            print('编辑分类失败')

    @pytest.mark.iwebsns
    def test_2_aditclass(self,test_edit):
        self.page4=Testaddlog(test_edit)
        self.page4.click_log()
        time.sleep(3)
        self.page4.click_createlog()
        self.page4.click_logclassifiction()
        self.page4.click_edit_class()
        try:
            self.page4.rename('日常活动')
            self.page4.click_cancel()
            print(self.page4.get_newclass())
            assert self.page4.get_newclass()=='日常'
            print('取消编辑成功')
        except AssertionError:
            print('取消编辑失败')
