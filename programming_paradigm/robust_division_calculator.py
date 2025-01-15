def safe_divide(numerator, denominator):
    """
    Perform division while handling potential errors such as division by zero and non-numeric inputs.
    :param numerator: The numerator for the division.
    :param denominator: The denominator for the division.
    :return: The result of the division or an appropriate error message.
    """
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line arguments and perform division.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
