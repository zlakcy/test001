from Automation_project.testpageobjects.testalbumobject import Testalbum
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testalbum:
    @pytest.mark.iwebsns
    def test_1_create_album(self,test_edit):
        self.page5=Testalbum(test_edit)
        self.page5.click_album()
        self.page5.click_createalbum()
        try:
            self.page5.add_album_name('new')
            self.page5.add_album_des('123')
            self.page5.add_album_label('123')
            self.page5.click_setting()
            self.page5.click_define()
            self.page5.click_create()
            time.sleep(3)
            self.page5.click_my_album()
            print(self.page5.get_new_album())
            assert self.page5.get_new_album()=='new'
            print('创建相册成功')
        except AssertionError:
            print('创建相册失败')

    @pytest.mark.iwebsns
    def test_2_create_album(self,test_edit):
        self.page5=Testalbum(test_edit)
        self.page5.click_album()
        self.page5.click_createalbum()
        try:
            self.page5.add_album_name(' ')
            self.page5.add_album_des('123')
            self.page5.add_album_label('123')
            self.page5.click_setting()
            self.page5.click_define()
            self.page5.click_create()
            time.sleep(3)
            print(self.page5.get_message())
            assert '请正确填入相册名' in self.page5.get_message()
            print('无效相册名验证成功')
        except AssertionError:
            print('无效相册名验证失败')

