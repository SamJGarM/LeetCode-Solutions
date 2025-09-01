"""
Author: Samuel Jaden García Muñoz
Date: 01/09/2025
Note:-
Initial solution with string operations. Will solve with mathematical operations now.
"""

class Solution:
    def reverse(self, x: int) -> int:
        # Convert the value into a string.
        x = str(x)

        # If the value is negative, store this in the sign variable and
        # strip the first character from the string.
        (sign, x) = (False, x[1:]) if x[0] == '-' else (True, x)

        # Add every character from the string number inversely to the result string.
        # Note: Could do x[::1] for a simpler solution.
        res = ''
        for c in range(len(x) - 1, -1, -1):
            res += x[c]

        # If the number was negative, append the sign now.
        res = '-' + res if not sign else res
        
        # Convert the string into an integer.
        res = int(res)
        
        # If resulting number outside of 32-bit bounds, return 0.
        if not (-2**31 <= res <= 2**31 - 1):
            return 0
        
        # Otherwise, return the inverted integer.
        return res

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""