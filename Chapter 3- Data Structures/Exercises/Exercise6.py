# Exercise 6: Shrinking Guest List :

# Create a list of people to invite to dinner
guests = ["Sumaia", "Aisha", "Urooj", "Salma"]

# Print invitations to each person
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us for a wonderful evening!")

# Print a message saying you can only invite two people
print("\nI can only invite two people for dinner.\n")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner this time.")

# Print messages to the two people still on your list
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner!")

# Use del to remove the last two names from your list
del guests[0]
del guests[0]

# Print the list to make sure it's empty
print("\nList of guests:", guests)
