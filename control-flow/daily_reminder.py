task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority.lower():
    case "high":
        priority_message = "This is a high priority task."
    case "medium":
        priority_message = "This is a medium priority task."
    case "low":
        priority_message = "This is a low priority task."
    case _:
        priority_message = "Invalid priority level."
if time_bound.lower() == "yes":
        reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
else:
        reminder_message = f"Note: '{task}' is a {priority.lower()} priority task. Consider completing it when you have free time."
print(reminder_message)
