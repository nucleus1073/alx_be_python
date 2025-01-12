# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

# Display Menu
def display_menu():
    """
    Display menu options for temperature conversion.
    """
    print("\nTemperature Converter Menu:")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")

# Main Function
def main():
    """
    Main function for temperature conversion with error handling and user interaction.
    """
    while True:
        # Call menu
        display_menu()

        try:
            # User selects an option
            choice = int(input("Enter your choice (1-3): ").strip())
            
            if choice == 1:
                # Conversion from Fahrenheit to Celsius
                try:
                    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                    celsius = convert_to_celsius(fahrenheit)
                    print(f"{fahrenheit}°F is {celsius:.2f}°C")
                except ValueError:
                    print("Error: Please enter a valid numerical value.")
            
            elif choice == 2:
                # Conversion from Celsius to Fahrenheit
                try:
                    celsius = float(input("Enter temperature in Celsius: "))
                    fahrenheit = convert_to_fahrenheit(celsius)
                    print(f"{celsius}°C is {fahrenheit:.2f}°F")
                except ValueError:
                    print("Error: Please enter a valid numerical value.")
            
            elif choice == 3:
                # Exit the program
                print("Exiting the program. Goodbye!")
                break
            
            else:
                # Invalid menu choice
                print("Invalid choice. Please enter a number between 1 and 3.")

        except ValueError:
            # Handle non-integer input for the menu
            print("Error: Please enter a valid number for menu options.")

# Entry Point
if __name__ == "__main__":
    main()
