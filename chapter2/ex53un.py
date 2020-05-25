#Exercise 53: Grade Points to Letter Grade

"""
This program will convert a grade points into a letter
"""

GP = float(input("Enter your grade points: "))

if GP >= 4.0:
    print("A+")
elif GP == 3.7:
    print("A-")
elif GP == 3.3:
    print("B+")
elif GP == 3.0:
    print("B")
elif GP == 2.7:
    print("B-")
elif GP == 2.3:
    print("C+")
elif GP == 2.0:
    print("C")
elif GP == 1.7:
    print("C-")
elif GP == 1.3:
    print("D+")
elif GP == 1.0:
    print("D")
elif GP == 0:
    print("F")
else:
    print("wrong input!")
