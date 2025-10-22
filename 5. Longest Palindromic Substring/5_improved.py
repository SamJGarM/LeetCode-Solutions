"""
Author: Samuel Jaden García Muñoz
Date: 18/08/2025
Revised: 10/22/2025
Note:-
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Create variables for storing the longest palindrome found and its length
        res = ""
        
        # Given the initial position of the left and right pointers, iterate outwards from the source
        # and return the best length palindrome.
        def search(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # Iterate through every character in the string as a starting position.
        for i in range(len(s)):
            # Initialize the left and right pointers to i (for odd-length palindromes)
            odd_palindrome = search(i, i)
            # Initialize the left and right pointers to i and i + 1 (for even-length palindromes)
            even_palindrome = search(i, i + 1)

            # Check both palindromes and compare to the current result, and keep the best.
            for palindrome in [odd_palindrome, even_palindrome]:
                if len(palindrome) > len(res):
                    res = palindrome

        # Return the best outcome.
        return res
    
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""