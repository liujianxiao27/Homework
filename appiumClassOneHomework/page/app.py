#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:23
# @Author : liujianxiao
# @Version：V 0.1
# @File : app.py
# @desc :
from appium import webdriver

from appiumClassOneHomework.page.BasePage import BasePage
from appiumClassOneHomework.page.main import Main
from appiumClassOneHomework.util import yamlUtil

# 2KE0220217012386
class App(BasePage):

    # 启动app
    def start(self):
        if self.driver is None:
            desireJson={
                "platformName": "android",
                "deviceName": "2KE0220217012386",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": True,
                "ensureWebviewsHavePages":True,
                "settings[waitForIdleTimeout]":0
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desireJson)
        else:
            self.driver.start_activity() #启动dirver
        self.driver.implicitly_wait(10)
        return self

    # 跳转主页
    def goMain(self):
        return Main(self.driver)