import json

f = open('test.text','r')
#data = eval(f.read())
data = json.load(f)         #反序列化
f.close()
#print(data['age'])
print(data)

#dump可以好几次，但load只能一次