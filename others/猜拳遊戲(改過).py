
# coding: utf-8

# In[3]:

import random
a={'剪刀':0, "石頭":1,"布":2}
while True:
    computer=random.choice(['剪刀', "石頭","布"])
    person=input("剪刀、石頭、布：")
    if person == "quit":
        print("下次再玩")
        break
    elif person == "剪刀" or person =="布" or person == "石頭":
        if computer == person:
            print("電腦出：" , computer)
            print("平手")
        else:
            if a[person] - a[computer] == 1 or a[person] - a[computer] == -2:
                print("電腦出：" , computer , "\n恭喜你贏了！！" )
            else:
                print("電腦出：" , computer,"\n再接再厲～別放棄！")
    else:
        print("輸入錯誤")

