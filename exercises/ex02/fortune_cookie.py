"""Program that outputs one of at least four random, good fortunes."""
from random import randint

3
__author__ = "730401999" 

print("Your fortune cookie says...")
fortune: int = randint(1, 4)
if fortune == 1:
    print("You will get an A on your next exercise!!")
elif fortune == 2:
    print("You will become a hacker one day!!")
elif fortune == 3:
    print("You will live forever!")
elif fortune == 4:
    print("Someone loves you... <3")
print("Now, go spread positive vibes!")
