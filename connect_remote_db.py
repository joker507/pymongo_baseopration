# -*- coding: utf-8 -*-
# @Time : 2020/10/20 19:31
# @Author : wianwu
# @Software: PyCharm 

import pymongo

if __name__ == '__main__':
    url = "mongodb://127.25.38.228:27017/"
    urlloc = "mongodb://localhost:27017/"
    # client = pymongo.MongoClient(host="47.95.216.136", port=27017)
    client = pymongo.MongoClient(url)

    # # 如果数据库不存在，则创建名为school的库
    # db = client['school']
    #
    # collection = db.students
    # student = {
    #     "id": "1234",
    #     "name": "sky",
    #     "gender": "male",
    # }
    # result = collection.insert_one(student)
    # print(result)

    dblist = client.list_database_names()  # db 查询命令：show dbs
    # dblist = myclient.database_names()#3.7版本以后就不用这个了
    print(dblist)
    if "test" in dblist:
        print("数据库已存在！")
    else:
        print("none")

