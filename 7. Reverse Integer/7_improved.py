"""
Author: Samuel Jaden García Muñoz
Date: 01/09/2025
Note:-
Improvement on previous solution with a mathematical approach.
"""

class Solution:
    def reverse(self, x: int) -> int:
        # Keep track of the sign of the integer.
        sign = -1 if x < 0 else 1

        # Create a result variable and set the integer to its absolute.
        res, x = 0, abs(x)

        # So long as x > 0:
        while x:
            # Get the digit position and decrease the integer by a power of ten.
            digit = x % 10
            x //= 10
            # Then increase the current result by 10, and add the new digit.
            res = res * 10 + digit

        # Turn the result negative if necessary.
        res *= sign
            
        # Then check if the result is a valid 32-bit integer and return accordingly.
        return res if -2**31 <= res <= 2**31-1 else 0

"""
Time Complexity: O(logx)
Space Complexity: O(1)
"""