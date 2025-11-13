"""
Author: Samuel Jaden García Muñoz
Date: 13/11/2025
Revised: 
Note:-

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            # If n == 0, return 1, as any number raised to the power of 0 is equal to 1.
            if n == 0:
                return 1
            # If x == 0, return 0, as 0 raised to the power of anything (except for 1) is 0.
            if x == 0:
                return 0
            
            # Then calculate the value of the power at half the exponent.
            res = pow(x, n // 2)
            # Multiply it by itself.
            res = res * res
            # Since we're rounding down with // 2, we will have to check each round if the current exponent is
            # odd or even, to check whether we should add an extra multiplication to the result before returning.
            return res if n % 2 == 0 else res * x
        
        # Calculate the result, using the absolute value of the exponent.
        res = pow(x, abs(n))
        # Return the result, returning 1 over the result if the exponent was initially negative.
        return res if n >= 0 else 1 / res


"""
Time Complexity: O(log n)
Space Complexity: O(log2 n)
"""