"""
Author: Samuel Jaden García Muñoz
Date: 01/09/2025
Revised: 08/11/2025
Note:-

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Dictionaries for keeping a running count of characters present in both strings.
        s1_count = {}
        s2_count = {}

        # Store all characters in s1 in the map.
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1

        # Iterate through every character in s2...
        for i in range(len(s2)):
            # Store the current character.
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

            # If i is >= than the len of s1 (our window is too large)...
            if i >= len(s1):
                # Remove the character outside of the window range
                # and delete it's entry if it is now empty.
                s2_count[s2[i-len(s1)]] -= 1
                if not s2_count[s2[i-len(s1)]]:
                    del s2_count[s2[i-len(s1)]]

            # If at any point the dictionaries match, a permutation has been found.
            if s1_count == s2_count:
                return True

        # Otherwise, a permutation has not been found.
        return False

"""
Time Complexity: O(s1 + s2)
Space Complexity: O(s1)
"""