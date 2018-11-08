# coding = utf-8

"""

    Author: 陈善轩

    这个文件是用进行Stay point Detect的，参考《Mining User Similarity Based on Location History》的Figure 2的实现代码


"""



from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

def computMeanCord(PointArray):
    Len = len(PointArray)
    longitude = 0.0
    latitude = 0.0
    for i in range(Len):
        longitude = longitude + PointArray[i]["longitude"]
        latitude = latitude + PointArray[i]["latitude"]
    return {"longitude": longitude / Len, "latitude": latitude / Len}

# longitude, latitude

# Detect User's stay Points
def stayPointDetection(Points, distThreh, timeThreh, MaxtimeThreh, userid):
    Sp = []
    i = 0
    PointNumber = len(Points)
    while i < PointNumber:
        j = i + 1
        MaxLen = -1
        while j < PointNumber:
            dist = haversine(Points[j]["longitude"], Points[j]["latitude"], Points[i]["longitude"], Points[i]["latitude"])
            if dist > MaxLen:
                MaxLen = dist
            if dist > distThreh:
                S = {}
                T = (Points[j]['T'] - Points[i]['T']).seconds
                if T > timeThreh and T < MaxtimeThreh:
                    print('pass', T)

                    S["coord"] = computMeanCord(Points[i: j+1])
                    S["arvT"] = Points[i]['T']
                    S["levT"] = Points[j]['T']
                    S["userid"] = userid
                    Sp.append(S)
                i = j
                break
            j = j + 1
        if MaxLen < distThreh:
            break
    return Sp




import pandas as pd
import json
import datetime
if __name__ == "__main__":

    path = '../data/Userid135.csv'
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
        CurrentTime = datetime.datetime.strptime(tempDateObject + ":" + tempTimeObject, '%Y/%m/%d:%H:%M:%S')

        Points.append({'longitude': Latitude, 'latitude': Longitude, 'T': CurrentTime})

    # print(Points)
    # 0.2公里，30min = 1800S
    Sp = stayPointDetection(Points, 0.2, 1200)
    print(Sp)










