#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 20:20
# @Author : liujianxiao
# @Version：V 0.1
# @File : yamlUtil.py
# @desc : 操作yaml 文件
import yaml


# 获取文件中所有数据


def getDatas(path):
    with open(path,encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas

# 获取文件中指定key的数据
def getDatasBykey(path,key):
    datas = getDatas(path)
    return datas[key]

