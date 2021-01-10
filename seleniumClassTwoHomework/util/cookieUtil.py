#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/10 11:23
# @Author : liujianxiao
# @Version：V 0.1
# @File : cookieUtil.py
# @desc : cookie工具类

# 添加cookie
import json

# 保存cookie
def write_cookie(driver,filepath):
    driver.get(filepath)
    cookies = driver.get_cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)

# 读取cookie
def read_cookie(driver,url,path):
    driver.get(url)
    with open(path, "r") as f:
        cookies=json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

