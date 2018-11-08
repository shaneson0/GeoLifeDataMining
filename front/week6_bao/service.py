
import json
import  testUrl
import os
import numpy as np
import pandas
import json

#文件路径，用来找json数据
url="./data/json_array.json"
def  getJsonData(user_id=9,date='2018-11-08'):
    print ("getJSONDate拿到数据",user_id,date)
    result = []
    f = open(url, encoding='utf-8') # 设置以utf - 8
    #解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    for i in range(len(setting)):
        if  user_id==setting[i]['id'] and date==setting[i]['T']:
          result.append(setting[i])
    print ("result",result)
    resultsjson=json.dumps(result)    #结果变成json格式返回
    #print (results)
    return resultsjson


result=[]
def  getJsonDataBy_File(id=9,date='2008-10-24'):
    #Read data from a file and display it on a web page
    for root, dirs, files in os.walk("../../trajectoryPreprocessing/stayPointDetectionJsonType", topdown=False):
        # print (root,dirs,files)
        for name in files:
            if 'json' in name:
                file_userid = int(root.split('\\')[1])
                file_date = str(root.split('\\')[2])
                filepath = os.path.join(root, name)
                if file_userid == id and file_date == date:
                    f = open(filepath, encoding='utf-8')  # 设置以utf - 8
                    # 解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
                    setting = json.load(f)
                    for i in range(len(setting)):
                        result.append(setting[i])
    resultJson=json.dumps(result);
    return resultJson;


# # Put_to_JSONFile
# def resultToJSONFile():
#     fp = open('result.json', 'w')
#     json_array1 = json.dump(result, fp)
#     fp.close()
#


getJsonData()