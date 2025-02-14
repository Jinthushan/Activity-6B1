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
        print("1 is rock, 2 is paper and 3 is scissors!")
        player_choice = int(input("Pick a number from 1 to 3 or press 0 to end the game: "))
        print("---------------------------------------")
        if(player_choice == 0):
            print("Goodbye!")
            run = False
        else:
            print("I picked " + gameplay)
            if(gameplay == 'rock' and player_choice == 2):
                print("You won!")
            elif(gameplay == 'rock' and player_choice == 3):
                print("You lose")
            elif(gameplay == 'rock' and player_choice == 1):
                print("It was a draw")

            if(gameplay == 'paper' and player_choice == 3):
                print("You won!")
            elif(gameplay == 'paper' and player_choice == 1):
                print("You lose")
            elif(gameplay == 'paper' and player_choice == 2):
                print("It was a draw")

            if(gameplay == 'scissors' and player_choice == 1):
                print("You won!")
            elif(gameplay == 'scissors' and player_choice == 2):
                print("You lose")
            elif(gameplay == 'scisssors' and player_choice == 3):
                print("It was a draw")

game()


