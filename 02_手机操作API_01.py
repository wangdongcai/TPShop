"""
1.学习目标
    掌握获取手机时间和发送键到设备
2.操作步骤(语法)
    driver.device_time  获取手机时间
    driver.keyevent(keycode)
   
3.需求
    在设置APP中,获取手机当前时间,按3次增加音量
4.总结

"""
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
# 4.获取手机当前时间
print(driver.device_time)
# 5.增大手机音量按3次
for i in range(3):
    driver.keyevent(24)
# 6 关闭app
time.sleep(5)
driver.quit()