# Using a recursive function to generate a geometric pattern using Python's turtle graphics

import turtle as t
import math
t.speed(0)
t.hideturtle()
#Defining recursive function
def draw_o(leng,depth):
    #Case: if depth =0 draw a straight line
    if depth == 0:
        t.forward(leng)
   
s = int(input("Please enter the number of sides: "))
s_length = int(input("Pleae enter the side length: "))
depth = int(input("Please enter the recursion depth: "))

angle = 360/s

for i in range(s):
    draw_o(s_length,0)#for depth 0
    t.left(angle)   
t.done()