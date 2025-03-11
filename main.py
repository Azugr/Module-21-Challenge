from menu import MENU  
from order_system import place_order
from receipt import print_itemized_receipt, print_receipt_heading, print_receipt_footer

def main():
    order, total_price = place_order(MENU)  

    print("\nThis is what we are preparing for you.\n")
    print_receipt_heading()
    print_itemized_receipt(order)
    print_receipt_footer(total_price)

if __name__ == "__main__":
    main()
