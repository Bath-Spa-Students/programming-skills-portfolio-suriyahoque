# Make dictionaries representing different pets
pet1 = {'kind': 'dog', 'owner': 'Suriya'}
pet2 = {'kind': 'cat', 'owner': 'Urooj'}
pet3 = {'kind': 'parrot', 'owner': 'Aisha'}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"\nKind of animal: {pet['kind'].title()}")
    print(f"Owner's name: {pet['owner'].title()}")

