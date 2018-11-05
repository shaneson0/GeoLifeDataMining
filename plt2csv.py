


import os
import numpy as np
import pandas

fields = {
    'id': [],
    "latitude": [],
    'longitude': [],
    'altitude': [],
    'date': [],
    'time': []
}

for root, dirs, files in os.walk("./rawdata", topdown=False):

    for name in files:
        if 'plt' in name:
            userid = int(root.split('/')[2])
            filepath = os.path.join(root, name)
            with open(filepath) as fp:
                lines = fp.readlines()
                lines = lines[6:]
                for line in lines:
                    tempsplit = line.split(',')
                    latitude = tempsplit[0]
                    longitude = tempsplit[1]
                    altitude = tempsplit[3]
                    tempdate = tempsplit[5]
                    temptime = tempsplit[6]
                    fields['id'].append(userid)
                    fields['latitude'].append(latitude)
                    fields['longitude'].append(longitude)
                    fields['altitude'].append(altitude)
                    fields['date'].append(tempdate)
                    fields['time'].append(temptime[:-1])
                print('pass', userid, filepath)


# print(len(fields['id']))

pf = pandas.DataFrame(fields)
pf.to_csv('./data/data.csv')