"""An exercise in remainders and boolean logic."""

__author__ = "730401999"


# Begin your solution here...

divisor: int = int(input("Enter an int: "))

if divisor % 2 == 0 and divisor % 7 == 0:
    print("TAR HEELS")
if divisor % 2 == 0 or divisor % 7 == 0: 
    if divisor % 2 == 0:
        print("TAR")
    if divisor % 7 == 0: 
        print("HEELS")
else:
    print("CAROLINA")
