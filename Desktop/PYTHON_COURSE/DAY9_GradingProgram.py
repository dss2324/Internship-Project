#you have database called student_score in form of dictionary
#the key is student_names & values are their exam scores
#wap that converts their score into grades
#by end of program you should have new dictionary called  student_grades
#that contain student name as key & grades as values
student_scores={
                 "Harry":81,
                 "Ron":78,
                "Hermione":99,
                 "Draco":74,
                  "Neville":62
                       }

student_grades={}

for key in student_scores:
    if student_scores[key]>=91 and student_scores[key]<=100:
        student_grades[key]="Outstanding"
    elif student_scores[key]>=81 and student_scores[key]<=90:
        student_grades[key]="Exceeds Exceptations"
    elif student_scores[key]>=71 and student_scores[key]<=80:
        student_grades[key]="Acceptable"
    elif student_scores[key]<=70:
        student_grades[key]="Fail"
        
        
print(student_grades)