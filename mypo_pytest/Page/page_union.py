from appium import webdriver

from mypo_pytest.Page.page_search import PageSearch
from mypo_pytest.base.base_serach import BaseSearch


class PageUinon():
    def union_page_serch(self,driver):
        return PageSearch(driver)

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = 'emulator-5554'
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.Settings'
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# pu=PageUinon()
# pu.union_page_serch(driver).page_click_set()
# pu.union_page_serch(driver).page_input_keys('keys')