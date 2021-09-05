from Automation_project.testpageobjects.testloginObject import TestLogPage
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testlogout:
    @pytest.mark.iwebsns
    def test_1_logout(self,test_edit):
        self.page=TestLogPage(test_edit)
        try:
            self.page.click_signout()
            assert '登录邮箱' in self.page.get_logform()
            print('用户登出成功')
        except AssertionError:
            print('用户登出失败')
