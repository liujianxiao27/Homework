#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/28 11:46
# @Author : liujianxiao
# @Version：V 0.1
# @File : addressBook.py
# @desc : 通讯录
from requestTwo.myFrame.base import Base


class AddressBook(Base):
    # 添加用户  只添加必填字段
    def addMember(self,userid,name,mobile:str,department:list):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        jsonData={
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        result = self.send("post",url,json=jsonData)
        return result


    # 获取用户
    def getMember(self,userId):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userId}"
        result = self.send("get",url)
        return result

    # 修改成员 此处只更改别名
    def updateMember(self,userId,alias):
        url= "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        jsondata={
            "userid": userId,
            "alias": alias
        }
        result = self.send("post",url,json=jsondata)
        return result

    # 删除成员
    def deleteMember(self,userId):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userId}"
        return self.send("post",url)

