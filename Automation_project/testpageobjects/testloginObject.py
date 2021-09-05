from selenium.webdriver.common.by import By

class TestLogPage:
    def __init__(self,driver):
        self.username=By.NAME,'login_email'
        self.password=By.NAME,'login_pws'
        self.submit=By.ID,'loginsubm'
        self.browser=driver
        self.logout=By.LINK_TEXT,'退出'
        self.mypage=By.LINK_TEXT,'我的主页'
        self.pwdmsg=By.CSS_SELECTOR,'p>label>span[id=pwdmsg]'
        self.logform=By.NAME,'login_form'

    def type_username(self,username):
        self.browser.find_element(*self.username).send_keys(username)

    def type_password(self,password):
        self.browser.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.submit).click()

    def get_mypage(self):
        value=self.browser.find_element(*self.mypage).text
        return value

    def get_pwdtext(self):
        msg=self.browser.find_element(*self.pwdmsg).XPATH
        return msg

    def click_signout(self):
        self.browser.find_element(*self.logout).click()

    def get_logform(self):
        z=self.browser.find_element(*self.logform).text
        return z