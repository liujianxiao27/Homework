#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/9 23:36
# @Author : liujianxiao
# @Version：V 0.1
# @File : yamlUtil.py
# @desc :yaml处理工具类
import yaml

#
def getdatas(path):
    with open(path,encoding="utf-8") as f:
        datas=yaml.safe_load(f)
        return datas
#
def getdatasByKey(path,key):
    with open(path,encoding="utf-8") as f:
        datas=yaml.safe_load(f)[key]
        return datas





def a():
    datas = getdatasByKey('../file/pageYaml/adminContacts.yaml','addDepartment')
    # datas = getdatas('../file/pageYaml/adminContacts.yaml')
    print(datas)

a()