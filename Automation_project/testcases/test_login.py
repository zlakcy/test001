from Automation_project.testpageobjects.testloginObject import TestLogPage
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class TestLogin:
    @pytest.mark.iwebsns
    def test_1_login(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file=ReadWrite(datafile_path)
        userlist=file.read()
        user=userlist[0]
        try:
            self.page1.type_username(user[0])
            self.page1.type_password(user[1])
            self.page1.click_login()
            time.sleep(3)
            print(self.page1.get_mypage())
            assert self.page1.get_mypage()=='我的主页'
            print('登录成功!')
        except AssertionError:
            print('登录失败!')

    @pytest.mark.iwebsns
    def test_2_login(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file=ReadWrite(datafile_path)
        userlist=file.read()
        user=userlist[1]
        try:
            self.page1.type_username(user[0])
            self.page1.type_password(user[1])
            self.page1.click_login()
            time.sleep(3)
            print(self.page1.get_pwdtext())
            assert '用户密码错误' in self.page1.get_pwdtext()
            print('错误密码验证成功!')
        except AssertionError:
            print('错误密码验证失败!')
