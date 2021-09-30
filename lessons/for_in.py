"""An example of for in syntax."""

names: list[str] = ["Kris", "Kaegon", "Chris", "Austin"]

# Example of interating through names using a while loop
print("While output:")
i: int = 0 
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for..in loop is the same as the while loop
print("for..in output:")
for name in names:
    print(name)
