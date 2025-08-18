"""
Author: Samuel Jaden García Muñoz
Date: 
Note:-

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Create variables for storing the longest palindrome found and its length
        res = ""
        resLen = 0

        # Iterate through every character in the string as a starting position
        for i in range(len(s)):
            # Initialize the left and right pointers to i (for odd-length palindromes)
            left, right = i, i
            # While left and right in bounds and left and right characters equal.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if current palindrome is best, and update result accordingly
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    res = s[left:right + 1]
                # Move pointers away from source accordingly
                left -= 1
                right += 1

            # Repeat previous steps, this time for even-length palindromes.
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1

        # Return the best outcome.
        return res
    
"""
Time Complexity:
Space Complexity:
"""