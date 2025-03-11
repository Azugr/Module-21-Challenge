def validate_integer_input(prompt, default=1):
    """
    Prompts the user for an integer input. If the input is invalid, returns the default value.
    """
    user_input = input(prompt).strip()
    if user_input.isdigit():
        return int(user_input)
    else:
        print(f"Invalid input. Defaulting to {default}.")
        return default

def format_price(price):
    """
    Formats a price to two decimal places with a dollar sign.
    """
    return f"${price:.2f}"


def clear_screen():
    """
    Clears the terminal screen for better readability.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a formatted line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    index_spaces = " " * (6 if index < 10 else 5)

    print(f"{index}{index_spaces}| {food_category} - {meal}{item_spaces} | ${price:.2f}")
