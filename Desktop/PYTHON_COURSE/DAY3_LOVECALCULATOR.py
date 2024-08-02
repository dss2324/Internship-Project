print("WELCOME TO LOVE CALCULATOR ")
name1=input("What is your name\n");
name2=input("What is their name\n");
t_occurence=name1.count('t')+name2.count('t')+name1.count('T')+name2.count('T'); #T
r_occurence=name1.count('r')+name2.count('r')+name1.count('R')+name2.count('R');#R
u_occurence=name1.count('u')+name2.count('u')+name1.count('U')+name2.count('U');#U
e_true=name1.count('e')+name2.count('e')+name1.count('E')+name2.count('E');#E

l_occurence=name1.count('l')+name2.count('l')+name1.count('L')+name2.count('L');#L
o_occurence=name1.count('o')+name2.count('o')+name1.count('T')+name2.count('O');#O
v_occurence=name1.count('v')+name2.count('v')+name1.count('V')+name2.count('V');#V
e_love=name1.count('e')+name2.count('e')+name1.count('E')+name2.count('E');#E


firstdigit=str(t_occurence+r_occurence+u_occurence+e_love)
seconddigit=str(l_occurence+o_occurence+v_occurence+e_love);
print("YOU HAVE "+firstdigit+seconddigit+"% LOVE IN RELATIONSHIP")