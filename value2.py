import json

data = json.load(open('api.json'))
x = json.dumps(data)
y = json.loads(x)

#print(y["login"])

print(y["login"])

## parse x:

#y = json.loads(x)

## the result is a Python dictionary:

#print(y['locations'])

#print (y['measurement'][3]['percent'])