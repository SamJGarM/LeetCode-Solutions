"""
Author: Samuel Jaden García Muñoz
Date: 13/11/2025
Revised: 
Note:-

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stack = []

        # Iterate through every bar in the chart.
        for idx, height in enumerate(heights):
            # Keep track of the starting index for checking previous index values that meet the height of the current bar.
            start_idx = idx
            # So long as the item on top of the stack is bigger than the current height...
            while stack and stack[-1][1] > height:
                # Pop the item from the stack and see if a new maximum has been found.
                pop_idx, pop_height = stack.pop()
                res = max(res, (idx - pop_idx) * pop_height)
                # Update the starting index, as the current value can now go back one position further.
                start_idx = pop_idx
            # Add the current bar to the stack.
            stack.append((start_idx, height))

        # Go through any items remaining in the stack, and check if they produce a better result.
        for idx, height in stack:
            res = max(res, height * (n - idx))
        
        # Return the best result.
        return res


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""