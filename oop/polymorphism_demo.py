import math
"""
Objective:
    Enhance your understanding of polymorphism in Python by
    creating a set of classes that demonstrate method
    overriding and polymorphic behavior.

Task Description:
    Create a Python script named polymorphism_demo.py. In this script:
    - Define a base class `Shape` with a method `area()`.
    - Create two derived classes: `Rectangle` and `Circle`, each overriding
        the `area()` method to compute their respective areas.
    - Demonstrate polymorphism by calling the `area()` method on different
        shape objects through a common interface.
"""


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return (math.pi * (self.radius ** 2))
