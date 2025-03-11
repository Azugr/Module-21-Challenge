from get_menu_dictionary import get_menu_items_dict
from update_order import update_order

def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    place_order = True
    while place_order:
        # Print menu heading
        print_menu_heading()

        # Loop through the menu dictionary and display the items
        for index, details in menu_items.items():
            print_menu_line(index, details["Item name"].split(" - ")[0], 
                            details["Item name"].split(" - ")[1], details["Price"])

        # Ask customer to input menu item number
        menu_selection = input("Type menu number: ").strip()

        # Update the order list using the update_order function
        order = update_order(order, menu_selection, menu_items)

        # Ask if they want to continue ordering
        keep_ordering = input("Would you like to keep ordering? (N) to quit: ").strip().lower()
        if keep_ordering == 'n':
            print("Thank you for your order.")
            place_order = False

    # Calculate the total price
    prices_list = [item["Price"] * item["Quantity"] for item in order]
    order_total = round(sum(prices_list), 2)

    return order, order_total
