def is_Leap(year):
    #year=int(input("enter a year to check if it is leap year or not "));
    if(year%400==0 and year%100!=0):
       # print(f"{year} is leap year");
       return True
    #elif(year%100==0):
    # print(f"{year} is not leap year");
    elif(year%4==0):
        #print(f"{year} is leap year");
        return True
    else:
        #print(f"{year} is not leap year"); 
        return False
    
def days_in_months(year,month):
    if month>12 or month<1:
        return "Invalid Month"
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    #special case for leap year and february
    if is_Leap(year)==True and month==2:
        return 29
    #any other case
    return month_days[month-1]
    


           
year=int(input("Enter a Year :"))
month=int(input("Enter a Month :"))
days=days_in_months(year,month)
print(days)