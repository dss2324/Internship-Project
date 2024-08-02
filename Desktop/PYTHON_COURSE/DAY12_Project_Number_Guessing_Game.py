#from DAY12_NumberGuessingGame_AsciiArt import logo
import random
computer_pick=random.randint(1,100)
is_end_ofGame=False
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 to 100")
choose_difficulty=input("choose a difficulty level 'easy' or 'hard' :")
if choose_difficulty=='easy':
    no_of_attempts=10
else:
    no_of_attempts=5
    
while no_of_attempts>0 and is_end_ofGame==False:
    
    def make_guess():
        global no_of_attempts
        user_pick=int(input("Make a Guess:"))
        if(user_pick>computer_pick):
            print("To High\nGuess again")
            no_of_attempts=no_of_attempts-1
        elif(user_pick<computer_pick):
            print("To low\nGuess again")
            no_of_attempts=no_of_attempts-1
        elif(user_pick==computer_pick):
            print(f"You got it You win the answer is {user_pick}")
            global is_end_ofGame
            is_end_ofGame=True
            
    make_guess()
    if no_of_attempts>0 and is_end_ofGame==False:     
     print(f"You have {no_of_attempts} remaining to guess the number")
     make_guess()
    elif no_of_attempts==0 and is_end_ofGame==False:
     print("You have run out of guessing\nYou lose") 
    