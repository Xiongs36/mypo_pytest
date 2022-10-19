import os,sys

from mypo_pytest.Page import loc_set, loc1_input, loc_return

sys.path.append(os.getcwd())
from mypo_pytest.base.base_serach import BaseSearch

from appium import webdriver

class PageSearch(BaseSearch):
    def page_click_set(self):
        self.base_click_element(loc_set)
    def page_input_keys(self,value):
        self.base_input_element(loc1_input, value)
    def page_click_return(self):
        self.base_click_element(loc_return)
# desired_caps = {}
#         # 设备信息
# desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = 'emulator-5554'
#         # app的信息
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.Settings'
#         # 中文输入允许
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
#         # 声明我们的driver对象
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# pu=PageSearch(driver)
# pu.page_click_set()
# pu.page_input_keys('keys')
# pu.page_click_return()