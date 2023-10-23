# Exercise 3: Stripping Names :ballot_box_with_check:

# Define a person's name with whitespace characters
name = "\t   Suriya Hoque \n"

# Print the name with leading and trailing whitespace
print("Name with Whitespace:")
print(name)

# Print the name after stripping leading and trailing whitespace
print("Name using lstrip():")
print(name.lstrip())

print("Name using rstrip():")
print(name.rstrip())

print("Name using strip():")
print(name.strip())