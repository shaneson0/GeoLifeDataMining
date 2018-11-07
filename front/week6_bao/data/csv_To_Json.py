


import pandas as pd
import json
import datetime
if __name__ == "__main__":

    path = 'data.csv'
    df = pd.read_csv(path)

    # latitude	longitude
    use_id = df['id'].values.tolist()
    latitude = df['latitude'].values.tolist()
    longitude = df['longitude'].values.tolist()
    datelist = df['date'].values.tolist()
    timelist = df['time'].values.tolist()

    Len = len(latitude)

    Points = []

    for idx in range(Len):
        id=use_id[idx]
        Latitude = latitude[idx]
        Longitude = longitude[idx]
        tempDateObject = datelist[idx]
        Points.append({'id':id,'longitude': Latitude, 'latitude': Longitude, 'T':  tempDateObject})

#print (Points)

#print (json.dumps(Points))

fp = open('json_array.json', 'w')
json_array1 = json.dump(Points, fp)
fp.close()
#print(type(json_array1))
#print(json_array1)








