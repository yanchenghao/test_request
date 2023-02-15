
import redis

redis.ConnectionPool(host='172.31.32.245', port=6379, decode_responses=True)
r = redis.Redis(host='172.31.32.245', port=6379, decode_responses=True)
name='tribe:hot:ids:20201209102029TRB100001640:en'
# start=r.delete(name)
# print(start)
# r.hdel(name,'first:All:en:10')
key=r.hgetall(name)
print(key)  # dahe
key['first:All:en:10']='["20221215071413MCRO140607449"]'
print(key)  # dahe
a=str(key)
print("aaaaaaa"+a)
print(type(key))  # dahe
print(type(a))  # dahe
# r.hset(name=name,key='first:All:en:10', value='["20221215071413MCRO140607448"]')
r.hset(name=name,mapping=key)
key3=r.hgetall(name)
print(key3)  # dahe
print(type(key))  # dahe
print("ddsdsd")
key3=r.hgetall(name)
print(key3)  # dahe
print(type(key))  # dahe


