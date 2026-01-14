# Assignment2 Q3:Using a recursive function to generate a geometric pattern using Python's turtle graphics
import turtle as t
t.speed(0)
#Defining recursive function to draw 
def drawGeometry(leng,depth):
    #Case: if depth =0 draw a straight line
    if depth == 0:
        t.forward(leng)
    else:
        lenOftheSegment = leng / 3 #DIVIDING INTO 3
        
        #draws the first segment
        drawGeometry(lenOftheSegment, depth - 1)        
        # turn& draw the indent
        t.left(60)
        drawGeometry(lenOftheSegment, depth - 1)        
        t.right(120)
        drawGeometry(lenOftheSegment, depth - 1)        
        t.left(60)
        drawGeometry(lenOftheSegment, depth - 1)
   
s = int(input("Please enter the number of sides: "))
s_length = int(input("Pleae enter the side length: "))
depth = int(input("Please enter the recursion depth: "))

angle = 360/s
for i in range(s):
    drawGeometry(s_length,depth)
    t.left(angle)   
t.done()