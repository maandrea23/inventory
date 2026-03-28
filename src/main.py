# Main entry point for inventory system
from validation import getOption
from menu import menu
from services import choose

inventory = []  # In-memory inventory: list of dicts

print("Welcome to the Complete Inventory System (CRUD + CSV)")

while True:
    try:
        option = getOption(menu)
        choose(option, inventory)
        if option == 9:
            break
    except KeyboardInterrupt:
        break

# Week goal: Complete inventory system with menu, validation, dict list, stats.

