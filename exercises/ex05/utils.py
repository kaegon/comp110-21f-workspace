"""List utility functions part 2."""

__author__ = "73040199"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    """A function to record the even ints in a list."""
    i = 0
    y: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
        i += 1
    return y

  
def sub(x: list[int], a: int, b: int) -> list[int]:
    """A function to create a sublist of chosen indexes of a given list."""
    y: list[int] = []
    if len(x) == 0:
        return y
    if a < 0:
        a = 0
    if b > len(x):
        b = len(x)
    while a < b:
        y.append(x[a])
        a += 1
    return y


def concat(a: list[int], b: list[int]) -> list[int]:
    """A function to combine two given lists."""
    c: list[int] = []
    i = 0 
    while i < len(a):
        c.append(a[i])
        i += 1
    j = 0
    while j < len(b):
        c.append(b[j])
        j += 1
    return c
