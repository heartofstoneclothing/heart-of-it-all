#calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Dictionary of operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print("Calculator!")
    print("Available operations: +, -, *, /")

    while True:
        try:
            # Input numbers and operation
            first_number = float(input("\nEnter the first number: "))
            operation = input("Enter the operator (+, -, *, /): ").strip()
            if operation not in operations:
                print("Invalid operation. Please choose an operator +, -, *, /.")
                continue
            second_number = float(input("Enter the second number: "))

            # Perform the operation
            result = operations[operation](first_number, second_number)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input!")

        more = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if more not in ('y'):
            print("Thank you for using the Calculator. Goodbye!")
            break

calculator()
