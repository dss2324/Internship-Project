student_dict={"student":["angela","james","lily"],"score":[56,76,98]}
for (key,value) in student_dict.items():
    print(value)
import pandas
student_data_frame=pandas.DataFrame(student_dict)
# loop through dataframes
# for (key,value) in student_data_frame.items():
#     print(value)
#loop through rows of a datab frame
for (index,row) in student_data_frame.iterrows():
    print(index)