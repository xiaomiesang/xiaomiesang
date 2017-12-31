print("登录".center(50,"-"))

f = open('e:/Python/login.txt')
login = f.read().split(",")
f.close()

name = input("请输入用户名：")
count = 0
while count < 3:
    if name in login:
        pw = input("请输入密码：")
        if pw == login[1]:
            print("登录成功")
            count=0
            exit()
        else:
            count += 1
    else:
        print("用户名错误！")
        pasa
print("账号已经被锁定")

result = ('%s,%s,%d'%(login[0],login[1],count))
f = open('e:/Python/login.txt','w')
f.write(result)
f.close()
