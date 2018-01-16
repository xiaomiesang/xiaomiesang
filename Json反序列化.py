import json

f = open('test.text','r')
#data = eval(f.read())
data = json.loads(f.read())         #反序列化
f.close()
#print(data['age'])
print(data)