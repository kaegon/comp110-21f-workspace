"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()
# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for the existence of a key 
if "Duke" in schools:
    print("'Duke' is presemt")
else:
    print("'Duke' is NOT presemt")

# Update / reassign a key-value pair

schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)


schools = {} 
print(schools)

schools = {
    "UNC": 19400,
    "Dukie": 6717,
    "NCSU": 26150
}
print(schools)


for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

