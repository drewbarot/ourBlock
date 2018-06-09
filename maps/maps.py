from datetime import datetime
import json

import os.path
import collections


data = {}

if os.path.isfile('maps.json') :
    with open ('maps.json', 'r+') as fp:
        data = json.load(fp)
        
for key in list((data.keys())):
    val = data[key]
    del data[key]
    data[int(key)] = val

lat = 43.751119
long = -79.509755

id = 0

if len(list(sorted(data.keys()))) == 0:
    id = 0
else:
    id = int(list(data.keys())[len(list(sorted((data.keys())))) - 1]) + 1
    
date = datetime.now()

month = date.strftime("%B")

day = date.strftime("%d")

year = date.strftime("%Y")

hour = date.strftime("%H")

data[id] = {"Year": year, "Month": month, "Day": day, "Hour": hour, "Latitude": lat, "Longitude": lat}


ordered_data = collections.OrderedDict(sorted(data.items()))

with open('maps.json', 'w') as f:
    json.dump(ordered_data, f)