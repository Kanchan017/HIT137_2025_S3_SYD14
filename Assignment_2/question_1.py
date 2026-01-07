#question1

# Asks for user inputs
shift_1 = int(input("Enter Shift1:"))
shift_2 = int(input("Enter Shift2:")) 

# Open the original file and read it.
f = open("raw_text.txt")
rw_txt = f.read()
f.close() # close the file after reading