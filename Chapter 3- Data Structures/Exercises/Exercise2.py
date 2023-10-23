# Exercise 2: Greetings :ballot_box_with_check:

# Create a list of friends' names
names = ["Sumaia", "Sadia", "Aisha", "Urooj", "Salma"]

# Print personalized messages to each person
message = "Hello, {}! I hope you're having a great day."

for name in names:
    personalized_message = message.format(name)
    print(personalized_message)
