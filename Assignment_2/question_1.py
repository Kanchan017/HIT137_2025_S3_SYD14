#question1

# Asks for user inputs
shift_1 = int(input("Enter Shift1:"))
shift_2 = int(input("Enter Shift2:")) 

# Open the original file and read it.
f = open("raw_text.txt")
rw_txt = f.read()
f.close() # close the file after reading

def encrypt(rw_txt, shift_1, shift_2):
    encrypted_text = ""  # empty string to hold encrypted text

    #to check the type of characters
    for char in rw_txt:
        #lowercase
        #first half of alphabet: (a-m)
        if char.islower():
            if char>='a' and char<='m':
                new_ord = ord(char) + (shift_1*shift_2)
                #Wrap around if past'z'
                if new_ord > ord('z'):
                    new_ord-=26

                encrypted_text += chr(new_ord)
        
        #second half of alphabet:(n-z)
            else:
                new_ord = ord(char)-(shift_1 + shift_2)
                #Wrap around if before 'a'
                if new_ord < ord('a'):
                    new_ord +=26
                #Convert back to character and append to result
                encrypted_text += chr(new_ord)
            
        #uppercase
        elif char.isupper():
        #for first half(A-M)
            if char >= 'A' and char <='M':
               new_ord = ord(char)- (shift_1)

              #Wrap around if before 'A'
               if new_ord < ord('A'):
                  new_ord += 26
            
               encrypted_text += chr(new_ord)
            
            else:
                new_ord = ord(char) + ((shift_2**2))

                if new_ord >ord('Z'):
                    new_ord -=26

                encrypted_text += chr(new_ord) 

        #for other characters
        else:
            encrypted_text += char

    return encrypted_text
    
# Call function and write to file
encrypted_text = encrypt(rw_txt, shift_1, shift_2)

with open("encrypted_text.txt", "w") as f:
    f.write(encrypted_text)

    
