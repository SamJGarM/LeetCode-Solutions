"""
Author: Samuel Jaden García Muñoz
Date: 21/08/2025
Note:-
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Running best volume.
        best = 0
        # Left and right pointers.
        left, right = 0, len(height) - 1

        # So long as the length is at least 1.
        while left < right:
            # Keep track if this volume is the best.
            best = max(best, min(height[left], height[right]) * (right - left))

            # Afterwards, move a pointer forward, according to which side is the smallest.
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        # Return the best volume.
        return best

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""