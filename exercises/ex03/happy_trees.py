"""Drawing forests in a loop."""

__author__ = "730401999"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

Dep: int = int(input("Depth: "))
i: int = 1 

while i < (Dep + 1):
    print(i * TREE)
    i += 1
