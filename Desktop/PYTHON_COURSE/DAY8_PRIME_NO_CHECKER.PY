n=int(input("Enter number to check if it is prime or not:"))

def prime_checker(number):
    count=0
    for i in range(1,number+1):
        if number%i == 0:
            count+=1;
    if count == 2:
        print(f"{number} is prime ")
    else:
        print(f"{number} is not prime")
        
prime_checker(number=n)