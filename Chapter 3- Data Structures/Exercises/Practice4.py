# Assume numbers1 has 100 elements
numbers1 = [i for i in range(1, 101)]  # Just an example, you can replace it with your actual list

# Initialize an empty list numbers2
numbers2 = []

# Copy the values from numbers1 to numbers2 using slicing
numbers2 = numbers1[:]

# Print the first few elements of numbers2 to verify the copy
print("First few elements of numbers2:", numbers2[:5])