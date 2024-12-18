task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority.lower():
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"               
    case _:          
        priority_message = "unknown priority"                                       
        print("Invalid priority input!")
if time_bound.lower() == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."
print(f"Reminder: '{task}' is a {priority_message} task {time_message}")
