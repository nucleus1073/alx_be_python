def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the provided operation.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation or a message for invalid inputs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Unsupported operation."

def main():
    """
    Main function to take user input and perform arithmetic operations.
    """
    print("Arithmetic Operations")
    
    try:
        # Input validation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        # Check if operation is valid
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Error: Unsupported operation. Please choose from add, subtract, multiply, or divide.")
            return

        # Perform operation
        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
