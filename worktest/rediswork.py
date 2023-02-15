import redis
import json
# name='tribe:hot:ids:20201209102029TRB100001640:en'
class redis_conn():
    def __init__(self, r):
        self.r = r
    def getredis(self,name):
        if self.r.type(name)=='string':
            value = self.r.get(name)
            print(self.r.type(name))
            print(value)
            return value
        if self.r.type(name)=='list':
            value = self.r.lrange('object', 0, -1)
            print(self.r.type(name))
            print(value)
            return value
        if self.r.type(name)=='set':
            value = self.r.smembers(name)
            print(self.r.type(name))
            print(value)
            return value
        if self.r.type(name)=='zset':
            value = self.r.zrange(name, 0, -1)
            print(self.r.type(name))
            print(value)
            return value
        if self.r.type(name)=='hash':
            value = self.r.hgetall(name)
            print(self.r.type(name))
            print(value)
            return value

if __name__ =="__main__":
    # port = 6379
    # name = 'tribe:hot:ids:20201209102029TRB100001640:en'

    port = 6379
    name = 'user:cache:user:info:1582211115409043457'
    redis.ConnectionPool(host=host, port=port, decode_responses=True)
    r = redis.Redis(host=host, port=port, decode_responses=True)
    R1 = redis_conn(r)
    value=R1.getredis(name)
    result=json.loads(value)
    result["certificationStatus"]=0
    result1=json.dumps(result)
    r.set(name,result1)
    R1.getredis(name)
