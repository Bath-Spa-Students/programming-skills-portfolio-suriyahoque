def factorial(n):
    """Recursive function to calculate the factorial of a positive integer."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")