from utils import validate_integer_input
from update_order import update_order
from menu import get_menu_items_dict, print_menu_heading, print_menu_line, MENU
from receipt import print_itemized_receipt


def place_order(menu):
    """
    Allows the user to place an order from the menu.
    """
    order = []
    total_price = 0
    menu_items = get_menu_items_dict(menu)

    while True:
        print("\n=========== MENU ===========\n")
        all_items = {}  # Dictionary to store valid inputs
        item_number = 1

        for category, items in menu.items():
            print(f"\n--- {category} ---\n")
            for item in items:
                formatted_name = item['name'].lower().replace(" ", "-")
                print(f"{item_number}. {item['name']:<30} ${item['price']:.2f}")

                # Store all possible input variations (numbers and names in different cases)
                all_items[str(item_number)] = item  # Lookup by number
                all_items[formatted_name] = item  # Lookup by lowercase formatted name
                all_items[item['name'].lower()] = item  # Normal lowercase name
                all_items[item['name'].title()] = item  # Title case name
                all_items[item['name'].upper()] = item  # Uppercase name
                item_number += 1
            print()

        # 🛠 Fix: Strip dots & extra spaces from input
        item_choices = input("\nEnter item numbers or names separated by commas (e.g., 1,4,pizza) or 'q' to quit: ").strip().replace(".", "")
        if item_choices.lower() == 'q':
            break

        # Process input
        selected_items = [choice.strip().lower() for choice in item_choices.split(",")]

        for item_choice in selected_items:
            if item_choice in all_items:  # If it's a valid selection
                selected_item = all_items[item_choice]
            else:
                print(f"Invalid input: {item_choice}. Please enter a valid number or item name.")
                continue

            quantity = input(f"How many {selected_item['name']} would you like? ")

            if not quantity.isdigit():
                print("Invalid quantity. Defaulting to 1.")
                quantity = 1
            else:
                quantity = int(quantity)

            order.append({"Item name": selected_item['name'], "Price": selected_item['price'], "Quantity": quantity})
            print(f"Added {quantity} {selected_item['name']}(s) to your order.")

        continue_ordering = input("\nWould you like to continue ordering? (y/n): ").strip().lower()
        if continue_ordering == 'n':
            break

    total_price = round(sum(item["Price"] * item["Quantity"] for item in order), 2)
    return order, total_price
