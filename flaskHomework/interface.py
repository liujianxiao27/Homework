#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/17 21:40
# @Author : liujianxiao
# @Version：V 0.1
# @File : interface.py
# @desc :接口
import json

import flask
import pymysql
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
# 设置连接数据库的URL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:ljx970227^@cdb-8uss8u9b.gz.tencentcdb.com:10172/horwards"
# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# 测试用例类
class TestCase(db.Model):
    __tablename__ = "testcase"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    steps = db.Column(db.String(1000), unique=False)

    def __repr__(self):
        return '<TestCase %r>' % self.name

class Task(db.Model):
    __tablename__="task"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    caseid = db.Column(db.String(80), unique=False)
    is_delete = db.Column(db.Integer, default=0, server_default='0')


    def __repr__(self):
        return '<task %r>' % self.name


pymysql.install_as_MySQLdb()
# db.create_all()
# 工具类
class util():
    def getTasklist(task: Task):
        id=task.id
        name=task.name
        caseid=task.caseid
        isDelete=task.is_delete
        if isDelete == 1:
            return None
        else:
            testCaseList=[]
            for cid in caseid:
                testcase=TestCase.query.filter_by(id=cid).first()
                if testcase:
                    testcaseJson={
                        "id": testcase.id,
                        "name": testcase.name,
                        "steps": testcase.steps
                    }
                    testCaseList.append(testcaseJson)
                else:
                    pass

            taskJson={
                "id": id,
                "name": name,
                "cases": testCaseList
            }
            return taskJson


# 测试用例接口
class TestCaseService(Resource):
    # 查询
    def get(self):
        name = request.args.get("name",None)
        if name:
            testcase = TestCase.query.filter_by(name=name).first()
            jsonData = {
                "testCase":{
                    "id":testcase.id,
                    "name":testcase.name,
                    "steps":testcase.steps
                }
            }
            return flask.jsonify(jsonData)
        else:
            testcases = TestCase.query.all()
            testCaseList = []
            for testcase in testcases:
                case = {
                    "id":testcase.id,
                    "name":testcase.name,
                    "steps":testcase.steps
                }
                testCaseList.append(case)
            jsonData={
                "testCases": testCaseList
            }
            return flask.jsonify(jsonData)

    # 添加用例
    def post(self):
        name = request.json.get("name")
        steps = json.dumps(request.json.get("steps"))
        testcase = TestCase(name=name,steps=steps)
        db.session.add(testcase)
        db.session.commit()
        return flask.jsonify({"message":"success"})



    # 修改用例
    def put(self):
        id = request.json.get("id")
        steps = request.json.get("steps")
        if id:
            testcase = TestCase.query.filter_by(id=id).first()
            if testcase:
                if steps:
                    testcase.steps = str(steps)
                    db.session.commit()
                    return flask.jsonify({"message": "success"})
                else:
                    return flask.jsonify({"message": "修改项不能为空"})
            else:
                return flask.jsonify({"message": "未找到用例"})
        else:
            return flask.jsonify({"message":"用例Id不能为空"})

    # 删除用例
    def delete(self):
        id = request.json.get("id")
        if id:
            testcase = TestCase.query.filter_by(id=id).first()
            if testcase:
                db.session.delete(testcase)
                return  flask.jsonify({"message": "success"})
            else:
                return flask.jsonify({"message": "未找到用例"})
        else:
            return flask.jsonify({"message":"用例Id不能为空"})

class TaskService(Resource):
    # 获取任务
    def get(self):
        name = request.args.get("name")
        if name:
            task = Task.query.filter_by(name=name).first()
            jsondata={
                "task":util.getTasklist(task)
            }
            return flask.jsonify(jsondata)

        else:
            tasks = Task.query.all()
            taskLsit = []
            for task in tasks:
                taskLsit.append(util.getTasklist(task))
            jsondata = {
                "tasks":taskLsit
            }
            return flask.jsonify(jsondata)

    # 新增任务
    def post(self):
        name = request.json.get("name")
        caseid = request.json.get("caseid")
        if name != None and caseid != None:
            task = Task(name=name,caseid=str(caseid))
            db.session.add(task)
            db.session.commit()
            return flask.jsonify({"message":"success"})
        else:
            return flask.jsonify({"message":"任务名称或关联caseid为空"})

    # 修改任务
    def put(self):
        id = request.json.get("id")
        caseid=request.json.get("caseid")
        if id != None and caseid != None:
            task=Task.query.filter_by(id=id).first()
            if task:
                task.caseid = str(caseid)
                db.session.commit()
                return flask.jsonify({"message": "success"})
            else:
                return flask.jsonify({"message": "未找到该任务"})
        else:
            return flask.jsonify({"message": "id或caseid不能为空"})

    # 删除任务
    def delete(self):
        id = request.json.get("id")
        if id:
            task = Task.query.filter_by(id=id).first()
            if task:
                task.is_delete = 1
                db.session.commit()

                return flask.jsonify({"message": "success"})
            else:
                return flask.jsonify({"message": "未找到该任务"})
        else:
            return flask.jsonify({"message":"id不能为空"})




api.add_resource(TestCaseService,"/testcase")
api.add_resource(TaskService,"/task")

if __name__ == '__main__':
    app.run()