def is_prime(number):
    """Function to check if a given number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function with different numbers
numbers_to_test = [7, 12, 23, 50, 97]

for num in numbers_to_test:
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
