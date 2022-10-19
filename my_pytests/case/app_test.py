from time import sleep

import  pytest
from appium import webdriver
from selenium.webdriver.common.by import By


class AppTest():
    def test_app(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'emulator-5554'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 中文输入允许desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        driver.find_element(By.XPATH, '//*[contains(@text,"更多")]').click()
        sleep(3)
        net_lists = driver.find_elements(By.ID, 'android:id/title')
        lists = []
        for i in net_lists:
            lists.append(i.get_attribute('text'))
        assert '移动网络' in lists, 'error'
        driver.quit()

    @pytest.mark.run(order=1)
    def test_01(self):
        assert False

    @pytest.mark.run(order=2)
    def test_02(self):
        assert False
if __name__ == '__main__':
    pytest.main(['-s',"app_test.py"])