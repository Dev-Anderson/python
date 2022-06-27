import json 

f = open('data.json')
data = json.loads(f.read())
for i in data['firstName']:
    print(i)
f.close()