from Automation_project.testpageobjects.testgroupobject import Testgroup
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testsearch_group:
    @pytest.mark.iwebsns
    def test_1_search_group(self,test_edit):
        self.page8=Testgroup(test_edit)
        self.page8.click_group()
        self.page8.click_search_group()
        try:
            self.page8.add_byname('new_group')
            self.page8.click_search()
            print(self.page8.get_result())
            assert self.page8.get_result()=='new_group'
            print('搜索群组成功')
        except AssertionError:
            print('搜索群组失败')

    @pytest.mark.iwebsns
    def test_2_search_group(self,test_edit):
        self.page8=Testgroup(test_edit)
        self.page8.click_group()
        self.page8.click_search_group()
        try:
            self.page8.add_label('1')
            self.page8.click_search()
            print(self.page8.get_result())
            assert self.page8.get_result()=='1'
            print('按类搜索群组成功')
        except AssertionError:
            print('按类搜索群组失败')


