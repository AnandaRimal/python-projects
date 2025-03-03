import tkinter as tk
from tkinter import messagebox

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns a list of all available menu items."""
        return [item.name for item in self.menu]

    def find_drink(self, order_name):
        """Finds a drink by its name."""
        for item in self.menu:
            if item.name.lower() == order_name.lower():
                return item
        return None


class CoffeeMaker:
    """Models the machine that makes the coffee."""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        return "\n".join([f"{item.title()}: {amount}ml" if item != "coffee" else f"{item.title()}: {amount}g" for item, amount in self.resources.items()])

    def is_resource_sufficient(self, drink):
        """Checks if resources are sufficient for the drink."""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                return False, item
        return True, None

    def make_coffee(self, drink):
        """Deducts the required ingredients from the resources."""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]


class MoneyMachine:
    """Handles money transactions."""
    CURRENCY = "$"

    def __init__(self):
        self.profit = 0

    def report(self):
        """Returns the current profit."""
        return f"Money: {self.CURRENCY}{self.profit:.2f}"

    def process_payment(self, cost, payment_amount):
        """Processes coins and checks if payment is sufficient."""
        if payment_amount >= cost:
            change = round(payment_amount - cost, 2)
            self.profit += cost
            return True, change
        else:
            return False, 0


class CoffeeMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Machine")
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

        self.create_widgets()

    def create_widgets(self):
        # Menu Buttons
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        for item in self.menu.get_items():
            button = tk.Button(self.menu_frame, text=item.title(), command=lambda item=item: self.order_drink(item))
            button.pack(side="left", padx=5)

        # Status
        self.status_label = tk.Label(self.root, text="Select a drink", font=("Arial", 14))
        self.status_label.pack(pady=10)

        # Report Button
        self.report_button = tk.Button(self.root, text="Report", command=self.show_report)
        self.report_button.pack(pady=10)

    def order_drink(self, drink_name):
        drink = self.menu.find_drink(drink_name)
        if not drink:
            messagebox.showerror("Error", "Sorry, that item is not available.")
            return

        sufficient, missing_item = self.coffee_maker.is_resource_sufficient(drink)
        if not sufficient:
            messagebox.showerror("Error", f"Sorry, there is not enough {missing_item}.")
            return

        payment_window = tk.Toplevel(self.root)
        payment_window.title(f"Pay for {drink.name.title()}")

        # Payment entry
        payment_label = tk.Label(payment_window, text=f"Please insert coins. The cost is ${drink.cost:.2f}.")
        payment_label.pack(pady=10)

        payment_entry = tk.Entry(payment_window, font=("Arial", 14))
        payment_entry.pack(pady=10)

        def process_payment():
            try:
                payment_amount = float(payment_entry.get())
                payment_successful, change = self.money_machine.process_payment(drink.cost, payment_amount)
                if not payment_successful:
                    messagebox.showerror("Error", "Sorry, that's not enough money. Money refunded.")
                else:
                    if change > 0:
                        messagebox.showinfo("Change", f"Here is your change: ${change:.2f}")
                    self.coffee_maker.make_coffee(drink)
                    messagebox.showinfo("Success", f"Here is your {drink.name.title()} ☕. Enjoy!")
                payment_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid amount.")

        # Process payment button
        process_button = tk.Button(payment_window, text="Pay", command=process_payment)
        process_button.pack(pady=10)

    def show_report(self):
        report = self.coffee_maker.report() + "\n" + self.money_machine.report()
        messagebox.showinfo("Machine Report", report)


# Run the GUI coffee machine program
if __name__ == "__main__":
    root = tk.Tk()
    coffee_machine_gui = CoffeeMachineGUI(root)
    root.mainloop()
