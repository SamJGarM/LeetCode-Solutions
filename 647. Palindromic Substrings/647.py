"""
Author: Samuel Jaden García Muñoz
Date: 20/08/2025
Revised: 29/09/2025

Note:-
Extremely similar solution to 5.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Searches for palindromes from left to right pointer.
        def search(left, right):
            searchRes = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                searchRes += 1
                left -= 1
                right += 1
            return searchRes

        res = 0

        # Iterate through every character in s as a starting point for palindromes.
        for i in range(len(s)):
            # Add all odd and even palindrome results.
            res += search(i, i) + search(i, i+1)
            
        return res
    
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""