"""
These functions validate responses.
"""


def validate_binary_response(prompt):
    while True:
        value = input(prompt)
        # Checks for valid input
        if not value == "0":
            if not value == "1":
                error_bar_print("The response must be 1 or 0.")
                continue
            else:
                break
        else:
            break
    return value


def validate_text_response(prompt):
    while True:
        # Checks for empty string
        value = input(prompt)
        if value == "":
            error_bar_print("The screen name cannot be blank.")
            continue
        else:
            break
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
    return value


def error_bar_print(error):
    top_bar = "##-------------ERROR-------------##"
    bottom_bar = "##-------------------------------##"

    print(top_bar)
    print(error)
    print(bottom_bar)