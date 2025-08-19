"""
Author: Samuel Jaden García Muñoz
Date: 19/08/2025
Note:-

"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack for storing the latest opening parentheses/bracket -> (, [, {
        stack = []
        # Dict matching closing parentheses/bracket to opening for closing pairs.
        pairMap = {")": "(", "]": "[", "}": "{"}

        # Iterate through every character
        for char in s:
            # If character is a closer.
            if char in pairMap:
                # If the stack isn't empty and the closer matches the top of the stack, pop and continue.
                if stack and pairMap[char] == stack[-1]:
                    stack.pop()
                # Otherwise, bad pattern, return.
                else:
                    return False
            # If character is an opener, append it.
            else:
                stack.append(char)

        # If the stack is empty (all parentheses had a matching pair in order) return true
        return not stack
    
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""