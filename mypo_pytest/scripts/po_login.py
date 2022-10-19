from  appium import  webdriver
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'emulator-5554'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 中文输入允许
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#el=driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"更多\").instance(0))")
el=driver.find_element('-android uiautomator','new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"通知\").instance(0))').click()
