def ai_agent():
    print("AI Reflection Assistant\n")

    mood = input("How was your day? (good/bad): ").strip().lower()

    if mood == "good":
        reason = input("What made it productive? ").strip()
        print(f"Great! Keep doing: {reason}")

    elif mood == "bad":
        problem = input("What went wrong? ").strip().lower()

        if "sleep" in problem:
            print("Suggestion: Improve your sleep cycle.")
        elif "phone" in problem or "distraction" in problem:
            print("Suggestion: Reduce distractions and set focus blocks.")
        elif "plan" in problem:
            print("Suggestion: Plan your tasks in advance.")
        else:
            print("Suggestion: Reflect and create a structured plan for tomorrow.")

    else:
        print("Invalid input")

ai_agent()
