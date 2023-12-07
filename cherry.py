# This is a simple "Hello, World!" program in Python

def main():
    print("Hello, World!")

    # Checklist
    tasks = [
        ("Calculator", True),
        ("To-Do List Application", True),
        ("Guess the Number Game", True),
        ("Basic Web Scraper", True),
        ("Weather App", True),
        ("Currency Converter", True),
        ("Web Development with Flask", False),
        ("Hangman Game", False),
        ("Mini Blog", False),
        ("Chatbot", False),
    ]

    print("\nChecklist:")
    for i, (task, completed) in enumerate(tasks, start=1):
        status = "[X]" if completed else "[ ]"
        print(f"{i}. {status} {task}")

if __name__ == "__main__":
    main()
