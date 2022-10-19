from appium import webdriver

class InitWebdriver():
    driver=None
    def __init__(self):
        self.desired_caps = {}
        # 设备信息
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'emulator-5554'
        # app的信息
        self.desired_caps['appPackage'] = 'com.android.settings'
        self.desired_caps['appActivity'] = '.Settings'
        # 中文输入允许
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] = True
    def init_driver(self):
        if self.driver is None:
        # 声明我们的driver对象
          self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        return self.driver

    def quit_driver(self):
        self.driver.quit()
        self.driver=None
