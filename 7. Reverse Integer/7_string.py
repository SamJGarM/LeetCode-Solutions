"""
Author: Samuel Jaden García Muñoz
Date: 29/9/2025
Revised: 
Note:-

"""

class Solution:
    def reverse(self, x: int) -> int:
        # Turn the integer value into a string.
        x = str(x)

        # Boolean flag for detecting if a given string is negative.
        isNegative = x[0] == '-'
        
        # If it's negative, strip the dash from the beginning of the string.
        if isNegative:
            x = x[1:]

        # Reverse the string.
        x = x[::-1]

        # Reappend the dash (negative symbol) if needed.
        if isNegative:
            x = '-' + x

        # Convert the string back into integer, as it is the desired return type.
        x = int(x)

        # Return the value if it is within the constraints, otherwise, return 0.
        return x if -2**31 <= x <= 2**31-1 else 0

"""
Time Complexity: O(log x)
Space Complexity: O(log x)
"""
