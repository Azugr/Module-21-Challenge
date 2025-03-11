def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("\n==================== ITEMIZED RECEIPT ====================")
    print(f"{'Item Name':<30}{'Quantity':<10}{'Total Price':<10}")
    print("-----------------------------------------------------------")


def print_itemized_receipt(order):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    """
    # Print the receipt heading
    print_receipt_heading()

    for item in order:
        item_name = item["Item name"]  
        item_price = item["Price"]
        item_quantity = item["Quantity"]

        # Send values to print_receipt_line function
        print_receipt_line(item_name, item_price, item_quantity)

    # Print the footer with total price
    total_price = sum(item["Price"] * item["Quantity"] for item in order)
    print_receipt_footer(total_price)


def print_receipt_footer(total_price):
    """
    Prints the footer with the total price.
    """
    print("-----------------------------------------------------------")
    print(f"{'TOTAL':<42}${total_price:.2f}")
    print("===========================================================\n")


def print_receipt_line(item_name, price, quantity):
    """
    Prints each line of the receipt in a structured format.
    """
    total_item_price = price * quantity
    print(f"{item_name:<30} x{quantity:<10} ${total_item_price:.2f}")
