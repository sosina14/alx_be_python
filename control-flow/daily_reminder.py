# daily_reminder.py

while True:
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use match case to handle different priority levels
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority entered."

    # Check if the task is time-sensitive
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Display the final reminder
    print("\nReminder:", reminder)

    # Ask if the user wants to add another task
    another_task = input("\nWould you like to add another task? (yes/no): ").lower()
    if another_task != "yes":
        print("Thank you! Have a productive day!")
        break

