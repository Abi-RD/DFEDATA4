        # with elif
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

mark1 = int(input("Enter your marks: "))

if mark1 > 85:
    print("Distinction!")
else:
    if mark1 > 65 and mark1 < 85:
        print("Pass")
    else:
        print("Fail")




