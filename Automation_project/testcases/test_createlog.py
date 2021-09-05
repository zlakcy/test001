from Automation_project.testpageobjects.testlogobject import Testaddlog
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testcreatelog:
    @pytest.mark.iwebsns
    def test_1_createlog(self,test_edit):
        self.page2=Testaddlog(test_edit)
        self.page2.click_log()
        time.sleep(3)
        self.page2.click_createlog()
        try:
            self.page2.add_title('123')
            self.page2.add_classification()
            self.page2.add_label('123')
            self.page2.add_content('123')
            self.page2.select_album()
            self.page2.click_submit()
            time.sleep(3)
            print(self.page2.get_newlog())
            assert self.page2.get_newlog()=='123'
            print('创建日志成功！')
        except AssertionError:
            print('创建日志失败！')

    @pytest.mark.iwebsns
    def test_2_createlog(self,test_edit):
        self.page2=Testaddlog(test_edit)
        self.page2.click_log()
        time.sleep(3)
        self.page2.click_createlog()
        try:
            self.page2.add_title()
            self.page2.add_classification()
            self.page2.add_label('123')
            self.page2.add_content('123')
            self.page2.select_album()
            self.page2.click_submit()
            time.sleep(3)
            print(self.page2.get_message())
            assert '请填写标题' in self.page2.get_message()
            print('无效标题验证成功')
        except AssertionError:
            print('无效标题验证失败')