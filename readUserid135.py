


import pandas as pd
import json

path = 'data/Userid135.csv'
df = pd.read_csv(path)

# latitude	longitude
latitude = df['latitude'].values.tolist()
longitude = df['longitude'].values.tolist()

Len = len(latitude)

Res = []

for idx in range(Len):
    Latitude = latitude[idx]
    Longitude = longitude[idx]
    Res.append({'Latitude': Latitude, 'Longitude': Longitude})

with open('./data/User135.json', mode='w') as fp:
    json.dump(Res, fp)




