# A function that performs basic arithmetic operations
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num1 == 0 or num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
