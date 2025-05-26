# This calculator will prompt the user to enter two numbers and 
# select an operation (addition, subtraction, multiplication, or division).
# The script will then perform the selected operation using
#   a Match Case statement and display the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {num1 + num2}. ")
    case "-":
        print(f"The result is {num1 - num2}. ")
    case "*":
        print(f"The result is {num1 * num2}. ")
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}. ")
