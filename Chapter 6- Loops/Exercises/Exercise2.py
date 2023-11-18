# Use a loop to ask users their age and calculate the cost of their movie ticket
while True:
    age_input = input("Enter your age (type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'

    try:
        age = int(age_input)
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit'.")