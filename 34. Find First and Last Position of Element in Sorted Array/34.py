"""
Author: Samuel Jaden García Muñoz
Date: 20/08/2025
Revised: 10/22/2025
Note:-
Suboptimal solution that doesn't reach O(log(n)) complexity, but it still gives a passing result.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Left and right pointers for a binary search.
        left, right = 0, len(nums) - 1

        while left <= right:
            # Get the middle position/
            middle = (left + right) // 2

            # If the target is found...
            if nums[middle] == target:
                # Branch out from the current position and find the left and rightmost likewise values.
                left, right = middle, middle
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
            
                # Return this range.
                return [left, right]

            # Otherwise operate as a binary search would normally.
            if nums[middle] > target:
                right = middle - 1

            else:
                left = middle + 1

        # If target is not found return [-1, -1]
        return [-1, -1]

"""
Time Complexity: O(log n + k)
Space Complexity: O(1)
"""