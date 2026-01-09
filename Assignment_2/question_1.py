#question1

# Asks for user inputs
shift_1 = int(input("Enter Shift1:"))
shift_2 = int(input("Enter Shift2:")) 

# Open the original file and read it.
with open("raw_text.txt", "r") as f:
    rw_txt = f.read()

def encrypt(rw_txt, shift_1, shift_2):
    encrypted_text = ""  # empty string to hold encrypted text

    #to check the type of characters
    for char in rw_txt:
        #lowercase
        #first half of alphabet: (a-m)
        if 'a' <= char<='m':
                shift = shift_1 * shift_2
                new_ord = chr((ord(char) - ord('a') + shift)%13 + ord('a') )           
                encrypted_text += new_ord
        
        #second half of alphabet:(n-z)
        elif 'n' <= char <= 'z':
                shift = shift_1 + shift_2
                new_ord = chr((ord(char) - ord('n') - shift)%13 + ord('n') )           
                encrypted_text += new_ord
            
        #uppercase
        elif  'A' <= char <='M':
               shift = shift_1
               new_ord = chr((ord(char) - ord('A') - shift)%13 + ord('A') )           
               encrypted_text += new_ord
            
        elif 'N' <= char <= 'Z':
                shift = shift_1 * shift_2
                new_ord = chr((ord(char) - ord('N') + shift)%13 + ord('N') )          
                encrypted_text += new_ord

        #for other characters
        else:
            encrypted_text += char

    return encrypted_text
    
# Call function and write to file
encrypted_text = encrypt(rw_txt, shift_1, shift_2)

with open("encrypted_text.txt", "w") as f:
    f.write(encrypted_text)