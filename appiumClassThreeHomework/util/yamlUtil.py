#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/12 11:23
# @Author : liujianxiao
# @Version：V 0.1
# @File : yamlUtil.py
# @desc : yaml工具类
import yaml


def getdatas(path):
    with open(path,'r',encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas

def getdatasBykey(path,key):
    datas = getdatas(path)
    return datas[key]




def t():
    datas = getdatasBykey("../file/main.yml","goMarket")
    for data in datas:
        print(data["by"])

t()
