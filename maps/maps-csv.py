from datetime import datetime
import json
from collections import OrderedDict
import os.path
from math import log
from math import e
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from math import sqrt

data = OrderedDict()
weights = []
lat = []
long = []

num_points = 500

if os.path.isfile('maps.json') :
    with open ('maps.json', 'r+') as fp:
        data = json.load(fp, object_pairs_hook=OrderedDict)
        
for key in range(len(list(data.keys()))):
    if key > num_points:
        break
    stored = data[list(data.keys())[len(list(data.keys())) - 1 - key]]
    
    month = stored['Month']
    day = stored['Day']
    year = stored['Year']
    
    lat.append(stored['Latitude'])
    long.append(stored['Longitude'])
    
    date = month + " " + str(day) + ", " + str(year)
    
    date_format = "%B %d, %Y"
    
    now = datetime.now()
    
    date_object = datetime.strptime(date, date_format)
    
    delta = now - date_object
    
    num_hours = delta.days*24

    weights.append(sqrt(1.0/num_hours) * 1000)


weights = np.array(weights)
weights = weights.reshape(-1, 1)

min_max_scaler = MinMaxScaler(feature_range=(0, 2))

weights = min_max_scaler.fit_transform(np.float32(weights))

weights = weights.tolist()

points = OrderedDict()

for i in range(num_points):
    points[i] = {"Latitude": lat[i], "Longitude": long[i], "Weight": weights[i][0]}

with open('heat_map.json', 'w') as f:
    json.dump(points, f, indent=4, separators=(',', ': '))

