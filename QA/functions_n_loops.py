
# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.

# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, 
# and output their name and final ICT grade as a percentage.

# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.

# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)


name = input("What is your name? ")

def ICT_grade(mark1, mark2, mark3):
    assessscore = ((mark1 + mark2 + mark3)/175)*100
    return assessscore

hm = int(input("Enter homework score: ")) 
while hm<0 or hm>25:
    hm = int(input("Re-enter homework score between 0 and 25: "))

cs = int(input("Enter assessment score: "))
while cs<0 or cs>50:
    cs = int(input("Re-enter assessment score between 0 and 50: "))


fs = int(input("Enter final exam score: "))
while fs<0 or fs>100:
    fs = int(input("Re-enter final exam score between 0 and 100: "))
 

percentscore = ICT_grade(hm, cs, fs)
if percentscore > 80:
    grade = "A"
elif 60 < percentscore <= 80:
    grade = "B"
elif 40 < percentscore <= 60:
    grade = "C"
else:
    grade = "F"
print(name, "your total score of", round(percentscore,2), "is a grade:", grade)

