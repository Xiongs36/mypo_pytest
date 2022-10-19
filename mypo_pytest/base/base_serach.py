# import os,sys
#
# sys.path.append(os.getcwd())
#定义类名
from selenium.webdriver.support.wait import WebDriverWait


class BaseSearch():
    def __init__(self,driver):
        self.driver=driver
    # 定义元素显示等待
    def base_find_element(self,loc,timeout=30,poll_frequency=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))
    # 点击方法
    def base_click_element(self,loc):
        self.base_find_element(loc).click()

    #输入方法
    def base_input_element(self,loc,value):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
# driver=InitWebdriver().init_webdriver()
# bs=BaseSearch(driver)
# #搜索按钮
# loc=By.ID,'com.android.settings:id/search'
# bs.base_click_element(loc)
# #输入搜索内容
# loc1=By.ID,'android:id/search_src_text'
#
