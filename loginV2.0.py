'''
编写登录接口：
    1.输入用户名和密码登录
    2.输错三次锁定账户
    3.下次登录还是上次的账户，提示锁定，直接退出（用到文件读写）
    4.成功 后显示登录成功
'''

lock = 'E:/PyCharmproject/day1/lock.text'                  #lock定义为锁定文件
account = 'E:/PyCharmproject/day1/account.text'            #account定义为账户文件
count = 0                                                  #计数器
flag = 1                                                   #标识器
#定义锁定用户列表为空
lock_user = []

#打开锁定文件，并读取锁定账户
user_lock = open('lock.text','r')
lock_file = user_lock.readlines()
user_lock.close()

#循环锁定账户，将账户追加到lock_user列表中
for _user in lock_file:
    _user = _user.strip('\n')
    lock_user.append(_user)

#打开账户文件，并读取用户和密码
user_file = open('account','r')
user_list = user_file.readlines()
user_file.close()

name = input('请输入用户名')
while count < 3:
    if name in lock_user:
        print('该用户名已被锁定')
        break
    else:
        passwd = input('请输入密码')
        count += 1
        for user in user_list:
            (_name,_passwd) = user.strip('\n').split()
            if name == _name:
                if passwd == _passwd:
                    print('登录成功')
                    flag = True
                    break
                else:
                    print('用户名或密码错误')
                    break
    if flag is True:
        break
else:
    print('验证失败，用户名被锁定')
    with open('lock.text','a') as f:
        f.write(name +'\n')



