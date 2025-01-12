# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
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

# User Interaction and Value Error Handling
def main():
    """
    Main function to interact with the user for temperature conversion.
    """
    print("Temperature Converter")

    while True:
        try:
            # Get temperature input
            temperature = float(input("Enter the temperature to convert: "))
            
            # Get unit input
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            
            # Perform the conversion based on the unit
            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F")
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
            # Option to exit or continue
            again = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
