"""
Author: Samuel Jaden García Muñoz
Date: 19/08/2025
Revised: 23/10/2025
Note:-
I see there's a better solution, so I'll figure out that one next time.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Create an array for each position in the nums list and calculate the prefix product.
        # However, position the results at the subsequent index value to avoid edge cases.
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        # Repeat for the suffix products of every position.
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        # And lastly, calculate the resulting product for each position.
        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        # Return the resulting list.
        return res
    
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""