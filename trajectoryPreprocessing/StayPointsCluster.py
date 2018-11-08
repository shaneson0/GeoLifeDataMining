


"""

    使用DBScan进行聚类

"""

from sklearn.cluster import DBSCAN
from math import radians, cos, sin, asin, sqrt

# 单位是米
def haversine(u, v):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1 = u['longitude']
    lat1 = u['latitude']
    lon2 = v['longitude']
    lat2 = v['latitude']

    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

def generateJson():
    with open("allstayPoints.json") as fp:
        X = json.load(fp)
        LocatiionLen = len(X)
        X = np.array(X)
        X = X.reshape(-1, 1)
        distance_matrix = squareform(pdist(X, (lambda u, v: haversine(u[0], v[0]))))
        print(distance_matrix.shape)
        # 景点之间
        db = DBSCAN(eps=600, min_samples=1, metric='precomputed')
        y_db = db.fit_predict(distance_matrix)

        print(y_db)
        print(y_db.shape)

        n_clusters_ = len(set(y_db)) - (1 if -1 in y_db else 0)
        print(n_clusters_)

        ClusterPoints = {}

        for i in range(LocatiionLen):
            ClusterType = y_db[i]
            if ClusterType not in ClusterPoints:
                ClusterPoints[ClusterType] = [X[i][0]]
            else:
                ClusterPoints[ClusterType].append(X[i][0])

        # print(ClusterPoints)
        # print(haversine(116.318417, 39.984702, 116.314107, 39.984649))

        # 求均值
        for k in ClusterPoints.keys():
            Lon = 0.0
            Lat = 0.0
            for coordinate in ClusterPoints[k]:
                Lon = Lon + coordinate['longitude']
                Lat = Lat + coordinate['latitude']

            Lon = float(Lon) / float(len(ClusterPoints[k]))
            Lat = float(Lat) / float(len(ClusterPoints[k]))

            userlist = []
            for point in ClusterPoints[k]:
                userlist.append(int(point['userid']))

            userlist = list(set(userlist))

            ClusterPoints[k] = {
                'longitude': Lon,
                'latitude': Lat,
                'userlist': userlist
            }

        # print(ClusterPoints)

        # 转为矩阵
        FinalClusterPoints = []
        for k in ClusterPoints.keys():
            FinalClusterPoints.append(ClusterPoints[k])

        # print(FinalClusterPoints)
        with open("finalAllStayPoints.json", mode="w") as fp:
            json.dump(FinalClusterPoints, fp)
        # print(ClusterPoints.keys())



from scipy.spatial.distance import pdist, squareform
import json
import numpy as np
import pandas as pd

if __name__ == '__main__':
    LocationLen = 0
    with open("finalAllStayPoints.json") as fp:
        X = json.load(fp)
        LocationLen = len(X)

    # generate user-location Matrix
    username = 182
    UserLocationMatrix = np.zeros((username, LocationLen))

    for locationid, location in enumerate(X):
        for userid in location['userlist']:
            UserLocationMatrix[userid][locationid] = 1

    # 转dataFrame
    index1 = pd.Series(np.arange(1, 11))
    index1 = index1.astype(str)
    index1 = 'A' + index1

    # pd.DataFrame()
    #
    # print(UserLocationMatrix)












