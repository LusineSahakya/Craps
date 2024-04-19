import random
#Function helps to roll dice and have 2 random numbers.
def roll_dice():
    first_die = random.randint(1,6)
    second_die = random.randint(1,6)
#The game counted the sum
    return first_die+second_die;


#Functions helps to run the game.
def playing_craps():
   
    first_roll = roll_dice()
    print("The sum of dice is ",first_roll)
#If the sum of both of them is 7 or 11 the player wins    
    if first_roll in (7,11):
        print("You win!")
#If the sum is 2, 3 or 12 (craps) the casino wins    
    elif first_roll in (2,3,12):
        print("You lose!")
#If during the first roll the sum is 4, 5, 6, 8, 9 or 10, that number becomes the “goal” number.
    else:
        goal_number = first_roll
        print("Your goal_number is", goal_number)


        while True:
            roll = roll_dice()
            print("The sum of dice is ", roll_dice())
# To win, the player should roll the dice till they roll the goal number again.            
            if roll == goal_number:
                print("You win!")
                break
# If the player rolls a 7 before rolling the goal number, they lose.    
            elif roll == 7:
                print("You lose!")
                break
            