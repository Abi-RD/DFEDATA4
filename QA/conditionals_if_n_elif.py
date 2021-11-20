        # with elif

# Write a program that determines the name of a shape from its number of sides. 
# Read the number of sides from the user and then report the appropriate name as part of a meaningful message. 
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides. 
# If a number of sides outside of this range is entered then your program should display an appropriate error message.

nsides = int(input("Enter the number of side: "))
name = " "

if nsides == 3:
    name = "Triangle"
elif nsides == 4:
    name = "Quadilateral"
elif nsides == 5:
    name = "Pentagon"
elif nsides == 6:
    name = "Hexgon"
elif nsides == 7:
    name = "Heptagon"
elif nsides == 8:
    name = "Octagon"
elif nsides == 9:
    name = "Nonagon"
elif nsides == 10:
    name = "Decagon"
if name == " ":
    print("Sorry," ,"Number sides not supported by this programme")
else:
    print("That's a", name)


# mark = int(input("Enter you mark: "))
    
""" if 84 < mark <= 100:
    print("Distinction")
elif 65 <= mark < 85:
    print("Pass")
else:
    print("fail") """

            #BETTER STILL
""" if mark > 85:
    print("Distinction")
elif mark > 65 and mark < 85:
    print("Pass")
else:
    print("fail") """

            #without elif

# mark1 = int(input("Enter your marks: "))

""" if mark1 > 85:
    print("Distinction!")
else:
    if mark1 > 65 and mark1 < 85:
        print("Pass")
    else:
        print("Fail") """



