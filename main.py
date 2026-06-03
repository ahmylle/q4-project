import random
num = random.randint(1,21)
rndmNum= random.randint(1,21)
print(rndmNum)
finalnum = None
#giving player there cards
while num <=21:
    if num <21:
        print("you lost")
    print (num,"🃏")
    #give the player the option to hit or stand
    NextMove =input("do you want to hit or stand   ").strip().lower()
    print(NextMove)
    if NextMove == "hit":
           finalnum = num + random.randint(1,10)
           print(finalnum)
    else:
        if NextMove==("stand"):
                    break
        if num > 21:
                print("bust")
                if rndmNum > num:
                    print("you lost")
                else:
                    if num :21
                    print("you won")
            

