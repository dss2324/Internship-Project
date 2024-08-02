print("WELCOME TO TIP CALCULATOR ");
bill=float(input("What was the total bill ? $ : "));
tip=int(input("How Much Tip would you like to give? 10,12,15 ? : "));
people=int(input("How many people to split bill ? "));
total_tip_as_percent=tip/100;
total_tip_amount=bill*total_tip_as_percent;
total_bill=bill+total_tip_amount;
bill_per_person=total_bill/people;
#final_amount="{:2f}".format(bill_per_person)->this syntax round precisely to 0 if 33.6 it will display 33.60
final_amount=round(bill_per_person,2);
print(f"Each person have to pay ${final_amount}  ");