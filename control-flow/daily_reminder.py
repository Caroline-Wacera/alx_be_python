task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
<<<<<<< HEAD
time_bound = input("Is it time-bound?(yes/no): ").lower()
match priority:
    case "high":
        priority_msg = "high priority task"
    case "medium":
        priority_msg = "medium priority task"
    case "low":
        priority_msg = "low priority task"
    case _:
        priority_msg = "task with unknown priority"

if time_bound == "yes":
    reminder_msg = f"Reminder: '{task}' is a {priority_msg} that requires immediate attention today!"
elif time_bound == "no":
    reminder_msg = f"Reminder: '{task}' is a {priority_msg}. Consider completing it when you have free time."

=======
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
        case "high":
            priority_msg = "high priority task"
        case "medium":
            priority_msg = "medium priority task"
        case "low":
            priority_msg = "low priority task"
        case _:
            priority_msg = "task with unknown priority"
if time_bound == "yes":
        reminder_msg = f"Reminder: '{task}' is a {priority_msg} that requires immediate attention today!"
elif time_bound == "no":
        reminder_msg = f"Reminder: '{task}' is a {priority_msg}. Consider completing it when you have free time."
>>>>>>> 61ae01629f45a572283fcb300aba0f48731e7a02
print(reminder_msg)
