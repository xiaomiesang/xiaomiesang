# 在一个函数里面用def声明一个新的函数

# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#     bar()
# foo()

x = 0    #全局变量
def grandpa():
    x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)    #3
        son()
        print(x)        #2
    dad()
    print(x)            #1
grandpa()
print(x)                #0
