#def test(*args):           #加上* 代表args的数值个数不固定,接收n个位置参数，转换成元组
#    print(args)
#test(1,2,3)
#test(*[1,2,3])    #*args = tuple([1,2,3])


def test2(**kwargs):            #把n个关键字参数转换成字典的方式
    print(kwargs)

#test2(name = 'xsx',age = 8, sex = 'F')


def test3(name,x=1,*args,**kwargs):
    print(name)
    print(x)
    print(args)
    print(kwargs)
test3('xsx','sx',1,2,3,age = 18)