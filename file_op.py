'''
#data = open('thunder',encoding='utf-8').read()    #默认gbk格式
f = open('thunder2','a',encoding='utf-8')   #文件句柄  r = read, w = write, a =append
                                            #read只读   write只写  append可追加不能读
f.write("xushixin\n")                       #r+ 先读后追加模式   w+ 先写后读模式
f.write('qiuya')                            #a+ 先追加后读
f.write('love')                             #rb  转成二进制编码  wb 写成二进制编码

f.close()


f = open('thunder','r',encoding='utf-8')

for index,line in enumerate(f.readlines()):              #读一行内存保存一行
    if index == 9:
        print('---------------')
        continue
    print(line.strip())  # 打印出每行

#print(f.readlines())    #以行为元素划分为列表
#for i in range(5):
#    print(f.readline())

f = open('thunder','r',encoding='utf-8')
count = 0
for line in f:                                         #内存只保存所读的这一行
    if count == 9:
        print('------------')
        count += 1
        continue
    print(line)
    count += 1
'''

f = open('thunder2','r',encoding='utf-8')
#print(f.tell())                              #tell记录第几个字符,当前位置
#print(f.readline())
#print(f.tell())
#f.seek(0)                        #查找   返回到某一位置
#print(f.readline())

#print(f.flush())           #实时刷新内容到被改写的文件

#f.truncate()                #从头开始截取
