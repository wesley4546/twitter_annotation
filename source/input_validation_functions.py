"""
These functions validate responses.
"""


def validate_binary_response(prompt):
    while True:
        value = input(prompt)
        # I made it check for the string version so I don't have to worry about True and False
        if not value == "0":
            if not value == "1":
                error_bar_print("The response must be 1 or 0.")
                continue
            else:
                break
        else:
            break
    # Output is a str
    return value


def validate_text_response(prompt):
    while True:
        # Checks for empty string
        value = input(prompt)
        if value == "":
            error_bar_print("The text cannot be blank.")
            continue
        else:
            break
    # Output is a str
    return value


def validate_category_response(prompt, number_of_categories):
    while True:
        # Checks for integer
        try:
            value = int(input(prompt))
        except ValueError:
            error_bar_print("The response must be a number.")
            continue
        if value not in range(1, number_of_categories + 1):
            error_bar_print("The response must be one of the categories")
        else:
            break
    # output is a int
    return value


def validate_numeric_response(prompt):
    while True:
        # Checks for integer
        try:
            value = int(input(prompt))
        except ValueError:
            error_bar_print("The response must be a number.")
        else:
            break
    return value


def error_bar_print(error):
    # Aesthetics
    top_bar = "\n##--------------------------ERROR--------------------------##"
    bottom_bar = "##---------------------------------------------------------##\n"

    print(top_bar)
    print(error)
    print(bottom_bar)
