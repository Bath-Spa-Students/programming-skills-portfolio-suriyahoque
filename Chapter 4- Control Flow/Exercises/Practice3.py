# Assume amount1 and amount2 are given
amount1 = 15
amount2 = 80

# Nested decision structures
if amount1 > 10:
    if amount2 < 100:
        # Display the greater of amount1 and amount2
        if amount1 > amount2:
            print("Greater amount:", amount1)
        else:
            print("Greater amount:", amount2)
    else:
        print("amount2 is not less than 100.")
else:
    print("amount1 is not greater than 10.")
