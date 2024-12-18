task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
if priority.lower() == "high":
    priority_message = "high priority task"
elif priority.lower() == "medium":
    priority_message = "medium priority task"
elif priority.lower() == "low":
    priority_message = "low priority task"
else:
    priority_message = "unknown priority task"
if time_bound.lower() == "yes":
    reminder_message = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
else:
    reminder_message = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."
print(reminder_message)
