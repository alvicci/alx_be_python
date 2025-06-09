def safe_divide(numerator, denominator):
    """
    Safely performs division between two values after converting them to floats.
    
    Handles common exceptions such as division by zero and non-numeric input.
    
    Args:
        numerator: The value to be divided (can be int, float, or string).
        denominator: The value to divide by (can be int, float, or string).
    
    Returns:
        str: A message with the division result or an appropriate error message.
    """
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
