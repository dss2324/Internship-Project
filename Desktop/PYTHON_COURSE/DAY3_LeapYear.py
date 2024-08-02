year=int(input("enter a year to check if it is leap year or not "));
if(year%400==0 and year%100!=0):
    print(f"{year} is leap year");
#elif(year%100==0):
   # print(f"{year} is not leap year");
elif(year%4==0):
    print(f"{year} is leap year");
else:
    print(f"{year} is not leap year");        