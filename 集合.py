list_1 =[1,4,5,7,3,6,7,9]
list_1 = set(list_1)   #创建集合，去重


list_2 = set([2,6,0,66,22,8,1])
'''
print(list_1,list_2)

print(list_1.intersection(list_2))  #取list_1和lits_2的交集

print(list_1.union(list_2))  #取list_1和list_2的并集

print(list_1.difference(list_2))    #取list_1和list_2的差集（差集：我有，你没有）
#print(list_2.difference(list_1))
print(list_1.symmetric_difference(list_2))  #取互相没有的

list_3 =set([1,4,7])
print(list_3.issubset(list_1))   #判断是否是子集
print(list_1.issuperset(list_3)) #判断是否是父集

list_4 = set([2,3,5])
print(list_3.isdisjoint(list_4))    #判断两个集合是否有交集
'''
print(list_1 & list_2)   #交集
print(list_1 | list_2)   #并集
print(list_1 - list_2)   #差集
print(list_1 ^ list_2)   #对称差集

list_1.add(10)    #添加
list_1.update([2,8])   #添加多项
list_1.remove(1)    #删除
print(len(list_1))   #判断长度
print(2 in list_1)   #判断是否在集合
print(list_1)
list_1.discard(888)   #同删除，但是删除不存在的东西不会报错