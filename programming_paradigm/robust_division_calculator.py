def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Handle division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division and return result
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."