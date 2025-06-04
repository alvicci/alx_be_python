# Functions and Data Structures – Python

Welcome to the `fns_and_dsa` directory of the **alx_be_python** repository!  
This collection of Python scripts demonstrates core programming concepts like function definitions, importing modules, list management, and basic use of Python’s standard libraries like `datetime`.

## 📁 Directory: `fns_and_dsa`

### 0. Arithmetic Operations Function

📄 **File:** `arithmetic_operations.py`  
🔁 **Used by:** `main.py`

**Objective:** Create a reusable function that performs basic arithmetic operations.

**Function Signature:**

```python
def perform_operation(num1: float, num2: float, operation: str) -> float or str
```

**Features:**

- Handles addition, subtraction, multiplication, and division.
- Returns a custom message when attempting to divide by zero.
- Designed to be imported and tested via a provided `main.py` script.

```shell
alvicci@ubuntu:~/0x00$python3 .\main.py
Arithmetic Operations
Enter the first number: 5
Enter the second number: 6
Enter the operation (add, subtract, multiply, divide): add
Result: 11.0
```

### 1. Shopping List Manager

📄 **File:** `shopping_list_manager.py`

**Objective:** Use lists to build a text-based shopping list manager.

**Features:**

- Add, remove, and view items from the shopping list.
- Menu-based user interface using a loop.
- Handles invalid choices gracefully.

```shell
alvicci@ubuntu:~/0x00$ python3 shopping_list_manager.py
Shopping List Manager
1. Add Item
2. Remove Item
3. View List
4. Exit
Enter your choice: 1
Enter the item to add: Milk
Milk added to your list!
```

### 2. Explore datetime Module

📄 **File:** `explore_datetime.py`

**Objective:** Learn to use Python’s datetime module for date and time manipulation.

**Features:**

- `display_current_datetime()` prints the current timestamp.
- `calculate_future_date()` adds user-defined days to the current date.
- Uses `datetime.now()` and `timedelta`.

```shell
alvicci@ubuntu:~/0x00$ python3 explore_datetime.py
2025-06-04 21:18:07
Enter the number of days to add to the current date: 4
2025-06-08
```

### 3. Temperature Conversion Tool

📄 **File:** `temp_conversion_tool.py`

**Objective:** Convert temperatures between Celsius and Fahrenheit using global variables.

**Features:**

- Global conversion factors:
- `convert_to_fahrenheit(celsius)` and `convert_to_celsius(fahrenheit)` functions.
- Validates user input and handles invalid formats.

```shell
alvicci@ubuntu:~/0x00$ python3 temp_conversion_tool.py
Enter the temperature to convert: 100
Is this temperature in Celsius or Fahrenheit? (C/F): F
100.0°F is 37.77777777777778°C
```

```shell
alvicci@ubuntu:~/0x00$ python3 temp_conversion_tool.py
Enter the temperature to convert: 0
Is this temperature in Celsius or Fahrenheit? (C/F): C
0.0°C is 32.0°F
```

How to Run the Scripts
Make sure you’re in the correct directory:

```shell
cd alx_be_python/fns_and_dsa
```

Ensure you have Python 3 installed on your system. You can check this by running:

```shell
python3 --version
```

Then run the scripts like this:

```shell
python3 script_name.py
```

Happy coding and keep exploring Python! 🚀
