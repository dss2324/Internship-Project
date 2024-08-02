# conditional statements
#if
x=3
if(x>0):
    print('x is greater than 0')
#else 
x=5
if(x%2==0):
    print('x is divisible by 2')
else:
    print('x is not divisible by 2')    
#elif->else if
y=34
if(y<10):
    print('y is less than 10')
elif(y>10 and y<30):
    print('y is btw 10 to 30')
else:
    print('y is greater than 30')
    
#nested if else
height=int(input('enter your height in cm:'))
age=int(input('enter your age: '))

bill=0;
if(height>120):
    
    if(age>12 and age<=18):
        #print("you have to pay $7 for ride")
        bill=bill+7;
    elif(age<12):
        #print('you have to pay $5')
        bill=bill+5;
    elif(age>=45 and age<=55):
        print("Everything is going to be ok. have a ride ")    
    else:
        #print('you have to pay $12 for ride')
        bill=bill+12;
        
    phototicket=input("do you want your photo y/n ")
    if(phototicket=="y"):
        print("you have to pay extra $3 for photo ")
        bill=bill+3;      
else:
    print('you can not ride') 
    
    
print(f"your total bill for roller coaster ride is ${bill}");   
    
        
