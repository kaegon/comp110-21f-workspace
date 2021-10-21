"""List utility functions."""

__author__ = "730401999"


# TODO: Implement your functions here.

def all(a: list[int], b: int) -> bool:
    """A function that checks if all the ints in a list are the same as a specified integer."""
    i = 0
    x = 0
    if len(a) < 1:
        return False
    while i < len(a):
        if b == a[i]:
            x += 1
            i += 1
        else:
            return False
    answer_1: bool = x == (len(a))
    return answer_1
    

def is_equal(a: list[int], b: list[int]) -> bool:
    "Determines if two lists of ints are the same."
    if len(a) != len(b):
        return False
    i = 0
    x = 0
    while i < len(a) and len(b):
        if a[i] == b[i]:
            x += 1
            i += 1
        else:
            return False
    answer_2: bool = x == len(a) and x == len(b)
    return answer_2

    
def max(input: list[int]) -> int:
    """max of list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    i = 0 
    j = i + 1
    while i and j < len(input):
        for j in input:
            if input[i] > j: 
                input.pop(j)
            j += 1
        i += 1 
    return input[0]

                
            
        
    
            

