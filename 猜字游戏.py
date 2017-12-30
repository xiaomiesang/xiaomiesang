from random import randint  #使随机

f = open('e:/Python/xsx.txt')
score = f.read().split()    #读取数据
f.close()
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times >0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0
print('你已经玩了%d次，最少%d轮猜出数字，平均%.2f轮猜出数字'%(game_times,min_times,avg_times))


num = randint(1,100)
times = 0                   #记录游戏轮数
print ('猜猜数字是多少？')
bingo = False
while bingo == False:
    times += 1
    answer = eval(input())
    if answer>num:
        print('大了')
    elif answer<num:
        print('小了')
    else :
        print('对了')
        bingo = True
if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
result = ('%d %d %d'%(game_times,min_times,total_times))
f = open('e:/Python/xsx.txt','w')
f.write(result)
f.close()
