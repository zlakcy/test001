from Automation_project.testpageobjects.testalbumobject import Testalbum
from Automation_project.config.testconfig import datafile_path
from Automation_project.data.read_write import ReadWrite
from Automation_project.log.log import logger
import time
import pytest

class Testupload:
    @pytest.mark.iwebsns
    def test_1_uploadphotos(self,test_edit):
        self.page6=Testalbum(test_edit)
        self.page6.click_album()
        self.page6.click_upload_photos()
        time.sleep(3)
        try:
            self.page6.select('new')
            self.page6.swich_mode()
            self.page6.click_selfile()
            self.page6.click_upload()
            self.page6.add_photo_name('123')
            self.page6.add_photo_des('123')
            self.page6.click_submit()
            self.page6.click_album()
            self.page6.click_new_album()
            print(self.page6.get_new_photo())
            assert 'photo_id=1589' in self.page6.get_new_photo()
            print('上传相片成功')
        except AssertionError:
            print('上传相片失败')

    @pytest.mark.iwebsns
    def test_2_uploadphotos(self,test_edit):
        self.page6 = Testalbum(test_edit)
        self.page6.click_album()
        self.page6.click_upload_photos()
        time.sleep(3)
        try:
            self.page6.select('new')
            self.page6.swich_mode()
            self.page6.click_selfile()
            self.page6.click_upload()
            assert alert=driver.switch_to.alert
            alert.accept()
            print('无效文件验证成功')
        except AssertionError:
            print('无效文件验证失败')
