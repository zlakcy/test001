import pytest
from selenium import webdriver
from Automation_project.config.testconfig import url,driver_path


@pytest.fixture(scope='module')
def test_logsystem(request):
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(10)  # 隐形等待
    yield browser
    browser.quit()

@pytest.fixture(scope='module')
def test_edit(request):
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(url)
    browser.maximize_window()
    browser.find_element_by_name('login_email').send_keys('2510992980@qq.com')
    browser.find_element_by_name('login_pws').send_keys('188006')
    browser.find_element_by_id('loginsubm').click()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
