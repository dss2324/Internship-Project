#new_dict={new_key:new_value for item in list}
#creating new dictionary based on values of existing dictionary
#new_dict={new_key:new_value for (key,value) in dict.items() if test}
import random
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
#creating student scores using dictionary comprehension
student_scores={students:random.randint(23,100) for students in names}
print(student_scores)

#creating passed_students dictionary using existing student dictionay
passed_students={students:score for (students,score) in student_scores.items() if score>50}
print(passed_students)