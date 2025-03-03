# Coffee Machine GUI

## Introduction
This is a simple Coffee Machine simulation built using Python and Tkinter. The application allows users to select a coffee type, pay for it, and receive a virtual coffee along with a report of resources and earnings.

## Features
- **Graphical User Interface (GUI)**: Built using Tkinter.
- **Menu Options**: Select from Latte, Espresso, and Cappuccino.
- **Payment Processing**: User enters an amount, and the machine calculates change or rejects insufficient payments.
- **Resource Management**: Checks if there are enough ingredients to make the selected coffee.
- **Report Generation**: Displays remaining ingredients and total money earned.

## How to Use
1. Run the program:
   ```sh
   python coffee_machine.py
   ```
2. Select a coffee type from the available options.
3. If resources are sufficient, a payment window will open.
4. Enter the payment amount and press the **Pay** button.
5. If payment is sufficient, the coffee is prepared and served virtually.
6. Click **Report** to check remaining resources and total earnings.

## Class Structure
- `MenuItem`: Represents each coffee type with ingredients and cost.
- `Menu`: Stores available coffee types and finds drinks by name.
- `CoffeeMaker`: Handles resources and checks availability.
- `MoneyMachine`: Processes payments and keeps track of earnings.
- `CoffeeMachineGUI`: Creates the Tkinter-based GUI for interaction.

## Future Improvements
- Implement multiple coin types for more realistic transactions.
- Allow users to add more ingredients to refill the machine.
- Improve coffee graphics and animations.

Enjoy your virtual coffee! ☕

