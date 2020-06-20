
import random
print("猜数字小游戏-游戏规则")
print("制作 by jiangyang")
print("按电脑提示猜一个1-100之间的整数，每个人有五次游戏机会，玩完之后下一个")
ask = ""
ask2 = ""

scores = []
Ranking_List = {}

times = []
score = 0
while ask2 != "exit":
 ask = ""
 count = 0
 scores = []
 player_name = input("请输入你的名字 ")
 if player_name.title() not in list(Ranking_List.keys()):
  while ask != 'N' and ask != 'n' :
   import time
 
   if count < 5:
  
    print("注意了，"+player_name.title()+"---猜数字游戏开始 ---,这是你的第"+str(count+1)+"次游戏")
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
     Ranking_List[player_name.title()] = max(scores)
     times.append(time)
  
  
  
     print("目前游戏次数: ",count,"，你的目前最高得分:",max(scores),"，最低用时: ",min(times),"秒\n")
    else:
     print("分数太低，此次成绩不统计\n")
    ask = input("是否要继续进行游戏？输入 N 退出，输入其他任意字符继续：") 
        
  
   else:
    print("你的游戏机会用完啦,请邀请下一位继续")
    print(player_name+"的最高得分:",max(scores),"，最低用时: ",min(times),"秒\n")
    break
  
 
  if Ranking_List:
   rank = 1
 
   
   print("\n        到目前为止比赛排行,从高到低排列\n")
   for rank_palyer, rank_score in sorted(Ranking_List.items(),key=lambda x:x[1],reverse=True):
    
     print("\t"+rank_palyer.title()+" ，得分是："+str(rank_score))
    
   ask2 = input("\n是否成为下一名挑战者？输入 exit 退出，输入其他任意字符继续：")  
 else:
   print("名字不能重复，请重新输入")
