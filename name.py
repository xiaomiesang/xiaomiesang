import copy


names = ["xsx","wj","cyf",[1,2],"ct","zjm","lhf"]
#names.append("pl")#追加一个pl到列表最后位置
#names.insert(1,"wj")#插入，第一个数值为插入的位置
#names[2] ="wj"#修改内容

#delect
#names.remove("cyf")#删除
#del names[0]#删除第几个
#del names[1] = names.pop(1)
#names.pop()#默认删除最后一个
print (names)
#print (names[0],names[2]) #输出列表第一个和第三个
#print (names[1:3]) #切片
#print (names[-2:])#切片 -2代表倒数第二个数，注意切片是从左到右切
#print (names.index("xsx"))#索引"xsx"的位置
#print (names[names.index("xsx")])#找到并打印
#print (names.count("wj"))#统计"wj"的个数
#names.clear()#清空names
#names.reverse()#反转names
#names.sort()#排序 （特殊符号-数字-大写-小写）

#names2 = [1,2,3,4]
#names.extend(names2)#扩展合并
#print(names)


#names2 = names.copy()#浅复制（只复制列表第一层）
names2 = copy.deepcopy(names)#深度复制
print(names,names2)
names[2]="陈逸峰"
names[3][0]="120"
print(names)
print(names2)

