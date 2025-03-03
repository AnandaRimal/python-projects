print("Welcome to the Calculator!")
from art import logo
print(logo)

# Define basic operations
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

# Mapping operations to their functions
operations = {
    "*": mul,
    "-": sub,
    "+": add,
    "/": div
}

# Get initial inputs and calculate the first result
user_given = input("Enter the operation (*, +, -, /) you want to perform: ")
while user_given not in operations:
    print("Invalid operation. Please enter a valid operation: *, +, -, /")
    user_given = input("Enter the operation (*, +, -, /): ")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    calculate_function = operations[user_given]
    answer = calculate_function(num1, num2)
    print(f"The result is: {answer}")
except ValueError:
    print("Error! Please enter numeric values.")
    exit()

# Loop for further operations
next_operation = True
while next_operation:
    pick = input("Do you want to perform another operation? Type 'yes' to continue or 'no' to exit: ").lower()
    if pick == "yes":
        second_operation = input("Enter the next operation (*, +, -, /): ")
        while second_operation not in operations:
            print("Invalid operation. Please enter a valid operation: *, +, -, /")
            second_operation = input("Enter the next operation (*, +, -, /): ")

        try:
            num3 = float(input("Enter the next number: "))
            calculate_function = operations[second_operation]
            answer = calculate_function(answer, num3)
            print(f"The new result is: {answer}")
        except ValueError:
            print("Error! Please enter numeric values.")
    elif pick == "no":
        next_operation = False
        print("Thank you for using the calculator!")
    else:
        print("Invalid choice. Please type 'yes' to continue or 'no' to exit.")
