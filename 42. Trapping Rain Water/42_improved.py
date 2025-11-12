"""
Author: Samuel Jaden García Muñoz
Date: 21/08/2025
Revised: 12/11/2025
Note:-
Improved approach with 2 pointers to reduce the space complexity.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # Left and right pointer for tracking our position through the array.
        left, right = 0, len(height) - 1
        # Left and right maximum variables for tracking the edges for trapping water.
        leftMax, rightMax = height[left], height[right]

        # Variable for keeping a running result of water we're trapping.
        res = 0

        # Iterate until the pointers meet.
        while left <= right:
            # Proceeding with the smallest maximum.
            if leftMax < rightMax:
                # Check if we've reached a new maximum.
                if height[left] > leftMax:
                    leftMax = height[left]
                # If we haven't, add the amount of water we can collect (or 0 in the case of a negative value).
                else:
                    res += max(leftMax - height[left], 0)
                # Increase the left pointer.
                left += 1
            # Repeat the process if the rightMax is the smaller maximum.
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    res += max(rightMax - height[right], 0)
                right -= 1
        
        # Return the result.
        return res

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""