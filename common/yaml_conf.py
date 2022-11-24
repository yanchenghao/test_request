from os.path import *

import yaml

# pwd=os.getcwd()
# print(pwd)
extrayaml = dirname(abspath(__file__)) + sep + "extract.yaml"
#提取yaml文件数据
def yaml_load(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
       sd=yaml.load(f,Loader=yaml.FullLoader)
       print(sd)
       return sd
#提取测试参数和断言
def get_yaml_data(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
       sd=yaml.load(f,Loader=yaml.FullLoader)
       print(sd)
    list=[0 for x in range(len(sd))]
    list1=[]
    b=0
    for i in range(len(sd)):
        list1.append(sd[i]["data"])#提取请求参数
        list1.append(sd[i]["check"])#提取要断言的结果
        list[i]=list1
        list1=[]
    return list
    # for a in sd:
    #     list1.append(a["data"])
    #     list1.append(a["check"])
    #     list.append(list1)
    # # list1=[]
    # # for b in sd:
    # #     list1.append(b["code"])
    # return list
#将字典，生成yaml文件
def yaml_dump(extract_dict):
    with open(extrayaml,"a") as f:
        sd=yaml.dump(extract_dict,f,encoding="utf-8",allow_unicode=True)
#清除yaml 文件
def yaml_clear():
    with open(extrayaml,"w") as f:
        f.truncate()

