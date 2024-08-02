import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
#random_draw=random.randint(1,3);
#password=''

#for i in range(0,nr_letters):
#i=letters[random.randint(0,len(letters)-1)]
 #   password=password+i;
#for j in range(0,nr_numbers):
   # j=numbers[random.randint(0,len(numbers)-1)]
   # password=password+j
#for k in range(0,nr_symbols):
    #k=symbols[random.randint(0,len(symbols)-1)]
    #password=password+k;
#print(password)


#hard level
password_list=[]
totalLENGTH=nr_letters+nr_numbers+nr_symbols
for i in range(0,nr_letters):
    i=letters[random.randint(0,len(letters)-1)]
    password_list+=random.choice(letters);
for j in range(0,nr_numbers):
    j=numbers[random.randint(0,len(numbers)-1)]
    password_list+=random.choice(numbers);
for k in range(0,nr_symbols):
    k=symbols[random.randint(0,len(symbols)-1)]
    password_list+=random.choice(symbols);
random.shuffle(password_list);
#print(password_list);

password=''
for x in password_list:
    password=password+x;
print(password);