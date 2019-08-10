"""
1.学习目标
    掌握模拟手势点击方法tap
2.操作步骤(语法)
   driver.tap([最多5个坐标])
3.需求
    打开设置首页,使用tap方法点击蓝牙[86,240][576,325]
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
# 4.使用tap方法点击蓝牙按钮[86,240][576,325]
driver.tap([(100,300),(200,300),(300,250)])
# 4 关闭app
time.sleep(5)
driver.quit()