"""
Objective:
    Solidify your understanding of class methods and static methods
    in Python by implementing examples of each in a class,
    demonstrating their usage and differences.

Task Description:
Create a Python script named class_static_methods_demo.py. In this script:
- Define a class `Calculator` that includes both a `@classmethod`
    and a `@staticmethod`.
- Use the class method for operations that require access to class-level data.
- Use the static method for general-purpose utility calculations that
    don’t depend on instance or class-specific data.

This task illustrates the differences between @classmethod and @staticmethod
    decorators, and when to use each in practical scenarios.
"""


class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return (a + b)

    @classmethod
    def multiply(cls, a, b):
        print(f"calculation_type: {cls.calculation_type}")
        return (a * b)
