"""
Author: Samuel Jaden García Muñoz
Date: 17/08/2025
Note:-
Improved version using a bottom-up approach
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Return 1 if n is a base case.
        if n <= 1:
            return 1
        
        # Otherwise keep track of the last 2 values.
        latest, secondLatest = 1, 1
        for _ in range(2, n + 1):
            # Iteratively progress through the steps, keeping track of the latest 2.
            current = latest + secondLatest
            latest, secondLatest = current, latest

        # Once the end is reached, return the latest value.        
        return latest
    
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""