"""
Author: Samuel Jaden García Muñoz
Date: 
Revised: 
Note:-

"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        # Iterate through every string and encode it with the following format:
        # n (Length of String) + ! (Delimiting Character) + x (String Content)
        for s in strs:
            res += f"{len(s)}!{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        # Iterate through the entirety of the encoded string.
        i = 0
        while i < len(s):
            # Initialize j to the value of our iterator.
            j = i
            # Until we find the delimiter, increase j
            while s[j] != "!":
                j += 1
            # Use j to determine the length of the word.
            length = int(s[i:j])
            
            # Append the word to the result.
            # From j + 1 (for the delimiter) to j + 1 (again) + the length of the word. 
            res.append(s[j+1:j+1+length])

            # Finally, increase i to the next segment of the encoded string.
            i = j + 1 + length

        return res

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""