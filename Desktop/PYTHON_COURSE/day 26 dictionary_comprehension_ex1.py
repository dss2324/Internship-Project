# str=input("enter a string: ")
# wordlist=str.split()
# result={word:len(word) for word in wordlist}
# print(result)
#(temp_c*9/5)+32=temp_f
weather_c=eval(input("enter the day with its temperature in celcius: "))
weather_f={day:temp * 9/5+32 for (day,temp) in weather_c.items()}
print(weather_f)
