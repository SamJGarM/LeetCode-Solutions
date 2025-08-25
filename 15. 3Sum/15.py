"""
Author: Samuel Jaden García Muñoz
Date: 25/08/2025
Note:-
2Sum with an outer loop.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list, so we can effectively implement a 2Sum solution with an outer loop.
        nums.sort()

        # List for all 0-sum results.
        res = []

        # Iterate through every number for the first position.
        for i in range(len(nums)):
            # Check for repeat values at position i.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Get the left and right pointers.
            left, right = i + 1, len(nums) - 1

            # Until the pointers meet...
            while left < right:
                # Calculate the total with the current pointers.
                total = nums[i] + nums[left] + nums[right]

                # If we've got a successful result...
                if total == 0:
                    # Add it to the output list.
                    res.append([nums[i], nums[left], nums[right]])
                    # And increase our left pointer.
                    left += 1
                    # Like previously, while our left pointer is the same as the previous, go forward to void duplicate solutions.
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                        
                # If our total is too large, decrease the right pointer.
                elif total > 0:
                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1

                # Otherwise, increase the left pointer.
                else:
                    left += 1

        # Return the result.
        return res

"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""