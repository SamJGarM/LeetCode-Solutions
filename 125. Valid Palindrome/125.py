"""
Author: Samuel Jaden García Muñoz
Date: 03/11/2025
Revised: 
Note:-
Can be improved by using a two-pointer approach to reduce space complexity to O(1).
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for c in s:
            if c.isalnum():
                stripped += c.lower()

        return stripped == stripped[::-1]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""