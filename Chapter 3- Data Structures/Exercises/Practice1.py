# Given list
list1 = [5, 20, 15, 20, 25, 50, 20]

# Remove all occurrences of item 20 using list comprehension
list_without_20 = [item for item in list1 if item != 20]

# Print the updated list
print("Original List:", list1)
print("List without 20:", list_without_20)