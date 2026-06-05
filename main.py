import random
num = random.randint(1,21)
enemynum= random.randint(1,21)
print("player is the bottom number")
print(enemynum,"🂠")
finalnum = None
    #giving player there cards
while num <=21:

        print (num,"🃏")
    #give the player the option to hit or stand
        NextMove =input("do you want to hit or stand   ").strip().lower()
        print(NextMove)
        if NextMove == "hit":
    #add the new card to the existing hand
            num+= random.randint(1,10)
            print(num)
        elif NextMove =="stand":
            break
#enemyplayer hand
        if enemynum <21:
            enemynum += random.randint(1,10)
                    
            # finalnum = num + random.randint(1,10)
        if enemynum > num:
            if num or enemynum ==21:
                    print("bust")
            else:
                print("YOU WON 🥳")
                

