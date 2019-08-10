"""
作业
1.封装滑动方法  swipe
    
2.滑动到指定元素
   
3.判断是否滑动到底部

"""
class Swipe:
    def __init__(self,driver):
        self.driver = driver
        self.size = self.driver.get_window_size()

    def swipe_up(self):
        """向上滑动"""
        x = self.size['width']*0.5
        start_y = self.size['height']*0.75
        end_y = self.size['height']*0.25
        self.driver.swipe(x,start_y,x,end_y,duration=5000)
# 1 导入appium
from appium import webdriver
import time

# 2 准备设备参数
desired_caps = {}
# 设备信息
desired_caps["platformName"] = "android"  # 系统名称
desired_caps["platformVersion"] = "5.1.1"  # 系统版本
desired_caps["deviceName"] = "bc"  # 设备名称
# app信息
desired_caps["appPackage"] = "com.android.settings"  # app包名
desired_caps["appActivity"] = ".Settings"  # app启动名
# 3 实例化webdriver---操作对象手机
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 4.滑动到指定元素
while True:
    try:
        driver.find_element_by_xpath("//*[@text = '日期和时间']").click()
        break
    except:
        Swipe(driver).swipe_up()

# 4 关闭app
time.sleep(5)
driver.quit()