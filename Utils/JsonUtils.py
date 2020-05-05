'''
@Desc: JSON工具类
@Author: Martin Huang
@Date: 2020-04-01 21:23:38
@Modify Notes: 
    2020/04/01 => 增加从指定路径读取JSON配置文件，并返回字典
    2020/04/01 => 增加将JSON字符串转换成字典返回
    2020/05/05 => 增加将JSON字典写回文件功能
'''
import json

class JsonUtils:
    #从指定路径path读取配置文件，并返回字典
    def json2Dict(path):
        with open(path,'r',encoding='utf-8') as f:
            jsonDict = json.loads(f.read())
        return jsonDict
    
    # 将JSON字符串转换为字典
    def jsonStr2Dict(jsonString):
        jsonDict = json.loads(jsonString)
        return jsonDict

    # 将JSON字典写回文件
    def json2File(path,jsonDict):
        with open(path,'w',encoding='utf-8') as f:
            json.dump(jsonDict,f,ensure_ascii=False,indent=4)