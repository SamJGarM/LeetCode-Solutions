"""
Author: Samuel Jaden García Muñoz
Date: 01/09/2025
Note:-
Initial solution with string operations. Will solve with mathematical operations now.
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        while x > 0:
            temp = x
            digit = x % 10
            x = x // 10

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""