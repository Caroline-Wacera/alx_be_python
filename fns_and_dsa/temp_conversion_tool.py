# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Accessing the global variable
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # Accessing the global variable
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# User Interaction
def temperature_conversion_tool():
    try:
        # Prompt user to input a temperature
        temperature = float(input("Enter the temperature to convert: "))

        # Ask for the unit of the input temperature
        unit = (
            input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
            .strip()
            .upper()
        )

        if unit == "C":
            # Call the conversion function for Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            # Call the conversion function for Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            # Handle invalid input for unit
            print(
                "Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."
            )
    except ValueError:
        # Handle invalid temperature input
        print("Invalid temperature. Please enter a numeric value.")


# Run the tool
if __name__ == "__main__":
    temperature_conversion_tool()