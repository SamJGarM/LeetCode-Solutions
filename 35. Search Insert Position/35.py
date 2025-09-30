"""
Author: Samuel Jaden García Muñoz
Date: 22/08/2025
Revised: 30/09/2025
Note:-

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Left and right pointers for binary search.
        left, right = 0, len(nums) - 1

        # Conduct the binary search as usual.
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            elif nums[middle] > target:
                right = middle - 1

            else:
                left = middle + 1

        # If target not found, instead of returning -1, return the left pointer index.
        return left

"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""