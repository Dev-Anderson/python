import json 
f = open("data.json")
data = json.load(f)
print(data)
for i in data['lastName']:
    print(i)
f.close()