#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/28 13:02
# @Author : liujianxiao
# @Version：V 0.1
# @File : test_addressbook.py
# @desc : 通讯录用例
import json

from requestTwo.myFrame.addressBook import AddressBook


class TestAddressBook():
    addressbook = AddressBook()

    # 测试添加成员
    def test_add(self):
       # 查询是否存在此成员
       userid = "suolong"
       searchMemberResult = self.addressbook.getMember(userId=userid)
       # 若存在则删除该用户
       if searchMemberResult.json().get("userid") == "suolong":
           self.addressbook.deleteMember(userId=userid)
       # 添加用户
       result = self.addressbook.addMember(userid=userid,name="索隆",mobile="16930000000",department=[2])
       # 获取接口返回数据并且断言
       errmsg = result.json().get("errmsg")
       assert errmsg == "created"

    # 测试修改用户
    def test_update(self):
        userid="suolong"
        # 查询用户是否存在
        searchMemberResult=self.addressbook.getMember(userId=userid)
        print("errcode:",searchMemberResult.json().get("errcode") )
        # 若不存在添加用户
        if searchMemberResult.json().get("errcode") == 60111:
            addresult = self.addressbook.addMember(userid=userid, name="索隆", mobile="16930000000", department=[2])
        # 请求修改用户
        result = self.addressbook.updateMember(userId=userid,alias="海贼猎人")
        # 断言修改结果
        errmsg = result.json().get("errmsg")
        assert errmsg == "updated"
        # # 断言查询成员信息
        member = self.addressbook.getMember(userId=userid)
        assert member.json().get("alias") == "海贼猎人"