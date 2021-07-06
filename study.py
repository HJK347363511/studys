from appium import webdriver
import time
server = "http://localhost:4723/wd/hub"
param = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}

driver = webdriver.Remote(server,param)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el3.click()
for i in range(100):
    driver.swipe(320, 1150, 320, 300, 1000)
    time.sleep(5)
driver.quit()