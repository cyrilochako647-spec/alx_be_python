
task = input("Enter your task for today: ")

priority = input("Enter the task priority (high, medium, low): ").lower()


time_bound = input("Is the task time-bound? (yes or no): ").lower()


match priority:
    case "high":
        reminder = f"Task '{task}' is high priority"
    case "medium":
        reminder = f"Task '{task}' is medium priority"
    case "low":
        reminder = f"Task '{task}' is low priority"
    case _:
        reminder = f"Task '{task}' has an undefined priority"


if time_bound == "yes":
    reminder += " that requires immediate attention today!"


print(reminder)
