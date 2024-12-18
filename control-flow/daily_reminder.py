task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority.lower():
        case "high":
            priority_message = "high priority task"
        case "medium":
            priority_message = "medium priority task"
        case "low":
            priority_message = "low priority task"
        case _:
            priority_message = "unknown priority task"
if time_bound.lower() == "yes":
        reminder_message = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
else:
        reminder_message = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."
print(reminder_message) 
