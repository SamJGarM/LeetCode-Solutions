"""
Author: Samuel Jaden García Muñoz
Date: 26/10/2025
Revised: 08/11/2025
Note:-

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        # Iterate through every string
        for string in strs:
            # Create an array with 26 0-values for each possible letter.
            count = [0] * 26

            # Iterate through each character in the string, adding it to the array as it's found.
            for char in string:
                count[ord(char) - ord("a")] += 1
            
            # We turn the count of characters from a list into a tuple so we can use it as a key for the res dict.
            count = tuple(count)

            # Check if a matching entry exists in the dict already.
            if count not in res:
                # ... and if not, create one...
                res[count] = []
            # Then append to the list at the dict entry.
            res[count].append(string)

        # Lastly, return the list of the values.
        return list(res.values())

"""
Time Complexity: O(m * n) - total number of strings * average length of each string * (amount of letters)
Space Complexity: O(m * n)
"""