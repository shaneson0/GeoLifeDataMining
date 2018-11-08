# coding=utf-8

import sys
sys.path.append('../')
import os
import json
from trajectoryPreprocessing.stayPointDetection import stayPointDetection
import pandas as pd
import datetime


def getPointDetection(path):
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

        Points.append({'longitude': Longitude, 'latitude': Latitude, 'T': CurrentTime})

    # print(Points)
    # 0.2公里，30min = 1800S
    Sp = stayPointDetection(Points, 0.2, 1800)
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
                Sp = getPointDetection(filepath)
                AllstayPoints = AllstayPoints + Sp
    return AllstayPoints


def main2():
    pass


if __name__ == '__main__':
    AllstayPoints = main()


    Res = []
    for point in AllstayPoints:
        Res.append({'longitude': point['coord']['longitude'], 'latitude': point['coord']['latitude']})

    with open("allstayPoints.json", mode="w") as fp:
        json.dump(Res, fp)

    # 9819
    print(len(AllstayPoints))











