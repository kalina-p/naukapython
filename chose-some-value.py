# -*- coding: utf-8 -*-

import json
json_data=open('api.json')
data=json.load(json_data)
# print(data['locations'])
z = (data['locations'])
for k, v in data.items():
    if k == 'measurement':
        print(v)



