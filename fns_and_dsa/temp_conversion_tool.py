# Global Conversion Factors
CONVERSION_FACTORS = {
    "FAHRENHEIT_TO_CELSIUS_FACTOR": 5 / 9,
    "CELSIUS_TO_FAHRENHEIT_FACTOR": 9 / 5,
    "FAHRENHEIT_OFFSET": 32
}

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - CONVERSION_FACTORS["FAHRENHEIT_OFFSET"]) * CONVERSION_FACTORS["FAHRENHEIT_TO_CELSIUS_FACTOR"]

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * CONVERSION_FACTORS["CELSIUS_TO_FAHRENHEIT_FACTOR"]) + CONVERSION_FACTORS["FAHRENHEIT_OFFSET"]

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
            
            # Perform operations based on user choice
            if choice == 1:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = convert_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is {celsius:.2f}°C")
            elif choice == 2:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = convert_to_fahrenheit(celsius)
                print(f"{celsius}°C is {fahrenheit:.2f}°F")
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

        except ValueError:
            print("Invalid input. Please enter numeric values for temperature and a number for menu options.")

# Entry Point
if __name__ == "__main__":
    main()
