"""
Author: Samuel Jaden García Muñoz
Date: 13/11/2025
Revised: 
Note:-
Brute force approach that solves problems, but has a very high time complexity.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        # Iterate through every bar in the chart.
        for i in range(n):
            # Get the height at the current position.
            height = heights[i]
            # And iterate through every height value from this position (from bottom to top).
            for j in range(height):
                width = 0
                # While the bar to the right is of the same height, or greater, extend the width.
                while i + width + 1 <= n and heights[i + width] >= height - j:
                    width += 1
                # Check if the bar formed by the maximum rectangle starting from this bar at this height beats the current maximum.
                res = max(res, (height - j) * width)
        # Return the best result found.
        return res

"""
Time Complexity: O(n^2 * h)
Space Complexity: O(1)
"""