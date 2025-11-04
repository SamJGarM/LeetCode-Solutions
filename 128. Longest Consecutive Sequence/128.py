"""
Author: Samuel Jaden García Muñoz
Date: 03/11/2025
Revised: 
Note:-

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Turn the list into a set for O(1) look-up and to remove duplicates.
        nums = set(nums)

        # Result variable for tracking longest sequence.
        res = 0
        # Iterate through every number in the set...
        for num in nums:
            # If the number before this one is in the set, we know this isn't the beginning of a sequence.
            if num - 1 in nums:
                continue
            
            # Otherwise, we can start counting from this value onwards to see how long this sequence is.
            seq_counter = 0
            while num + seq_counter in nums:
                seq_counter += 1
            
            # If it surpasses the current longest, overwrite the value.
            res = max(seq_counter, res)

        return res

"""
Time Complexity: O(2n) => O(n)
Space Complexity: O(n)
"""