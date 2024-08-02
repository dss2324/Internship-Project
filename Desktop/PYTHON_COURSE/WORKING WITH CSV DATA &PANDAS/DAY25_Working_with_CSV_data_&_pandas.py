#Reading CSV Data in python
#CSV Means comma seprated value & it is way of representing tabular data

#with open("WORKING WITH CSV DATA &PANDAS\weather_data.csv") as datafile:
#    data=datafile.readlines()
    #print(data)
    
#we will use csv library for  the same thing but this time we will do less work
#import csv
#with open("WORKING WITH CSV DATA &PANDAS\weather_data.csv") as datafile:
#    data=csv.reader(datafile)
    #print(data)
    #challenge:-extract all temp from csv file in list tempratures in integer format
#    tempratures=[]
#    for row in data:
#        if row[1]!="temp":
#            tempratures.append(int(row[1]))
#    print(tempratures)            

#using pandas for data analysis more less work then csv
import pandas
data=pandas.read_csv("WORKING WITH CSV DATA &PANDAS\weather_data.csv")
#if you want to print only temp data,by specifying name of coulmn you can get hold of data
print(data["temp"])
#print(data)