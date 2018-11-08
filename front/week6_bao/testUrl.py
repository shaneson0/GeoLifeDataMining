

'''
This is for testing, don't worry


'''
import os
import numpy as np
import pandas
import json

points = []
result = []
def getDateByFile():
    for root, dirs, files in os.walk("../../trajectoryPreprocessing/stayPointDetectionJsonType", topdown=False):
       # print (root,dirs,files)
        for name in files:
            if 'json' in name:
                userid = int(root.split('\\')[1])
                date=str(root.split('\\')[2])
                filepath = os.path.join(root, name)
                if userid==9 and  date=='2008-10-24':
                    f = open(filepath, encoding='utf-8')  # 设置以utf - 8
                    # 解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
                    setting = json.load(f)
                    for i in range(len(setting)):
                            result.append(setting[i])
    return result
   # print("result", result)




if __name__ == '__main__':
    getDateByFile()
    print (result)
