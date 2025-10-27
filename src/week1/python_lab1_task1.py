"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2

if __name__ == "__main__":
    radius = float(input("Radius is: "))
    area = circle_area(radius)
    print (f"The area is: {area:.2f}")