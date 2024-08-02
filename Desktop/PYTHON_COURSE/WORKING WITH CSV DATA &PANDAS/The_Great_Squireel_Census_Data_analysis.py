import pandas
#here data is dataframe
data =pandas.read_csv("WORKING WITH CSV DATA &PANDAS/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
#here rhs is a row that contains "Gray" as primary fur color
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict={"Fur Color":["Gray","Red","Black"],
            "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]                                   
            }

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")