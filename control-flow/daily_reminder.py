task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")
        exit()

if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
elif time_bound == 'no':
    reminder += ". Consider completing it when you have free time."
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    exit()


print("Reminder:", reminder)
