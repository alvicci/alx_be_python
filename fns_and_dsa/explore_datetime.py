from datetime import datetime, timedelta

# Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    # YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

# Calculate a Future Date
def calculate_future_date():
    input_days = int(input("Enter the number of days to add to the current date: "))
    future_date = (datetime.now() + timedelta(days=input_days))
    print(future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()