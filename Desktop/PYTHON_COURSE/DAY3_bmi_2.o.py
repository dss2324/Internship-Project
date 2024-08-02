weight=input("Enter Your Weight : ");
height=input("Enter Your Height in metres :");
bmi=int(weight)/float(height)**2;
if(bmi<18.5):
    print(f"you are underweight your BMI is {int(bmi)}");
elif(bmi>=18.5 and bmi<25):
    print(f"you are normal your BMI is {int(bmi)}");    
elif(bmi>=25 and bmi<30):
    print(f"you are overweight your BMI is {int(bmi)}");    
elif(bmi>=30 and bmi<35):
    print(f"you are obese your BMI is {int(bmi)}"); 
else:
    print(f"you are clinically obese your BMI is {int(bmi)}");       