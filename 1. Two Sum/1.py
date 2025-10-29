"""
Author: Samuel Jaden García Muñoz
Date: 26/10/2025
Revised: 29/10/2025
Note:-

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to contain all numbers that have been iterated over.
        hashMap = {}

        # Iterate through every number...
        for i in range(len(nums)):
            #... and if the complement (target - number) is in the hashmap..., return the answer.
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            # Otherwise, add the current entry to the hashmap.
            hashMap[nums[i]] = i

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""