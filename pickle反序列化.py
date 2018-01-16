import pickle

def sayhi(name):
    print('hello',name)
    print('hello2', name)

f = open('test.text','rb')
#data = eval(f.read())
#data = pickle.loads(f.read())         #反序列化
data = pickle.load(f)     #等同上句
f.close()
#print(data['age'])
print(data['func']('xsx'))