import pandas as pd
import json

data = json.load(open('api.json'))

# z = (data['locations'])
# print(z)
z = (data['locations'])
za =z[0]
#print(za)
#print(za['created'])
zb = (za['measurement'])
print(zb)
zc = zb.get('volts')
print('Volts:', zc)

#print(z)
#df = pd.json_normalize(z[0])
#df.info()
#print(df['address'])
#print(z[0])
