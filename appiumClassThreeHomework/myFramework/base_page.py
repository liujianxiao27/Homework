#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/7 10:33
# @Author : liujianxiao
# @Version：V 0.1
# @File : base_page.py
# @desc :
import yaml
from appium.webdriver.webdriver import WebDriver

from appiumClassThreeHomework.myFramework.handel import handel_blacklist
from appiumClassThreeHomework.util import yamlUtil


class BasePage():
    errorCount = 0
    errorMax = 3

    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    # 查找元素
    # by 查找方式 支持元组(by,locator)若以元组形式不用传locator字段
    # locator 定位元素
    @handel_blacklist
    def find(self,by,locator):
        #查询元素
        element = self._driver.find_element(by,locator)
        return element


    # 输入文案
    def sendkey(self,value,element):
            element.send_keys(value)


    # 从yml文件读取数据进行页面操作
    def steps(self,path,key=None):
        if key is None:
            steps = yamlUtil.getdatas(path)
        else:
            steps = yamlUtil.getdatasBykey(path,key)
        for step in steps:
            by = step["by"]
            locator = step["locator"]
            action = step["action"]
            element = self.find(by,locator)
            if action == "click":
                element.click()
            elif action == "sendkeys":
                self.sendkey(step["value"],element)

