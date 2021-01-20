#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/20 10:36
# @Author : liujianxiao
# @Version：V 0.1
# @File : handel.py
# @desc :装饰器
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appiumClassThreeHomework.util import yamlUtil

# 黑名单处理
def handel_blacklist(fun):
    def run(*args,**kwargs):
        try:
            # 调用方法若无报错直接返回
            return fun(*args,**kwargs)
        except Exception as e:
            # 解析黑名单
            blacklists = yamlUtil.getdatasBykey("../file/blacklist.yml","xueqiu")
            # 循环处理黑名单
            for black in blacklists:
                by = black["by"]
                locator = black["locator"]
                action = black["action"]
                self = args[0]
                # elements = self._driver.find_elements(by,locator)
                elements = WebDriverWait(self._driver,30).until(expected_conditions.element_to_be_clickable((by,locator)))
                elements=self._driver.find_elements(by, locator)
                if len(elements) > 0:
                    if action == "click":
                        elements[0].click()
                # 处理完成后再次调用方法
                return fun(*args,**kwargs)
            raise e
    return run
