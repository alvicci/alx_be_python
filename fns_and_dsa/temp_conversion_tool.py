# This script will define functions to convert temperatures
#   between Celsius and Fahrenheit, demonstrating the use of
#   global variables to store conversion factors that are
#   accessible within functions.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temperature = float(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if degree == 'f':
    temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {temp}°C")
elif degree == 'c':
    temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {temp}°F")
else:
    print("Enter a valid degree conversion")
