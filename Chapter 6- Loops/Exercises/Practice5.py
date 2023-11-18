# Initialize a variable to store the largest number
largest_number = float('-inf')  # Start with negative infinity to handle negative numbers

# Use a while loop to get user input until '0' is entered
while True:
    user_input = input("Enter a number (enter '0' to exit): ")

    # Check if the input is '0' to exit the loop
    if user_input == '0':
        break

    # Convert the input to a float
    number = float(user_input)

    # Update the largest number if the current input is greater
    if number > largest_number:
        largest_number = number

# Print the largest number after exiting the loop
print("The largest number entered is:", largest_number)