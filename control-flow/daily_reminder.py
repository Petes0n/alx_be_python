task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        reminder = f"The task '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"The task '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"The task '{task}' is a LOW priority task."
    case _:
        reminder = f"The task '{task}' has an unknown priority."

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(f"Reminder: {reminder}")
