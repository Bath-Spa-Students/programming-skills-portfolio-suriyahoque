import math

def calculate_circle_area(radius):
    """Function to calculate the area of a circle."""
    return math.pi * radius**2

# Example usage
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is: {area:.2f}")