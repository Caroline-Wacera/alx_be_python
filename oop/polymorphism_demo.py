import math

class Shape:
    """Base class for shapes."""
    def area(self):
        """Method to calculate area. Should be overridden by subclasses."""
        raise NotImplementedError("The area() method must be overridden in derived classes.")


class Rectangle(Shape):
    """Derived class for rectangles."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class for circles."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)