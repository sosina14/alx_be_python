# daily_reminder.py

while True:
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Clean and normalize the input
    task = task.strip()
    priority = priority.strip().lower()
    time_bound = time_bound.strip().lower()

    # Validate priority input using match case
    match priority:
        case "high":
            reminder = f"'{task}' is a high-priority task"
        case "medium":
            reminder = f"'{task}' is a medium-priority task"
        case "low":
            reminder = f"'{task}' is a low-priority task"
        case _:
            print("Invalid priority entered. Please enter 'high', 'medium', or 'low'.")
            continue  # Restart the loop if the priority is invalid

    # Validate time-bound input
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
        continue  # Restart the loop if the time-bound input is invalid

    # Display the customized reminder
    print("\nReminder:", reminder)

    # Ask if the user wants to add another task
    another_task = input("\nWould you like to add another task? (yes/no): ")
    another_task = another_task.strip().lower()
    
    if another_task != "yes":
        print("Thank you! Have a productive day!")
        break
