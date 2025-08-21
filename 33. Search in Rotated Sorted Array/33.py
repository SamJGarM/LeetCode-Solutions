"""
Author: Samuel Jaden García Muñoz
Date: 21/08/2025
Note:-
Gonna need some repetition to better understand this problem.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Left and right pointers for binary search.
        left, right = 0, len(nums) - 1

        while left <= right:
            # Get middle position.
            middle = (left + right) // 2

            # If the target is found, return it's index.
            if nums[middle] == target:
                return middle

            # Check if the left half is sorted.
            elif nums[middle] >= nums[right]:
                # Check if the target is in the sorted left half.
                if nums[middle] > target >= nums[left]: 
                    # Search the left.
                    right = middle - 1
                # Target is greater than the middle, or less than the left boundary,
                # so check the right half.
                else:
                    # Search the right.
                    left = middle + 1
            
            # Otherwise, the right half is sorted.
            else:
                # Check if the target is within the sorted right half.
                if nums[middle] < target <= nums[right]:
                    # Search the right.
                    left = middle + 1
                # Target is less than the middle, or greater than th e right boundary,
                # so check the left half.
                else:
                    right = middle - 1

        # Target not found.
        return -1

"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""