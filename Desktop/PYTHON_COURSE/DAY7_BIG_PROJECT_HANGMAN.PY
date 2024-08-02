import random
#Challenge 1:- picking a random world & checking answer
#todo1:- randomly chose a word from word_list & assign it to a variable called choosen word
#todo2:- ask the user to guess a letter & assign their ans to avariable called guess make guess lowercase
#todo3:-check if letter the user guessed is one of chosen_word
from hangman_words import word_list



lives=6;
choosen_word=random.choice(word_list);
print(f"chosen word is {choosen_word}");

display=[]
for i in range(len(choosen_word)):
    display+="_"    
print(display)
end_of_game=False
from hangman_ascii_art import logo
print(logo);
while not end_of_game:    
    guess=input("Guess a Letter ").lower();
    #check guessed letter
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in choosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose");
    #Join all element in list and turn it into a string
    print(f"{''.join(display)}");
    if "_" not in display:
        end_of_game=True;
        print("You Win")
    from hangman_ascii_art import stages
    print(stages[lives])