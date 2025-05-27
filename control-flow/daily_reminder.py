# This script will ask the user for a single task, its priority level,
#   and if it is time-sensitive. The program will then provide a customized
#   reminder for that task, demonstrating control flow and loops without
#   relying on data structures to store multiple tasks.

description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            start = "Reminder"
            end = " that requires immediate attention today!"
    case "medium" | "low":
        start = "Note"
        end = ". Consider completing it when you have free time."

print(f"{start}: '{description}' is a {priority} priority task{end}")
