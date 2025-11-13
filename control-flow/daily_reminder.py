task = input("Enter your task for today: ")
priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is the task time-bound? (yes or no): ").lower()


match priority:
    case "high":
        reminder = f"Task '{task}' is a high priority task" 
        reminder = f"Task '{task}' is a medium priority task"
    case "low":
        reminder = f"Task '{task}' is a low priority task"
    case _:
        reminder = f"Task '{task}' has an undefined priority"


if time_bound == "yes":
    reminder += " that requires immediate attention today!"


print(reminder)

