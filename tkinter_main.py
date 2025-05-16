import tkinter as tk
from tkinter import *

import random as rd
import datetime as dt

def main():
    intro()
    index = generate_random_number()
    print(f"Exercise number generated: {index + 1}")
    file_path = "consequences.txt"

    print("\nYour consequence is:")
    print(read_file(file_path, index))

    # NOTE: create code that automatically inputs consequence and date to a file (logbook)
    print(f"Consequences given on: {dt.datetime.today():%B %d, %Y @ %H:%M}")
    pass


def intro():
    print(
        "Welcome to the Consequences game!\n",
        "This is to punish you for:\n",
        "1. Eating \"meryenda\"\n",
        "2. Overeating during BREAKFAST, LUNCH, or DINNER\n",
        "3. Not doing / missing an action on my daily to-do list\n",
        "4. Getting annoyed and using unstable emotions to decide on thigns\n",
        )
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

def write_file(file_path):
    pass

# Create the main window

r = tk.Tk()

r.geometry("400x200")

r.title("Consequences")
button = tk.Button(r, text="Generate Consequence", command=lambda: main())

msg = Message(r, text="Welcome to the Consequences game!\nThis is to punish you for:\n1. Eating \"meryenda\"\n2. Overeating during BREAKFAST, LUNCH, or DINNER\n3. Not doing / missing an action on my daily to-do list\n4. Getting annoyed and using unstable emotions to decide on thigns\n")

msg.pack(pady=20)
button.pack(pady=20)

r.mainloop()