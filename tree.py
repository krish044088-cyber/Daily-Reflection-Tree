def daily_reflection():
    print("Daily Reflection System\n")

    goal = input("Did you complete your main goal today? (yes/no): ").strip().lower()

    if goal in ["yes", "y"]:
        try:
            hours = int(input("How many hours did you work? ").strip())

            if hours >= 5:
                print("Result: Highly Productive Day")
            else:
                print("Result: Moderately Productive Day")

        except ValueError:
            print("Invalid input: Please enter numeric hours")

    elif goal in ["no", "n"]:
        reason = input("Why not? ").strip().lower()

        if "distraction" in reason:
            print("Result: Improve Focus")
        elif "energy" in reason:
            print("Result: Fix Sleep Routine")
        elif "plan" in reason:
            print("Result: Plan Tomorrow Better")
        else:
            print("Result: Reflect and improve tomorrow")

    else:
        print("Invalid input")

daily_reflection()