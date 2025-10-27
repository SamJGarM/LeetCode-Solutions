"""
Author: Samuel Jaden García Muñoz
Date: 26/10/2025
Revised: 27/10/2025
Note:-
Maintain a variable with the value of the most frequently repeating character to reduce constantly calls
to max(count.values()) which could be up to 26 comparisons if all letters are used.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dict for holding each character and its count in a given slice
        count = {}
        res = 0

        # Maximum frequency tracker to avoid repeat max() calls.
        max_freq = 0
        # Left pointer for beginning of slice
        left = 0
        # Right pointer for end of slice
        for right in range(len(s)):
            # Update the dict entry (if existing, otherwise create it)
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # If our slice size minus the amount of same characters is greater than k,
            # we currently have an invalid segment. Therefore, remove characters from the left
            # until a successful slice is obtained.
            while right - left + 1 - max_freq > k:
                # Update the dict accordingly and increase the left pointer.
                count[s[left]] -= 1
                left += 1

            # The result is then the maximum value of our slice and the existing result.
            res = max(res, right - left + 1)

        return res

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""