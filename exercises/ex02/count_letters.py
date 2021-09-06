"""Counting letters in a string."""

__author__ = "730401999"


# Begin your solution here...
letter: str = input("What letter would you like to search for? ")
word: str = input("Enter a word: ")
length: int = len(word)
a: int = 0 
count: int = 0
while a < length:
    if (word[a]) == letter:
        count = count + 1 
    a = a + 1
print("Count: " + str(count))
