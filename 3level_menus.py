data ={
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":["CICC","HP"]
        },
    },
    '浙江':{
        "杭州":{
            "滨江":["星光大道","东方郡"],
            "江干":["四季青","下沙大学城"]
        },
        "温州":{
            "龙湾":["电商大厦","安邦护卫"],
            "瓯海":["至潮电影院","医科大学"]
        },
    },
    '广西':{
        "桂林":{
            "阳朔":["十里画廊","小吃街"]
        },
        "南宁":{
            "青秀":["广西大学","万象城"]
        },
    },
}                                               #创建多级菜单
exit_flag = False                               #定义exit_flag为False
while not exit_flag:                            #当exit_flag不为True时进入死循环
    for i in data:
        print(i)                                #打印第一层菜单

    choice = input("请选择进入省份：")
    if choice in data:                          #判断choice是否存在
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)                  #打印第二层

            choice2 = input("请选择进入城市：")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)                      #打印第三层

                    choice3 = input("请选择进入地区：")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t",i4)                        #打印第四层
                        choice4 = input("已到最后，按b返回")
                        if choice4 == "b":
                            pass                                      #输入b，返回上一层
                        elif choice4 == "q":
                            exit_flag = True                          #将exit_flag设为True，结束循环，退出

                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True

