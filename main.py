from menu import get_menu_dictionary
from order_system import place_order
from receipt import print_itemized_receipt, print_receipt_heading, print_receipt_footer

def main():
    meals = get_menu_dictionary()
    order, total_price = place_order(meals)

    print("\nThis is what we are preparing for you.\n")
    print_receipt_heading()
    print_itemized_receipt(order)
    print_receipt_footer(total_price)

if __name__ == "__main__":
    main()
