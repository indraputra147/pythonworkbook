#Exercise 51: Letter Grade to Grade Points

"""
The program begins by reading a letter from the user
then compute and display the equivalent number of grade points
"""

GRADE = input("Enter the letter of your grade (from A to F): ")

if GRADE == "A"  or GRADE == "A+":
    print("Your grade points is 4.0")
elif GRADE == "A-":
    print("Your grade points is 3.7")
elif GRADE == "B+":
    print("Your grade points is 3.3")
elif GRADE == "B":
    print("Your grade pointas it 3.0")
elif GRADE == "B-":
    print("Your grade points is 2.7")
elif GRADE == "C+":
    print("Your grade points is 2.3")
elif GRADE == "C":
    print("Your grade points is 2.0")
elif GRADE == "C-":
    print("Your grade points is 1.7")
elif GRADE == "D+":
    print("Your grade points is 1.3")
elif GRADE == "D":
    print("Your grade points is 1.0")
elif GRADE == "F":
    print("Your grade points is 0")
else:
    print("Invalid letter grade!")
