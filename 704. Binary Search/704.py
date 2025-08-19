"""
Author: Samuel Jaden García Muñoz
Date: 19/08/2025
Note:-
Iterative alternative for DFS.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Left and right pointers
        left, right = 0, len(nums) - 1

        # Until the left and right pointers meet.
        while left <= right:
            # Get the middle position.
            middle = (right + left) // 2
            # Check if we've found our target.
            if nums[middle] == target:
                return middle
            # If the target is larger than the middle value, then we know our left value can move forward.
            if target > nums[middle]:
                left = middle + 1
            # Otherwise we know our right value can move down.
            else:
                right = middle - 1

        # In case target is not in the array.
        return -1
    
"""
Time Complexity: O(n)
Space Complexity: O(h) 
"""