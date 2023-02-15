# https://github.com/PyMySQL/PyMySQL/
import pymysql
from contextlib import closing
import traceback

try:
    # 获取一个数据库连接,with关键字 表示退出时,conn自动关闭
    # with 嵌套上一层的with 要使用closing()
    with closing(pymysql.connect(host='localhost', user='root', passwd='Aa_123456', db='myshopback', port=3306,
                                 charset='utf8')) as conn:

        print("connect database successfully")

        # 获取游标,with关键字 表示退出时,cur自动关闭
        with conn.cursor() as cur:
            sql = """
                           select * FROM users_myuser
                        """
            cur.execute(sql)
            print("select table successfully")
            mycur = cur.fetchall()
            for x in mycur:
                print(x)

except pymysql.Error as e:
    print("Mysql Error:", e)
    traceback.print_exc()