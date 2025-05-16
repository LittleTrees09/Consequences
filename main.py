import random as rd
import datetime as dt

CONSEQUENCE_FILE = "consequences.txt"
LOG_FILE = "logbook.txt"

def intro():
    print(
        "\nWelcome to the Consequences game!\n"
        "This is to punish you for:\n"
        "1. Eating \"meryenda\"\n"
        "2. Overeating during BREAKFAST, LUNCH, or DINNER\n"
        "3. Not doing / missing an action on your daily to-do list\n"
        "4. Getting annoyed and using unstable emotions to decide on things\n"
    )

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Get consequence")
        print("2. Edit consequence list")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            get_consequence()
        elif choice == "2":
            edit_consequences()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")

def get_consequence():
    try:
        with open(CONSEQUENCE_FILE, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        if not lines:
            print("No consequences available.")
            return

        index = rd.randint(0, len(lines) - 1)
        consequence = lines[index]
        timestamp = dt.datetime.now().strftime("%B %d, %Y @ %H:%M")

        print(f"\nYour consequence is:\n→ {consequence}")
        print(f"Assigned on: {timestamp}")

        with open(LOG_FILE, 'a') as log:
            log.write(f"{timestamp} - {consequence}\n")
    except FileNotFoundError:
        print(f"Error: '{CONSEQUENCE_FILE}' not found.")

def edit_consequences():
    print("\n--- Edit Consequences ---")
    print("1. View all")
    print("2. Add new")
    print("3. Delete by number")
    print("4. Go back")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        view_consequences()
    elif choice == "2":
        add_consequence()
    elif choice == "3":
        delete_consequence()
    elif choice == "4":
        return
    else:
        print("Invalid input.")

def view_consequences():
    try:
        with open(CONSEQUENCE_FILE, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        if not lines:
            print("No consequences found.")
        else:
            print("\nCurrent Consequences:")
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line}")
    except FileNotFoundError:
        print(f"Error: '{CONSEQUENCE_FILE}' not found.")

def add_consequence():
    new_consequence = input("Enter new consequence: ").strip()
    if new_consequence:
        with open(CONSEQUENCE_FILE, 'a') as file:
            file.write(new_consequence + '\n')
        print("Consequence added.")
    else:
        print("No consequence entered.")

def delete_consequence():
    try:
        with open(CONSEQUENCE_FILE, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        if not lines:
            print("No consequences to delete.")
            return

        print("\nCurrent Consequences:")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line}")

        try:
            num = int(input("Enter the number of the consequence to delete: "))
            if 1 <= num <= len(lines):
                deleted = lines.pop(num - 1)
                with open(CONSEQUENCE_FILE, 'w') as file:
                    for line in lines:
                        file.write(line + '\n')
                print(f"Deleted: {deleted}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
    except FileNotFoundError:
        print(f"Error: '{CONSEQUENCE_FILE}' not found.")

if __name__ == "__main__":
    intro()
    main_menu()