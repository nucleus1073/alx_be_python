# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 
# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
def main():
    """
    Main function to interact with the user and perform temperature conversions.
    """
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature to convert: ").strip())

        # Prompt user for the unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the conversion based on the unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            # Handle invalid unit input
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        # Handle invalid temperature or unit input
        print(f"Error: {e}. Please enter a valid numeric temperature and unit.")

# Ensure the script runs as intended when executed directly
if __name__ == "__main__": 
    main()