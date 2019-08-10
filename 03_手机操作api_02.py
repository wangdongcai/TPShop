"""
1.学习目标
    掌握进入手机通知栏,获取手机网络,设置手机网络
2.操作步骤(语法)
   driver.open_notifications()  打开手机通知栏
   driver.network_connection    获取手机网络
   driver.set_network_connection() 设置手机网络
3.需求
    打开手机通知栏,点击ApowerMirror
    先获取模拟器的网络,设置模拟器网络飞行模式
4.总结
    打开手机通知栏:driver.open_notifications()
    如果想点击通知栏中的内容,必须是你所启动APP的对应通知
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
# # 4.打开手机通知栏
# driver.open_notifications()
# time.sleep(5)
#
# # 5.进入ApowerMirror
# element = driver.find_element_by_xpath("//*[@text = 'ApowerMirror']")
# 6. 获取手机网络
print(driver.network_connection)

# 7. 设置手机网络
# driver.set_network_connection(2)
# 4 关闭app
time.sleep(5)
driver.quit()