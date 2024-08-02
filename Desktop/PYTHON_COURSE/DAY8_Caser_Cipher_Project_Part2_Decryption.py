#todo1:-CREATE  a function called 'decrypt' that takes the 'text' and 'shift' as inputs
#todo2:-inside the decrpyt function,shift each letter of the 'text' backwards in the alphabet by shift amount & print the decrypted text
#eg:-cipher_text="hello",shift=5,plain text="hello",print output:"The decoded text is hello"
#todo3:-call the decrypt function & pass in the user inputs
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#direction=input("Type 'encode' to encrypt,type 'decode to decrypt:\n")
#text=input("Type your message :\n").lower()
#shift=int(input("Type the shift number:\n"));

def decrypt(cipher_text_input,shiftamount_input):
    plaintext=""
    for i in cipher_text_input:
        position=alphabet.index(i);
        new_position=position-shiftamount_input;
        #new_letter=alphabet[new_position]
        plaintext += alphabet[new_position]
    print(f"The Decoded Text is {plaintext}")
    
#decrypt(cipher_text_input,shiftamount_input)