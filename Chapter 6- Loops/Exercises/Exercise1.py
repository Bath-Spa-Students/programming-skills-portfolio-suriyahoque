# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Prompt the user to enter pizza toppings
while True:
    topping = input("Enter a pizza topping (enter 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    # Add the topping to the list
    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Print the final list of pizza toppings
print("\nYour pizza toppings:")
for topping in pizza_toppings:
    print(topping)
