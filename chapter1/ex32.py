#Exercise 32: Sum of the Digits in an Integer

"""
The program reads a 4 digit integer from the user
display the sum of its digit
"""

di = input("Input 4 digit of integer: ")

x1 = int(di[0])
x2 = int(di[1])
x3 = int(di[2])
x4 = int(di[3])
x5 = x1 + x2 + x3 + x4

summ = "{} + {} +  {} + {} = {} "
print(summ.format(x1, x2, x3 ,x4 ,x5))
