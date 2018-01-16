import json


def sayhi(name):
    print('hello',name)

info = {
    'name':'xsx',
    'age':'22',
    #'func':sayhi       #json只能对简单的数据类型进行序列化，是所有语言通用的

}
f = open('test.text','w')
f.write(json.dumps(info))

info['age'] = 21
f.write(json.dumps(info))

f.close()
