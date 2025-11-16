task = input("Enter the task description: ")
priority = input("Enter the task priority (high/medium/low): ")
time_bound = input("Is the task time-bound? (yes/no): ")

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
    reminder += " It requires immediate attention today!"

print(reminder)
