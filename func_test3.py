def test(x,y,z):
    print(x)
    print(y)
#test(y=2,x=1) #与形参顺序无关
#test(1,2)     #与形参一一对应
test(3,z=2,y=6) #关键参数不能放在位置参数前面