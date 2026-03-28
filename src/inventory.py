# Input validation function
def inventory(type_input, msg, error_msg):
    user_input = input(msg)
    # Validate non-empty for str
    if type_input is str:
        if not user_input.strip():
            print(error_msg)
            return inventory(type_input, msg, error_msg)
    # Validate positive for numbers
    try:
        value = type_input(user_input)
        if type_input in (int, float) and value < 0:
            print(error_msg)
            return inventory(type_input, msg, error_msg)
        return value
    except ValueError:
        print(error_msg)
        return inventory(type_input, msg, error_msg)


