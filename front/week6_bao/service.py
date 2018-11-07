
import json




def  getJsonData(user_id=9,date='2008-10-23'):
    result = []
    f = open("./data/json_array.json", encoding='utf-8') # 设置以utf - 8
    #解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    for i in range(len(setting)):
        #print (setting[i])
        #if  user_id==setting[i]['id'] and date==setting[i]['T']:
          result.append(setting[i])

    #print (result)
    #resultToJSONFile()    #结果存入文件
    results=json.dumps(result)    #结果变成json格式返回
    #print (results)
    return results




# # Put_to_JSONFile
# def resultToJSONFile():
#     fp = open('result.json', 'w')
#     json_array1 = json.dump(result, fp)
#     fp.close()
#


getJsonData()