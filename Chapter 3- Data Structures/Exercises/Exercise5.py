# Exercise 5: Change Guest List :

# Create a list of people to invite to dinner
guests = ["Sumaia", "Aisha", "Urooj"]

# Print invitations to each person
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us for a wonderful evening!")

# Print the name of the guest who can't make it
guest_cant_make_it = "Urooj"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new person
new_guest = "Salma"
guests[guests.index(guest_cant_make_it)] = new_guest

# Print a second set of invitation messages
print("Updated Invitations:")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner. Please join us for a wonderful evening!")
