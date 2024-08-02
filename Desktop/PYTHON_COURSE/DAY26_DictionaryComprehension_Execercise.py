sentence="What is the Airspeed Velocity of an Unladen Swallow?"
word_list=sentence.split()

word_in_sentence={word:len(word) for word in word_list}
print(word_in_sentence)


#use dictionary comprehension called weather_f that takes each temprature in degree Celsius
#and convert it into farhenhit degrees
weather_c={"Monday":12,
            "Tuesday":14,
            "Wednesday":15,
            "Thursday":14,
            "Friday":21,
            "Saturday":22,
            "Sunday":24}

weather_f={day:round((temp_c*(9/5))+32,2) for (day,temp_c) in weather_c.items()}
print(weather_f)