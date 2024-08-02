year=int(input("enter the year: "))
if(year%4==0 and year%400==0):
    print("the year is leap")
else:
    print("year is not leap")