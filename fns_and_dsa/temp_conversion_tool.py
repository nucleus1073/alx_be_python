# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

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
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): ").strip())
            
            if choice == 1:
                try:
                    fahrenheit = float(input("Enter temperature in Fahrenheit: ").strip())
                    celsius = convert_to_celsius(fahrenheit)
                    print(f"{fahrenheit}°F is {celsius:.2f}°C")
                except ValueError:
                    print("Error: Please enter a valid number for the temperature.")
            
            elif choice == 2:
                try:
                    celsius = float(input("Enter temperature in Celsius: ").strip())
                    fahrenheit = convert_to_fahrenheit(celsius)
                    print(f"{celsius}°C is {fahrenheit:.2f}°F")
                except ValueError:
                    print("Error: Please enter a valid number for the temperature.")
            
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Error: Please enter a valid choice (1-3).")
        
        except ValueError:
            print("Error: Invalid input. Please enter a number (1-3).")

# Entry Point
if __name__ == "__main__":
    main()
