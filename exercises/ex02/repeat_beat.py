"""Repeating a beat in a loop."""

__author__ = "730401999"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
a: int = int(input("How many times do you want to repeat it? "))
i = 1 
if a > 0:
    b = beat 
    while i < a:
        i = i + 1
        b = beat + " " + b
    else:
        print(b)
else:
    print("No beat...")