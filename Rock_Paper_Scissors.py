import random

def rockpaper():
    x = random.randint(1,3)
    if(x == 1):
        play = "rock"
    elif(x == 2):
        play = "paper"
    elif(x == 3):
        play = 'scissors'
    return play,x

def game():
    run = True
    while(run == True):
        print("Welcome to Rock Paper Scissors!")
        gameplay,x = rockpaper()
        player_choice = input("Pick a number from 1 to 3 or press 0 to end the game")
        player_choice = input("1 is rock, 2 is paper and 3 is scissors!")
        print("---------------------------------------")
        if(player_choice == 0):
            print("Goodbye!")
            run = False
        else:
            print("I picked " + gameplay)
            if(player_choice == x):
                print("You won!")
            else:
                print("You lose")

game()


