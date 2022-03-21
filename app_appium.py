# coding=utf-8
import time

from appium import webdriver
from PIL import Image

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'appPackage': 'com.xingin.xhs',
    'appActivity': 'com.xingin.xhs.activity.SplashActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 登录 TODO：账号密码登录报错，提示登陆异常，要验证码登录
def login():
    time.sleep(3)
    # 开始同意按钮
    el1 = driver.find_element_by_id("com.xingin.xhs:id/ctf")
    el1.click()
    time.sleep(10)
    # 手机号码登录按钮
    el2 = driver.find_element_by_id("com.xingin.xhs:id/d07")
    el2.click()
    time.sleep(5)
    # 选择密码登录
    el5 = driver.find_element_by_id("com.xingin.xhs:id/d53")
    el5.click()
    time.sleep(5)
    # 输入账号
    el6 = driver.find_element_by_id("com.xingin.xhs:id/d0a")
    el6.send_keys("XXXX")
    time.sleep(5)
    # 输入密码
    el7 = driver.find_element_by_id("com.xingin.xhs:id/d12")
    el7.send_keys("XXXX")
    time.sleep(5)
    # 点击登录
    el8 = driver.find_element_by_id("com.xingin.xhs:id/d0c")
    el8.click()
    time.sleep(3)
    # 点击同意
    el7 = driver.find_element_by_id("com.xingin.xhs:id/cte")
    el7.click()

    
# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向下滑动---->刷新
def swipeDown(t):
    size = getSize()
    x1 = int(size[1] * 0.5)
    y1 = int(size[0] * 0.75)
    y2 = int(size[0] * 0.05)
    driver.swipe(x1, y1, x1, y2, t)


def main():
    login()
    while True:
        swipeDown(500)
        time.sleep(5)


if __name__ == '__main__':
    main()