import requests
import json

police_response = requests.get('http://c4s.torontopolice.on.ca/arcgis/rest/services/CADPublic/C4S/MapServer/0/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A-8883817.175430955%2C%22ymin%22%3A5400734.670536719%2C%22xmax%22%3A-8844681.416948998%2C%22ymax%22%3A5439870.429018676%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100')
police_json = police_response.json()

break_ins = []
for i in police_json['features']:
    date_time = i['attributes']['ATSCENE_TS'].split(" ")[0]
    street_1 = i['attributes']['XSTREETS'].split("-")[0]
    street_2 = i['attributes']['XSTREETS'].split("-")[1]
    type = i['attributes']['TYP_ENG']
    if type == "BREAK & ENTER":
        break_ins.append([street_1, street_2, date_time, type])
    

break_i = []

for i in break_ins:
    street_1 = i[0]
    street_2 = i[1]
    
    date = i[2]
    
    response = requests.get("https://geocoder.cit.api.here.com/6.2/geocode.json?city=Toronto&street=" + street_1 + "%40%20" + street_2 + "&app_id=rVpfKtRBGBtZDJKZ9Gbm&app_code=ZMu35JxtwhF2fGAScL_sMw&gen=8")
     
     
    json_data = response.json()
     
    lat = json_data['Response']['View'][0]['Result'][0]['Location']['MapView']['BottomRight']['Longitude']
    long = json_data['Response']['View'][0]['Result'][0]['Location']['MapView']['BottomRight']['Latitude']
     
    break_i = [lat, long, date]

print(break_i)
