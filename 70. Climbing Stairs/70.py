"""
Author: Samuel Jaden García Muñoz
Date: 17/08/2025
Note:-

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a dictionary for memoization.
        memo = {}

        # Recursive function that takes the amount of steps_left.
        def climb(steps_left):
            # If this section has been navigated beforehand, return the stored solution.
            if steps_left in memo:
                return memo[steps_left]
            # If base case reached, return 1 (destination reached / 1 step to destination).
            if steps_left <= 1:
                return 1
            
            # Since the current section hasn't been navigated before, find it's solution and store it to our memo dict.
            memo[steps_left] = climb(steps_left - 1) + climb(steps_left - 2)
            return memo[steps_left]
        
        # Return the result
        return climb(n)
    
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""