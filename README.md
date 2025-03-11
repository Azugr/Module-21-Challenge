# Takeout Order System

## Overview
This project is a **Takeout Order System** developed as part of a programming assignment. It allows users to browse a restaurant menu, place orders, and receive an itemized receipt. The system ensures accessibility by allowing both numeric and text-based input for item selection.

## Features
- Displays a structured menu with categories and items.
- Users can select menu items by entering numbers or item names.
- Supports multiple item selection at once.
- Validates user input and provides appropriate error messages.
- Prompts users to confirm their order before finalizing.
- Generates an itemized receipt with total pricing.

## Usage
### Running the Program
1. Open a terminal and navigate to the project directory:
   ```bash
   cd path/to/your_project
   ```
2. Run the program:
   ```bash
   python main.py
   ```

### Ordering Process
- The program displays the menu upon launch.
- Users can enter item numbers (e.g., `1,3,5`) or names (e.g., `burger - chicken`).
- The system asks for quantity confirmation.
- Users can continue adding items or quit by entering `q`.
- The final receipt is displayed.

## Example Output
```
=========== MENU ===========

--- Burritos ---
1   Burrito - Chicken              $4.49
2   Burrito - Beef                 $5.49
3   Burrito - Vegetarian           $3.99

--- Pizza ---
4   Pizza - Cheese                 $8.99
5   Pizza - Pepperoni              $10.99

Enter item numbers or names separated by commas (e.g., 1,4,pizza) or 'q' to quit: 2,5
How many Burrito - Beef would you like? 2
Added 2 Burrito - Beef(s) to your order.

How many Pizza - Pepperoni would you like? 1
Added 1 Pizza - Pepperoni(s) to your order.

Would you like to continue ordering? (y/n): n

Itemized Receipt:
--------------------------------------------------
Burrito - Beef        $5.49     x2
Pizza - Pepperoni    $10.99     x1
--------------------------------------------------
Total Price: $21.97
```

## Technical Details
- **Language:** Python
- **Concepts Used:** Loops, Functions, Dictionaries, Input Handling
- **Error Handling:** Prevents invalid inputs and unexpected crashes

## Assignment Note
This project was completed as part of a coding assignment for Module 21 of the bootcamp. It demonstrates practical implementation of Python concepts including loops, input validation, and data structures.

## 🎥 Walkthrough Video
A walkthrough video is included in the submission. It covers:
[🔗 https://drive.google.com/file/d/1VryIqEdwrhgXbFb_e2sPVa81e4wFrOQW/view?usp=drive_link]()

## GitHub Repository
This project is hosted on GitHub:
[🔗 https://github.com/Azugr/Module-21-Challenge](https://github.com/Azugr/Module-21-Challenge)

## Contribution
Feel free to fork, modify, and improve the project.

## License
MIT License
