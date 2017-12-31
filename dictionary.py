'''
av_catalog = {
    "欧美":{
        "www.youporn.com":["很多免费的，世界最大的","质量一般"],
        "www.pornhub.com":["很多免费的，也很大","质量比yourporn搞点"],
        "letmedothistoyou.com":["多是自拍，高质量图片很多","资源不多，更新慢"],
        "x-art.com":["质量很高，真的很高","全部收费"]
    },
    "日韩":{
        "tokyo-hot":["质量怎么样不清楚","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费","服务器在国外"]
    }
}
av_catalog['大陆']['1024'][1]='可以做镜像'
av_catalog.setdefault("台湾",{"www.google.com":["免费","要翻墙"]})  #新增一个值，如果已经存在便不做修改

print(av_catalog)
'''
info = {
    'stu01':'xsx',
    'stu02':'wj',
    'stu03':'msc',
    'stu04':'lhf'
}
for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)                           #中间有个把字典变成列表的过程，不高效

'''
b ={
    'stu01':'wq',
    1:3,
    2:5
}
info.update(b)          #将info和b合并，已存在的key的value被覆盖，不存在就添加
print(info)
c = dict.fromkeys([6,7,8],"test")     #初始化新字典
print(c)
print(info.items())     #将字典转换成列表
'''
'''
print(info)              #字典是无序的
print(info['stu02'])
print(info.get('stu05'))     #查找
#info['stu01']='徐时鑫'   #存在就修改
#info['stu05']='cyf'      #不存在就创建
#del info['stu05']        #删除
#info.pop('stu05')         #删除
print('stu02' in info)     #判断stu02是否在info中
print(info)
'''
