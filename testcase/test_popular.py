import pytest
import requests
from common import log_config
from common import http_requests
from common import yaml_conf
from config import conf
import os
logger= log_config.GetLogger.get_logger()
request1=http_requests.HttpRequest()
protocol=conf.get_protocol()
host=conf.get_host()

header=yaml_conf.yaml_load("./data/header.yaml")
list=yaml_conf.get_yaml_data("./data/all.yaml")


path = "/api/content/index/all"
url1=protocol+host+path
@pytest.mark.parametrize("params,check", list)
# @pytest.mark.usefixtures("login")
# @pytest.mark.usefixtures("login1")
def test_popular(login,params,check):
    # params=params["type"]
    # print(params)
    # params=params["data"]
    print("222222222")
    print(login)
    header["authorization"] = login
    print(params)
    print(url1)
    print(header)
    logger.info("当前url:" + url1)
    # url="http://api.molelive.com/api/content/index/all"
    logger.info("当前的测试参数"+str(params))
    logger.info("当前的check" + str(check))
    # print(pams)
    r1=request1.request(url1,headers=header,params=params,http_method="get",timeout=5,verify=False)
    # r1=requests.get(url1,params=params,headers=header)
    # logger1.logger.info(r1["body"])
    logger.info("当前的返回结果" + str(r1))
    print(r1)
    assert r1["body"]["code"] == check["code"]
    assert r1["code"] == 200
    # print(r1.content)
    # print(r1.url)
    # print(header)
    # print(r1.request)
    # print(r1.text)
    # assert  r1.status_code==200
    # assert r1.json()["code"] == 1


