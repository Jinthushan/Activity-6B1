import random

def rockpaper():
    x = random.randint(1,3)
    if(x == 1):
        play = "rock"
    elif(x == 2):
        play = "paper"
    elif(x == 3):
        print('scissors')

