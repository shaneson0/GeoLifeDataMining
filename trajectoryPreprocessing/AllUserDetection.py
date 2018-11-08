# coding=utf-8

import sys
sys.path.append('../')
import os
import json
from trajectoryPreprocessing.stayPointDetection import stayPointDetection
import pandas as pd
import datetime


def getPointDetection(path, userid):
    df = pd.read_csv(path)

    # latitude	longitude
    latitude = df['latitude'].values.tolist()
    longitude = df['longitude'].values.tolist()
    datelist = df['date'].values.tolist()
    timelist = df['time'].values.tolist()

    Len = len(latitude)

    Points = []

    for idx in range(Len):
        Latitude = latitude[idx]
        Longitude = longitude[idx]
        tempDateObject = datelist[idx]
        tempTimeObject = timelist[idx]
        # 2009/1/3:1:21:34
        try:
            CurrentTime = datetime.datetime.strptime(tempDateObject + ":" + tempTimeObject, '%Y/%m/%d:%H:%M:%S')
        except:
            CurrentTime = datetime.datetime.strptime(tempDateObject + ":" + tempTimeObject, '%Y-%m-%d:%H:%M:%S')
        if Longitude > 115.25 and Longitude < 117.30 and Latitude > 39.26 and Latitude < 41.03:
            Points.append({'longitude': Longitude, 'latitude': Latitude, 'T': CurrentTime, 'userid': userid})

    # print(Points)
    # 0.2公里，30min = 1800S
    # 景点detection, 设置为1公里， 1小时
    # 北京市界的地理坐标为：北纬39”26’至41”03’，东经115”25’至 117”30’。
    # 需要摒除掉住所，假设呆在景点为3个小时
    Sp = stayPointDetection(Points, 2000, 7200, 10800, userid)
    return Sp


# 首先，逐级读取文件，获取 Userid 和 datetime
def main():
    AllstayPoints = []
    for root, dirs, files in os.walk("./stayPointDetectionAnalys", topdown=False):
        for name in files:
            if 'csv' in name:
                userid = root.split('/')[-2]
                datetime = root.split('/')[-1]
                filepath = os.path.join(root, name)
                Sp = getPointDetection(filepath, userid)
                AllstayPoints = AllstayPoints + Sp

    return AllstayPoints


def main2():
    pass


if __name__ == '__main__':
    AllstayPoints = main()


    Res = []
    for point in AllstayPoints:
        Res.append({'longitude': point['coord']['longitude'], 'latitude': point['coord']['latitude'], 'userid': point["userid"]})

    with open("allstayPoints.json", mode="w") as fp:
        json.dump(Res, fp)

    # 9819
    print(len(AllstayPoints))











