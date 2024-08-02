alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#direction=input("Type 'encode' to encrypt,type 'decode to decrypt:\n")
#text=input("Type your message :\n").lower()
#shift=int(input("Type the shift number:\n"));
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""




print(logo);

should_end=False
choice="yes"
while not should_end:
  
     
    direction=input("Type 'encode' to encrypt,type 'decode to decrypt:\n")
    text=input("Type your message :\n").lower()
    shift=int(input("Type the shift number:\n"));
 
    if direction=="encode":
     from DAY8_Caser_Cipher_Project_Part1_Encryption import encrypt
     encrypt(plaintext=text,shiftamount=shift)
   
    
    elif direction=='decode':
        from DAY8_Caser_Cipher_Project_Part2_Decryption  import decrypt
        decrypt(cipher_text_input=text,shiftamount_input=shift)
        
    choice=input("do you want to continue yes/no ?:")
    if choice=="no":
      should_end=True