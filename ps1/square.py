#This program creates an estimate for customers if they have a square room.

#This gathers the user input 
name = input("What is the name of the customer ")

address= input("What is the address of the custoemr ")

s1 = int(input("What is the size of 1 side of the room in feet "))

#calc the area of the house that is a square. 
area = s1 * s1 

#calculates the total cost 
floor = area * 2
install = area * 1.5 
total = floor + install

#Output
print("Estimate for", name)
print(address)
print("\n")
print("Square room with area of " , area, "square feet")
print("Estimated cost of flooring is" , floor)
print( "Estimated cost for installation" , install)
print("Total estimate is " , total)