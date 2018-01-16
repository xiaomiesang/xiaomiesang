import pickle


def sayhi(name):
    print('hello',name)

info = {
    'name':'xsx',
    'age':'22',
    'func':sayhi       #pickle可对所有数据类型进行序列化

}
f = open('test.text','wb')
#.write(str(info))
print(pickle.dumps(info))            #序列化  默认二进制
#f.write(pickle.dumps(info))
pickle.dump(info,f)       #等同上句
f.close()
