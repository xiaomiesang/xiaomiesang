import time

def consunmer(name):
    print('%s 准备吃包子啦！' %name)
    while True:
        baozi = yield          #yield 保存当前状态并返回值

        print('包子[%s]来了，被[%s]吃了！' %(baozi,name))

def producer(name):
    c = consunmer('A')
    c2 = consunmer('B')
    c.__next__()
    c2.__next__()
    print('老子开始准备做包子啦！')
    for i in range(10):
        time.sleep(1)
        print('做了1个包子，分两半！')
        c.send(i)                   #调用yield并传值
        c2.send(i)
producer('xsx')