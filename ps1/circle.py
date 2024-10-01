#This program creates an estimate for customers if they have a Rectangular  room.

#Gathers User Input 
name = input(" What is the name of the customer ")
address = input("What is the address of the customer ")
radius = int(input("What is the radius of the room in feet"))

area = 3.14(radius **2)

#calcualtes the cost of install as well as flooring
floor = area * 2
install = area * 1.5
total = floor + install 

#prints the output
print("Estimate for", name)
print(address)
print("\n")
print("Circle room with area of " , area, "square feet")
print("Estimated cost of flooring is" , floor)
print( "Estimated cost for installation" , install)
print("Total estimate is " , total)