import time
def logger():
    time_format = '%Y-%m-%d %X'               #定义时间格式
    time_current = time.strftime(time_format) #引用时间格式
    with open('a.txt','a+') as f:
        f.write('%s end action\n' %time_current)

def text1():
    print('test1 starting action...')

    logger()

def text2():
    print('test2 starting action...')

    logger()


def text3():
    print('test3 starting action...')

    logger()

text1()
text2()
text3()