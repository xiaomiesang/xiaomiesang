product_list = [
    ('苹果手机',5800),
    ('苹果电脑',9800),
    ('自行车',800),
    ('手表',1000),
    ('书',100),
]                            #创建一张商品列表
shopping_list = []           #创建一张空的购物车列表用于存储选择的商品
salary = input('请输入您的工资:')                    #输入工资
if salary.isdigit():
    salary = int(salary)                             #判断工资是不是数字
    while True:                                      #当工资是数字的时候进入循环
        for index,item in enumerate(product_list):       #enumerate函数取出商品列表的下标
            #print(product_list.index(item),item)
            print(index,item)                            #打印带序号的商品列表
        user_choice = input("请选择您要购买的商品：")    #用户选择商品编号
        if user_choice.isdigit():                        #判断用户输入的编号必须是数字类型
            user_choice = int(user_choice)               #赋予编号整型
            if user_choice < len(product_list) and user_choice >=0:   #判断编号大小是不是在列表长度内
                p_item = product_list[user_choice]                    #通过选择的编号取出对应的商品
                if p_item[1]<=salary:                                 #判断对应商品的价格是否小于等于工资
                    shopping_list.append(p_item)                      #将商品加入到购物车列表
                    salary -=p_item[1]                                #现有的工资等于原有的减去购买商品的价格
                    print('已将%s加入购物车,您的余额还有\033[31;1m%s\033[0m元'%(p_item,salary))   #打印已购买的商品和余额
                else:
                    print('\033[31;1m您的余额只剩%s元了，无法购买！\033[0m'%salary)       #资金不足以购买时提示余额
            else:
                print ('\033[41;1m商品不存在，请重新选择！\033[0m')       #当编号不在商品列表内，提示商品不存在
        elif user_choice == 'quit':                            #判断用户输入quit
            print('----------购物清单---------')
            for p in shopping_list:
                print (p)
            print ('您的余额还剩\033[31;1m%s\033[0m元'%salary)
            exit()                                              #打印购物车列表，提示余额并退出
        else:
            print('\033[41;1m请输入正确的编号!\033[0m')         #输入编号不为数字时提示
else:
    print('\033[41;1m错误的输入方式！!\033[0m')                 #输入工资不为数字时提示

# \033[数字;1m *** \033[0m --->  设置字体颜色的固定格式 31为红色  32为绿色