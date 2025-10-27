"""
Author: Samuel Jaden García Muñoz
Date: 26/10/2025
Revised: 
Note:-

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Dicts for holding each character and their frequency/count.
        s_count = {}
        t_count = {}

        # Edge statement if the lengths of the strings are mismatching.
        if len(s) != len(t):
            return False

        # Iterate through each character in both strings and add them to their corresponding dict.
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        # Return if the contents are the same.
        return s_count == t_count

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""