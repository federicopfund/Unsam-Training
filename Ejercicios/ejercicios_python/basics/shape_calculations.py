"""
Shape calculations module.

This module defines basic shape classes and their area calculations.
"""

import math


class Shape:
    """Abstract base class for shapes."""
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must implement area method")


class Rectangle(Shape):
    """Represents a rectangle with length and width."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Represents a circle with a given radius."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    rectangle = Rectangle(length=5, width=3)
    circle = Circle(radius=4)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())
