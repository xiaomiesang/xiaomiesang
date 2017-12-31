name = "xushixin{name}"
print(name.capitalize()) #首字母大写
print(name.count('x')) #统计个数
print(name.center(50,"-")) #打印50个字符，将name居中其余用-补充
print(name.encode())  #转二进制
print(name.endswith("in"))   #判断字符串什么结尾
print(name.find('x'))
print(name.format(name='xsx'))  #格式化{name}
print(name.format_map({'name':'xsx'}))
print('123'.isalnum()) #判断是否纯阿拉伯字符
print('name'.isalpha()) #判断是否纯英文字符
print('name'.isdecimal()) #判断是否十进制
print('name'.isidentifier()) #判断是不是一个合法的标识符（变量名）
print(name.isupper()) #判断是否全是大写
print('+'.join(['1','2','3','4'])) #将+加入到[]各个元素中间
print(name.ljust(50,'+'))  #长度50的情况下字符串在左边，右边又+填补 rjust()正好相反
print(name.lower()) #大写变小写  upper()小写变大写
print(name.lstrip()) #从左边去空格和回车   strip()从两端去空格和回车
print(name.replace('x','X',1))  #替换
print(name.split('x')) #将字符串以x为分隔符切成列表
print(name.swapcase())  #大小写转换
