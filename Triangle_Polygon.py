!pip install ColabTurtle
from ColabTurtle.Turtle import *
initializeTurtle()
home()
clear()

## triangle ##
def polygon(nsides):
    angle = 360/nsides
    left(90)
    for i in range(nsides):
        fd(100)
        right(angle)
        
def triangle(nsides):
    right(30)
    fd(100)
    right(120)
    fd(100)
    right(120)
    fd(100)

nsides = input("Enter number of sides: ")
nsides = int(nsides)

if nsides == 3:
    triangle(nsides)
elif nsides > 3:
    polygon(nsides)
else:
    print("Invalid input")
