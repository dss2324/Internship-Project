row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
map=[row1,row2,row3];
print(f"{row1}\n{row2}\n{row3}")
print("Whre Do you want to put treausre ? ")
positionROW=int(input('enter row no : '));
positionCOL=int(input('enter coulmn : '));
map[positionROW-1][positionCOL-1]='X';
print(f"{row1}\n{row2}\n{row3}")
#print(map);