import sys,time


for i in range(50):
    sys.stdout.write('#')     #sys.stdout  标准输出，屏幕就是标准输出
    sys.stdout.flush()  #当不加这句时候，会先把内存占满然后一起输出#，加了后会实时输出
    time.sleep(0.1)
