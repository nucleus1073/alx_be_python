import math

class Shape:
    def area(self):
        """
        Base method for calculating area. Must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initializes a Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of a rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes a Circle with radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of a circle.
        """
        return math.pi * (self.radius ** 2)

def main():
    # Create a list of shapes
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrate polymorphism by calling the area method on each shape
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()