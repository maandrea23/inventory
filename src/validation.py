# Menu option validation
def getOption(options):
    while True:
        for i, option in enumerate(options, start=1):
            print(f"{i} - {option}")
        try:
            sel = int(input("Select option (1-9): "))
            if 1 <= sel <= 9:
                return sel
            print("Please choose 1-9.")
        except ValueError:
            print("Enter a valid number.")

