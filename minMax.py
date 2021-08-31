from random import randint

def randomFn(min , max):
    rand = randint(min,max) 
    print("my random digit is: " , rand)
    return rand


res = ""
min = 0
max = 99
while res != "d":
    rand = randomFn(min,max)
    res = input("enter >> ")
    if (res == "d"):
        print("Yeeeeeeeeesssss")
        break
    elif res == "k":
        max = rand - 1
    elif res == "b":
        min = rand + 1
     

