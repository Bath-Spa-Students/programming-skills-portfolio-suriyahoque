# Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

# Find and replace the first occurrence of value 20 with 200
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break  # Break the loop after the first occurrence is replaced

# Print the updated list
print("Updated List:", list1)