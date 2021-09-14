"""Finding duplicate letters in a word."""

__author__ = "730401999"

word: str = input("Enter a word: ")

i: int = 0
dup: int = 0 

while i < len(word):
    j = i + 1 
    while j < len(word):
        if word[i] == word[j]:
            dup = dup + 1
        j = j + 1
    i = i + 1          

if dup > 0:
    print("Found duplicate: True")
else: 
    print("Found duplicate: False")          