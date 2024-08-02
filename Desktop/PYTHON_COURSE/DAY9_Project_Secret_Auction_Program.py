import os
from DAY9_Project_Secret_Auction_AsciiArt import logo
print(logo)
bidders={}

is_end_of_game=False
max=0
max_winner=''
while is_end_of_game==False:
    bidder_name=input("Enter your name:-")
    bid_value=int(input("What is your bid amount?: $"))
    bidders["Name"]=bidder_name
    bidders["bid_amount"]=bid_value
    if max<bid_value:
     max=bid_value
     max_winner=bidder_name
    choice=input("Are there any other bidders ? yes/no:-")
    if choice=="no":
        is_end_of_game=True
        print(f"Winner of bid is {max_winner} and bid amount is ${max}")
    else:
        clear=lambda:os.system('cls')
        clear() 
    
print(bidders)
    
#Angela had created dictionary first then loop through dictionary where name is key
#and bid amount is value to find higest bidder
    