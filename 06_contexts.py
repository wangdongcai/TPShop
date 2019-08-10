"""
1.学习目标
    掌握获取context方法
2.操作步骤(语法)
   获取当前页面的context
    driver.current.context
    获取所有页面的contexts
    driver.contexts
3.需求
    打开百度app,获取当前页面的context,进入微博登陆页面后再获取所有contexts
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
desired_caps["appPackage"] = "com.baidu.searchbox"  # app包名
desired_caps["appActivity"] = ".MainActivity"  # app启动名
# 3 实例化webdriver---操作对象手机
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 4.点击未登录,进入个人中心
driver.find_element_by_xpath("//*[@text = '我的']").click()
# 5.获取当前context
home_page = driver.current_context
print(home_page)
# 6.在个人中心点击微博按钮
driver.find_element_by_accessibility_id("微博登录").click()
time.sleep(5)
# 7.获取所有contexts
contexts = driver.contexts
print(contexts)
# 8.进入webview页面
driver.switch_to.context(contexts[1])
# 9.输入微博账号
driver.find_element_by_id("loginName").send_keys("123456")
# 10 退出webview
driver.switch_to.context(home_page)
# 11.点击关闭按钮
driver.find_element_by_xpath("//*[@text = '关闭']").click()
# 4 关闭app
time.sleep(5)
driver.quit()