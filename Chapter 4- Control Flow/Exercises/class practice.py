Sales = float(input("Enter sales :"))
bonus = 100 
if Sales > 83999 : 
    bonus = 999
else: 
    bonus = 0
print("Your Bonus : "+str(bonus ) ) 

# Nested Desicion structure 
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.") 
number = float(input("Enter a number: "))

# if-elif-else statement 
number = float(input("Enter a number: "))
if number > 0:
    category = "Positive"
elif number < 0:
    category = "Negative"
else:
    category = "Zero"

print(f"The number is in the category: {category}")

