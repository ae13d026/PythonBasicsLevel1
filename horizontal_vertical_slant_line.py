!pip install ColabTurtle 
from ColabTurtle.Turtle import*
initializeTurtle()
print("1) sleeping/horizontal line")
print("2) standing/vertical line")
print("3) inclined/slant line")
option = input("Enter your option: ")
option = int(option)
if option == 1:
    home()
    clear()
    right(90)
    forward(100)
elif option == 2:
    home()
    clear()
    forward(100)
elif option == 3:
    home()
    clear()
    right(45)
    forward(100)
else:
    print("Invalid option")
