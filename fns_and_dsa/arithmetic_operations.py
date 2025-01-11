def perform_operation(n1, n2, operation):
    
    try:
        if operation == 'add':
            return n1 + n2
        elif operation == 'subtract':
            return n1 - n2
        elif operation == 'multiply':
            return n1 * n2
        elif operation == 'divide':
            if n2 == 0:
                return "Error: Division by zero is not allowed."
            return n1 / n2
        else:
            return "Error: Unsupported operation."
    except Exception as e:
        return f"Error: {str(e)}"
    def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()