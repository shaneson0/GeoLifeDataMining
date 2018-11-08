
import json
import numpy as np
import pandas as pd
import json

import sys
sys.path.append("../")
from trajectoryDataMining import CF_svd_knn

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

data = np.array(UserLocationMatrix)

cf = CF_svd_knn.CF_svd(k=3, r=1)
# cf = CF_knearest(k=1)
recommendlist = cf.fit(data)

res = {}
for userid, recommendItems in enumerate(recommendlist):
    tempRecommendItem = []
    for recommendId in recommendItems:
        tempRecommendItem.append({"longitude": X[recommendId]["longitude"], "latitude": X[recommendId]["latitude"]})
    res[userid] = tempRecommendItem

print(res)
with open('recommendRes.json', mode='w') as fp:
    json.dump(res, fp)



















