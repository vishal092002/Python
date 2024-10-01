#This program creates an estimate for customers if they have a Rectangular  room.

#Gathers User Input 
name = input("What is the name of the customer ")
address = input("What is the address of the customer ")
length = int(input("What is the length of the room "))
width = int(input("What is the width of the room "))

#Calculates the area of a rectangle room 
area = length * width

#calcualtes the cost of install as well as flooring
floor = area * 2
install = area * 1.5
total = floor + install 

#prints the output
print("Estimate for", name)
print(address)
print("\n")
print("Rectangle room with area of " , area, "square feet")
print("Estimated cost of flooring is" , floor)
print( "Estimated cost for installation" , install)
print("Total estimate is " , total)