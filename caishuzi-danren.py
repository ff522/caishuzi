
import random
ask = ""
count = 0
scores = []
Ranking_List = {}
times = []
score = 0
while ask != 'N' and ask != 'n':
 import time
 print("---猜数字游戏开始---")
 Guess_number = random.randint(0,100)
 #Guess_number = 50 #测试用
 starttime=time.time()
 print('请输入1--100整数:')
 i = 0
 a = 0
 
 while a != Guess_number:
    try:
        i = i + 1
        a = int(input("输入数字： "))
        if a - Guess_number < -10:
            print('遗憾，太小了')
        elif a - Guess_number >= -10 and a - Guess_number < 0:
            print('遗憾，有点小了')
        elif a - Guess_number <= 10 and a - Guess_number > 0:
            print('遗憾，有点大了')
        elif a - Guess_number > 10:
            print('遗憾，太大了')
        else:
         if i <= 3:
          endtime=time.time()
          time=int(endtime-starttime)
          score = 100-5*i 
          print('太棒了，只用了'+str(i)+'次，就猜中了正确数字 '+str(Guess_number))
          print('游戏得分:'+str(score)+'，游戏用时'+str(time)+'秒\n')
         elif i>=4 and i<=10:
          endtime=time.time()
          time=int(endtime-starttime)
          score = 100-5*i 
          print('还行，只用了'+str(i)+'次，就猜中了正确数字 '+str(Guess_number))
          print('游戏得分:'+str(score)+'，游戏用时'+str(time)+'秒\n')
         else:
          endtime=time.time()
          time=int(endtime-starttime)
          score = 100-5*i
          print('你用了'+str(i)+'次,终于猜中了，要加油了')
          print('你总共花了'+str(time)+'秒完成游戏\n')
            
    except ValueError:      #异常处理
        print('输入错误，请输入整数：')
 count = count + 1
 if score > 50: 
  scores.append(score)
  Ranking_List[count] = [score,time]
  times.append(time)
  
  
  
  print("目前游戏次数: ",count,"，目前最高得分:",max(scores),"，最低用时: ",min(times),"秒\n")
 else:
  print("分数太低，此次成绩不统计\n")
  
        
 ask = input('是否要重新进行游戏？输入 N 退出，输入其他任意字符继续：')
if Ranking_List:
 #Ranking_List1 = sorted(Ranking_List.items(),key=lambda x:x[1],reverse=True)
 #print(Ranking_List1)
 print("\n        本次比赛排行,从高到低排列\n")
 for rank_count, rank_scores in sorted(Ranking_List.items(),key=lambda x:x[1],reverse=True):
   print("第"+str(rank_count)+"次游戏，得分"+str(rank_scores[0])+"，用时"+str(rank_scores[1])+"秒")
