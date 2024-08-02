import pandas
data=pandas.read_csv("WORKING WITH CSV DATA &PANDAS\weather_data.csv")
# A pandas DataFrame is a 2D data structre like 2D array or a table with rows and coulmns
# A series in pandas is somewhat like list it means one single coulmn of table

#we can convert our dataframe to sql,json,excel, and so many other formats
#eg:-here we are converting our dataframe(table) into dictionary
#data_to_dict=data.to_dict()
#print(type(data))
#print(type(data_to_dict))
#printing dictionary that is data_to_dict
#print(data_to_dict)

#here data["temp"] is series
#temp_list=data["temp"].to_list()
#challenge calculate average temprature
#sum=0
#avg=0
#for i in temp_list:
#    sum=sum+i
    
#avg=round(sum/len(temp_list),2)
#print(f"average temprature is {avg}")    

#series equivalent of above method to calculate avg
#print(data["temp"].mean())
#finding maximum temprature from data series data["temp"]
#print(data["temp"].max())
#alternative to square brackets here it is treated as object
#print(data["day"])
#print(data.day)

#getting data in row
#when we put condition and filt the coulmn we got hold of row
#here we got hold of dataframe in dataframe we get data series and check if it equals to monday
#then we are printing ow in which data series data["day"] is monday
#print(data[data["day"]=="Monday"])

#challenge:-getting row in which temprature is max
#print(data[data["temp"]==data["temp"].max()])

#getting single data from row
#monday=data[data.day=="Monday"]
#print(monday.condition)

#challenge:-convert monday's temprature to fahrenhit. hint use[] to get a
#single value from the pandas Series by index
#monday_temp_c=monday.temp[0]
#monday_temp_f=((9/5)*monday_temp_c)+32
#print(monday_temp_f)

#create a dataframe from scratch
data_dict={
            "students":["Amy","James","Angela"],
            "scores":[76,56,65]
                }

data=pandas.DataFrame(data_dict) #here DataFrame is  class of pandas that take some data & convert it into tabular format
print(data)
data.to_csv("new_data.csv")