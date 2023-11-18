# Create a dictionary of three major rivers and the countries they run through
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

# Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country)