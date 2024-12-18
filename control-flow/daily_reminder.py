def colorize_message(priority: str, message: str) -> str:
    if priority == "high":
        return f"\033[91m{message}\033[0m"  # Red for high priority
    elif priority == "medium":
        return f"\033[93m{message}\033[0m"  # Yellow for medium priority
    elif priority == "low":
        return f"\033[92m{message}\033[0m"
    else:
        return message
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        priority_msg = "high priority task"
        urgency_msg = "This needs your immediate attention!"
    case "medium":
        priority_msg = "medium priority task"
        urgency_msg = "Try to tackle it as soon as possible."
    case "low":
        priority_msg = "low priority task"
        urgency_msg = "You can do this when you have free time."
    case _:
        priority_msg = "task with unknown priority"
        urgency_msg = "Priority unknown. Please review."
if time_bound == "yes":
    reminder_msg = f"Reminder: '{task}' is a {priority_msg} that requires immediate attention today!"
else:
    reminder_msg = f"Note: '{task}' is a {priority_msg}. Consider completing it when you have free time."
reminder_msg += f" {urgency_msg}"
final_message = colorize_message(priority, reminder_msg)
print(final_message)
