print("welcome to python pizza deliveries")
size=input("what size pizza do you want? S,M,L ")
add_peproni=input("do you want extra peproni? Y/N")
extra_cheese=input("do you want extra chesse? Y/N ")
bill=0;
if(size=='S'):
    bill=bill+15;
    if(add_peproni=='Y'):
        bill=bill+2;
    if(extra_cheese=='Y'):
        bill=bill+1;
elif(size=='M'):
    bill=bill+20;
    if(add_peproni=='Y'):
        bill=bill+3;
    if(extra_cheese=='Y'):
        bill=bill+1;     
else:
    bill=bill+25;
    if(add_peproni=='Y'):
        bill=bill+3;
    if(extra_cheese=='Y'):
        bill=bill+1;
  
print(f"Your total bill is ${bill}");       