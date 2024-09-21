# daily_reminder.py

while True:
    # Prompt user for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate inputs and use match case for priority
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority entered. Please enter 'high', 'medium', or 'low'.")
        continue  # Restart the loop if the priority is invalid

    match priority:
        case "high":
            reminder = f"'{task}' is a high-priority task"
        case "medium":
            reminder = f"'{task}' is a medium-priority task"
        case "low":
            reminder = f"'{task}' is a low-priority task"

    # Check if the task is time-sensitive
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
        continue  # Restart the loop if the time-bound input is invalid

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Display the customized reminder
    print("\nReminder:", reminder)

    # Ask if the user wants to add another task
    another_task = input("\nWould you like to add another task? (yes/no): ").strip().lower()
    if another_task != "yes":
        print("Thank you! Have a productive day!")
        break
