# -*- coding: utf-8 -*-
# @Time : 2020/10/18 23:46
# @Author : wianwu
# @Software: PyCharm 
'''官方文档：https://api.mongodb.com/python/current/api/pymongo/collection.html
    菜鸟教程：https://www.runoob.com/mongodb/mongodb-tutorial.html
'''


import pymongo
'''创建数据库'''
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]

'''判断集合是否存在'''
# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
#
# dblist = myclient.list_database_names()
# # dblist = myclient.database_names()#3.7版本以后就不用这个了
# print(dblist)
# if "test" in dblist:
#     print("数据库已存在！")
# else:
#     print("none")

'''创建集合'''
#一个
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
#
# mycol = mydb["sites"]


'''插入集合'''
# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
#
# x = mycol.insert_one(mydict)
# print(x)
# print(x)

# '''返回_id字段'''
# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# mydb = myclient['runoobdb']
# mycol = mydb["sites"]
#
# mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
#
# x = mycol.insert_one(mydict)
#
# print(x.inserted_id)

#'''插入多个文档'''
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# mylist = [
#     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
#
# x = mycol.insert_many(mylist)
#
# # 输出插入的所有文档对应的 _id 值
# print(x.inserted_ids)

#指定id插入
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["site2"]
#
# mylist = [
#     {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
#     {"_id": 2, "name": "Google", "address": "Google 搜索"},
#     {"_id": 3, "name": "Facebook", "address": "脸书"},
#     {"_id": 4, "name": "Taobao", "address": "淘宝"},
#     {"_id": 5, "name": "Zhihu", "address": "知乎"}
# ]
#
# x = mycol.insert_many(mylist)
#
# # 输出插入的所有文档对应的 _id 值
# print(x.inserted_ids)

'''查询文档'''
## 查询一个文档
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# x = mycol.find_one()
#
# print(x)

# #查询所有
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# for x in mycol.find():
#     print(x)

## 查询指定字段的数据
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
## 参数设置0为不显示，1为显示，如果只设置0则其他为1 ， 反之同理
# for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
#     print(x)
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# for x in mycol.find({},{"alexa": 0 }):
#   print(x)

#条件查询
'''菜鸟教程：https://www.runoob.com/mongodb/mongodb-query.html'''
# #字段查找
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"name": "RUNOOB"}
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

##以下实例用于读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} :
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"name": {"$gt": "H"}}
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

##正则表达式：以下实例用于读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"} :
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"name": {"$regex": "^R"}}
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

#返回指定条数记录
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myresult = mycol.find().limit(3)
#
# # 输出结果
# for x in myresult:
#     print(x)

'''修改文档'''
#修改一条
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"alexa": "10000"}
# newvalues = {"$set": {"alexa": "12345"}}
#
# mycol.update_one(myquery, newvalues)
#
# # 输出修改后的  "sites"  集合
# for x in mycol.find():
#     print(x)

# #修改多条记录
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"name": {"$regex": "^F"}}
# newvalues = {"$set": {"alexa": "123"}}
#
# x = mycol.update_many(myquery, newvalues)
#
# print(x.modified_count, "文档已修改")

'''排序'''
##升序
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# mydoc = mycol.find().sort("alexa")
# for x in mydoc:
#     print(x)

##降序
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# mydoc = mycol.find().sort("alexa", -1)
#
# # for x in mydoc:
# #     print(x)
# print(type(mydoc))

'''删除文档'''

#删除单个
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"name": "Taobao"}
#
# mycol.delete_one(myquery)
#
# # 删除后输出
# for x in mycol.find():
#     print(x)

#删除多个
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# x = mycol.delete_many({})
#
# print(x.deleted_count, "个文档已删除")

#删除集合
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["site2"]
#
# ret = mycol.drop()
# if ret :
#     print("已经删除")
