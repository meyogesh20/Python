''' Python Coding Style (PEP 8 Highlights) '''
#| ✅ Feature                    | Description
#| -------------------------------------------------------------------------------------------------------
#| ✅ 4-space indentation        | All blocks are consistently indented                                   
#| ✅ Docstrings (comments)      | For class, methods, and functions                                      
#| ✅ Blank lines                | Used to separate logical sections                                      
#| ✅ Line wrapping              | All lines < 79 characters                                              
#| ✅ Naming conventions         | `UpperCamelCase` for class, `lowercase_with_underscores` for functions 
#| ✅ Comments                   | Clearly used where needed                                              
#| ✅ No tabs or fancy encodings | Uses default UTF-8          
#| -------------------------------------------------------------------------------------------------------

# my_module.py

from typing import List


class TemperatureConverter:
    """A class for converting temperatures between Celsius and Fahrenheit."""

    def __init__(self, temperature: float):
        self.temperature = temperature

    def to_celsius(self) -> float:
        """Convert stored temperature from Fahrenheit to Celsius."""
        return (self.temperature - 32) * 5 / 9

    def to_fahrenheit(self) -> float:
        """Convert stored temperature from Celsius to Fahrenheit."""
        return (self.temperature * 9 / 5) + 32


def average(numbers: List[float]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def main():
    """Main function demonstrating class and function usage."""
    temps_f = [32, 68, 86]
    temps_c = []

    for temp in temps_f:
        converter = TemperatureConverter(temp)
        celsius = converter.to_celsius()
        temps_c.append(celsius)
        print(f"{temp}°F = {celsius:.2f}°C")

    print("\nAverage temperature in Celsius:", average(temps_c))


if __name__ == "__main__":
    main()

#| -------------------------------------------------------------------------------------------------------
# ✅ Python Coding Style (PEP 8 Highlights)
# Indentation: Use 4 spaces per indentation level — no tabs.

# Line Length: Limit lines to 79 characters to improve readability and side-by-side viewing.

# Blank Lines: Use them to separate functions, classes, and logical code blocks.

# Comments: Place comments on their own line when possible. Keep them clear and concise.

# Docstrings: Use them to describe the purpose of functions, classes, and modules.

# Spacing: Use spaces around operators and after commas. Avoid spaces directly inside 
#          parentheses, brackets, or braces.

# Naming Conventions:
# 1. Classes: UpperCamelCase
# 2. Functions & methods: lowercase_with_underscores

# Always use self as the first argument in instance methods.

# Encodings: Stick to UTF-8 (default) or ASCII for compatibility.

# Identifiers: Avoid non-ASCII characters in variable/function/class names to ensure global readability.