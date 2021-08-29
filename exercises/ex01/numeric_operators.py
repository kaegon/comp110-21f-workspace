"""A program to demonstrate how python computes numerical operators"""

__author__: str = "730401999"
left_side: str = input("Left-hand side: ")
right_side: str = input("Right-hand side: ")
x = int(left_side)
y = int(right_side)
print(left_side + " ** " + right_side + " is " + str(x ** y))
print(left_side + " / " + right_side + " is " + str(x / y))
print(left_side + " // " + right_side + " is " + str(x // y))
print(left_side + " % " + right_side + " is " + str(x % y))
