import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors];
user_choice=int(input("What do you choose ? type 0 for rock, 1 for paper & 2 for scissors\n "));

if(user_choice>=3 or user_choice<0):
    print("You Typed an invalid number, you lose");
else: 
  print("YOU CHOOSE ");
  print(game_images[user_choice])
computer_choice=random.randint(0,2);
print("COMPUTER CHOOSE ");
print(game_images[computer_choice])
if(user_choice>=3 or user_choice<0):
    print("") 
else:    
  if(user_choice==0 and computer_choice==2):
    print("YOU WIN ")
  elif(computer_choice>user_choice):
    print("COMPUTERS WINS ");
  elif(computer_choice==0 and user_choice==2):
    print("COMPUTER WINS");
  elif(user_choice>computer_choice):
     print("YOU WIN")
  elif(computer_choice==user_choice):
     print("It's a Draw");    
