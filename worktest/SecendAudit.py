import pymysql
import pymongo
from datetime import datetime, timedelta

crawler_mongo_uri = "mongodb://root:UXgIbgiLM3ycUO2gB0BNDPAt!@dds-gw8e5676eb7f57e41.mongodb.germany.rds.aliyuncs.com:3717/news_online?authSource=admin"
crawler_mongo_client = pymongo.MongoClient(crawler_mongo_uri)
cursor = crawler_mongo_client.get_database('news_online')

id = "20230215030404MCRO140609540"

mysql_conn = pymysql.connect(
    host='rm-gw8uu4urpvcm8rx50.mysql.germany.rds.aliyuncs.com',
    port=3570,
    user='afnews_app',
    password='rrDYkE73B8GJdWWDv4y7',
    db='afnews_main'
)
mysql_cursor = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)

micro_blog = cursor["micro_blog"].find_one({"id": id})
print(micro_blog)

def get_author_detail(author_id):
    sql = "SELECT * FROM afnews_main.t_patron_user where id='{}';".format(author_id)
    mysql_cursor.execute(sql)
    result = mysql_cursor.fetchone()
    return result


author_info = get_author_detail(micro_blog['author_id'])


data = {
    "content_id": id,
    "language": micro_blog['language'],
    "country": micro_blog['country'],
    "post_time": micro_blog['post_time'],
    "author_name": author_info['nickname'],
    "author_id": micro_blog['author_id'],
    "create_time": datetime.utcnow(),
    "update_time": datetime.utcnow(),
    "media_type": micro_blog["resource_type"],
    "view": 1,
    "heat": 0,
    "resource_type": micro_blog["resource_type"],
    "source_type": "USER",
}
# print(data)
cursor['review_audit_user'].insert_one(data)

print("===end===")