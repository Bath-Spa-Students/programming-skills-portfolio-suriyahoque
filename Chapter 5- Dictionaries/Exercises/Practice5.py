# Two dictionaries to merge
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge the dictionaries using update()
merged_dict = dict1.copy()  # Create a copy of dict1 to avoid modifying it directly
merged_dict.update(dict2)

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)