#file=open("DAY24_MY_FILE.txt")
#opening file with "with" keyword
# benefit of opening file with "with" is we no longer need to worry about closing it it automattically closes
with open("DAY24_MY_FILE.txt",mode='+a') as file: #here file is variable name
    #contents=file.read()
    file.write("\nthis is a file")
    
    