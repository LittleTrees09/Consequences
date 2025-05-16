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

def main():
    index = generate_random_number()
    print(f"Exercise number generated: {index + 1}")
    file_path = "consequences.txt"

    print("\nYour consequence is:")
    print(read_file(file_path, index))

    # NOTE: create code that automatically inputs consequence and date to a file (logbook)
    print(f"Consequences given on: {dt.datetime.today():%B %d, %Y @ %H:%M}")
    pass





def generate_random_number():
    """Generate a random number."""
    with open(r"consequences.txt", 'r') as file:
        lines = file.readlines()
        upper_bound = len(lines)
    return rd.randint(0, upper_bound - 1)

def read_file(file_path, index):
    """Read the file and return its content."""
    file_path = open(file_path, 'r')
    content = file_path.readlines()

    
    return content[index]

    # Uncomment to read all lines in the file.    
    # with open(file_path, 'r') as file:
    #     for line in file:
    #         print(line, end='')

def write_file(file_path):
    
    pass

if __name__ == "__main__":
    intro()
    main()
