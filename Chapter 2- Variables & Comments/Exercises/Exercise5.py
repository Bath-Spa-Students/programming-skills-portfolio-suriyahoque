# Exercise 5: USB Shopper :ballot_box_with_check:

# Define the cost of one USB stick and the girl's budget
usb_stick_cost = 6  # cost of one USB stick in pounds
budget = 50  # total budget in pounds

# Calculate how many USB sticks she can buy
num_usb_sticks = budget // usb_stick_cost

# Calculate how much money she will have left
money_left = budget % usb_stick_cost

# Display the results
print(f"The girl can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{money_left} left.")