#for loop
a=['delhi','mumbai','kolkata','bangalore','chennai']
for city in a:
    print(city)
s=[2,3,4,5]
for i in s:
    if(i%2!=0):
     print(i,'not divisible by 2')    
#while loop
i=1
while i<=5:
    print(i)
    i=i+1
#break statement
for i in range(1,10):
    print(i)
    if i==5:
        break
#continue statement
for i in range(1,10):
    if i==5:
        continue
    print(i)        