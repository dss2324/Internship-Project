import random
import os
from DAY11_BlackJack_Art import logo
#the deck is unlimited in size
#there are no jokers
#the jack/queen/king all count as 10
#the ace can count as 11 or 1 dependeing on situation
#use the following list
#cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#the cards in list have equal probablity of been drawn
#cards are not removed from deck as they are drawn
#the computer is the dealer
def deal_card():
    """_Returns a random card  from deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    """Tke a list of card and return score calculated from cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw 😋"
    elif computer_score==0:
       return "you lost computer wins with blackjack 😢"
    elif user_score==0:
        return "You win with blackjack 😎"
    elif user_score>21:
        return "you went over.you lose 😥 "
    elif computer_score>21:
        return "computer went over you win ✌🏽"
    elif user_score>computer_score:
        return "you win 😁"
    elif computer_score>user_score :
        return "you lose 😟"
    
def playGame():
    print(logo)  
    user_card=[]
    computer_card=[]
    is_game_over=False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
        
        
    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)

        print(f"Users card {user_card} and your score is {user_score}")
        print(f"Computer's first card {computer_card[0]}")
            
        if user_score==0 or computer_score==0 or user_score>21:
         is_game_over=True
        else:
         user_should_deal =  input("Type 'y' to get another card,type 'n' to pass:") 
         if(user_should_deal=='y'):
            user_card.append(deal_card())
         else:
            is_game_over=True


    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)


    print(f"Your final hand {user_card},final score:{user_score}")
    print(f"Computer's final hand {computer_card},final score:{computer_score}")    
    print(compare(user_score,computer_score))
        
while input("do you want to play blackjack game again y/n ?:")=='y':
    clear=lambda:os.system('cls')
    clear() 
    playGame()
    
