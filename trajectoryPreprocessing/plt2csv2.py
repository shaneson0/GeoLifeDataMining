


import os
import numpy as np
import pandas



for root, dirs, files in os.walk("../rawdata", topdown=False):

    for name in files:
        if 'plt' in name:
            userid = int(root.split('/')[2])
            filepath = os.path.join(root, name)
            with open(filepath) as fp:

                fields = {
                    'id': [],
                    "latitude": [],
                    'longitude': [],
                    'altitude': [],
                    'date': [],
                    'time': []
                }

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

                pf = pandas.DataFrame(fields)

                folerPath = './stayPointDetectionAnalys/%s/%s'%(userid, tempdate)
                if not os.path.exists(folerPath):
                    os.makedirs(folerPath)

                pf.to_csv('./stayPointDetectionAnalys/%s/%s/data.csv'%(userid, tempdate))

                print('pass', userid, tempdate)


