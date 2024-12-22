task=input("Enter your task: ")
time_bound=input("Is it time-bound? (Yes/No): ").lower()
priority= input("Priority (high/medium/low): ").lower()
match priority:
    case "high":
        if time_bound=="yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound=="no":
            print(f"{task} is a high priority task but you can do it when you have free time")