"""Practice with dictionaries."""

__author__ = "730401999"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """A funtion that reverses keys and values."""
    new_list: dict[str, str] = {}
    for x in xs:
        b: str = x
        a: str = xs[x]
        if a in new_list:
            raise KeyError("Duplicate keys found.")
        else:
            new_list[a] = b  
    return new_list


def favorite_color(xs: dict[str, str]) -> str: 
    """A function that gives the color that appears most often in a dictionary."""
    if len(xs) == 0:
        return "No Values Entered"
    result: dict[str, int] = {}
    for x in xs:
        if x in result: 
            result[x] += 1
        else:
            result[x] = 1
    new: dict[int, str] = {}
    for x in result:
        b = result[x]
        if b is max(result.values()):
            new[b] = x
    c = ""
    for x in new:
        c = new[x]
    return xs[c]
    

def count(xs: list[str]) -> dict[str, int]:
    """A funtion to count the number."""
    result: dict[str, int] = {}
    for x in xs:
        if x in result: 
            result[x] += 1
        else:
            result[x] = 1
    return result