from Automation_project.testpageobjects.testgroupobject import Testgroup
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testcreate_group:
    @pytest.mark.iwebsns
    def test_1_create_group(self,test_edit):
        self.page7=Testgroup(test_edit)
        self.page7.click_group()
        self.page7.click_creategroup()
        try:
            self.page7.add_groupname('new_group')
            self.page7.add_group_intro('111')
            self.page7.sel_joinmethod()
            self.page7.add_label('111')
            self.page7.click_establish()
            time.sleep(3)
            self.page7.click_group()
            print(self.page7.get_new_group())
            assert self.page7.get_new_group()=='new_group'
            print('创建群组成功')
        except AssertionError:
            print('创建群组失败')

    @pytest.mark.iwebsns
    def test_2_create_group(self,test_edit):
        self.page7=Testgroup(test_edit)
        self.page7.click_group()
        self.page7.click_creategroup()
        try:
            self.page7.add_groupname('')
            self.page7.add_group_intro('111')
            self.page7.sel_joinmethod()
            self.page7.add_label('111')
            self.page7.click_establish()
            time.sleep(3)
            self.page7.click_group()
            print(self.page7.get_message())
            assert '请填写' in self.page7.get_message()
            print('无效标题验证成功')
        except AssertionError:
            print('无效标题验证失败')
