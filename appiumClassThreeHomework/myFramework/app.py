#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/7 11:55
# @Author : liujianxiao
# @Version：V 0.1
# @File : app.py
# @desc :
from time import sleep

from appium import webdriver

from appiumClassThreeHomework.page.Main import Main
from appiumClassThreeHomework.myFramework.base_page import BasePage
from appiumClassThreeHomework.util import yamlUtil


class App(BasePage):

    # 启动app
    def startApp(self):
        if self._driver is None:
            desireJson = yamlUtil.getdatasBykey("../file/appPackage.yml", "XueQiu")
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desireJson)
        else:
            self._driver.start_activity() #启动dirver
        self._driver.implicitly_wait(10)
        return self

    # 关闭app
    def endApp(self):
        sleep(4)
        self._driver.quit()

    # 跳转至主页
    def goMain(self):
        return Main(self._driver)


