alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#direction=input("Type 'encode' to encrypt,type 'decode to decrypt:\n")
#text=input("Type your message :\n").lower()
#shift=int(input("Type the shift number:\n"));
#todo1:-CREATE  a function called 'encrypt' that takes the 'text' and 'shift' as inputs
#todo2:-inside the encrypt function,shift each letter of the 'text' forwards in the alphabet by shift amount & print the encrypted text
#eg:-plain text="hello",shift=5,cipher_text="mjqqt",print output:"The encoded text is mjqqt"
#todo3:-call the encrypt function & pass in the user inputs
#here we had taken alphabets 2 times bc in some edge case like if we pass zulu in plain
#text and shiftamount 5 then it will throw index error but twice alphabets remove this problem
#& index() function only consider first case if matching elemnts are found in list
def encrypt(plaintext,shiftamount):
    cipher_text=""
    for i in plaintext:
        position=alphabet.index(i)
        new_position=position+shiftamount
        new_letter=alphabet[new_position]
        cipher_text += new_letter
    print(f"The Encoded Text is {cipher_text}")
    
#encrypt(plaintext=text,shiftamount=shift)