import pymongo
import urllib.parse
MyClient = pymongo.MongoClient("mongodb://root:UXgIbgiLM3ycUO2gB0BNDPAt!@dds-gw8e5676eb7f57e41.mongodb.germany.rds.aliyuncs.com:3717/admin")
print(MyClient.server_info()) #判断是否连接成功
client_list = MyClient.list_database_names()
print(client_list)
print(type(client_list))
database="news_online"
collection='tribe_to_content'
if database in client_list:
     print("数据库已存在！")
     mydb = MyClient[f"{database}"]
     collist = mydb.list_collection_names()
     print(collist)
     if collection in collist:
         print('集合存在')
         Mycollection=mydb[f"{collection}"]
         print("sdsd")
         findstr={
    "$or":[{"audit_status": "Approved"},{"audit_status":"High"},{"audit_status": "Normal"},{"audit_status": "Low"}],
    "tribe_id":"20201209102029TRB100001638",
    "status":"Published"
}
         projection={
        "content_id": 1,
        "final_heat":1,
        "audit_status":1
   }
         x = Mycollection.find_one({{"content_id": '20221224162220MCRO140608545'}})
         print(x)
         result=Mycollection.find(findstr, projection).sort('final_heat', -1).limit(100)
         a=len(list(result))
         result1 = Mycollection.find(findstr, projection).sort('final_heat', -1).limit(100)
         for i in result1:
             print(i)
             a=a-1
             name="_id"
             if name in i.keys():
                UpdateResult=Mycollection.update_one({name:i[name]}, {"$set":{'final_heat': a}})
                 
MyClient.close()





