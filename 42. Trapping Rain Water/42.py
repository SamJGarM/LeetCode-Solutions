"""
Author: Samuel Jaden García Muñoz
Date: 21/08/2025
Revised: 12/11/2025
Note:-

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # Array for checking the max in any given location from the left.
        leftMax = [0] * len(height)
        # ... from the right.
        rightMax = [0] * len(height)

        # Iterate through the entire array and store the current max height from the left.
        for i in range(len(height)):
            if i == 0:
                leftMax[i] = height[i]
            else:
                leftMax[i] = max(height[i], leftMax[i - 1])
        
        # Iterate through the entire array and store the current max height from the right.
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                rightMax[i] = height[len(height) - 1]
            else:
                rightMax[i] = max(height[i], rightMax[i + 1])

        # Run through the array one last time, calculating the max difference in height at any given position,
        # only taking values greater than 0. (as we can't trap negative water)
        res = 0
        for i in range(len(height)):
            res += max(0, min(leftMax[i], rightMax[i]) - height[i])
                
        # Return the result.
        return res

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""