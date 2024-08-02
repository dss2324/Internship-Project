#You are painting wall,here one paint can  cover 5 square metre of wall
#given a random height & width of wall how many can of paints you need to but
#formula :- no of cans=(wall_height x wall_width)/coverage per can
#round of the answer
import math
test_h=int(input("Height of wall : "))
test_w=int(input("Width of wall : "))
coverage_per_can=5
def print_calc(height,width):
    no_of_cans=(height*width)/coverage_per_can
    print(f"Total no of paint cans required are {math.ceil(no_of_cans)}")
#here ceil() is used instead of round() bc if u input 17x8=136/5=27.2 round() will 
#make 27 wheras ceil() will make 28   
print_calc(height=test_h,width=test_w)