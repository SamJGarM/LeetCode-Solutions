"""
Author: Samuel Jaden García Muñoz
Date: 09/11/2025 
Revised: 
Note:-
Very similar to 739.
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to map a value to its index and the greater value.
        greaterMap = {val:[idx, -1] for idx, val in enumerate(nums2)}

        # Stack for maintaining values until a greater value has been found.
        stack = []
        for idx, val in enumerate(nums2):
            # Once a greater value has been found...
            while stack and stack[-1][1] < val:
                # ...take it out of the stack and keep track of the greater value in the map.
                stack_idx, stack_val = stack.pop()
                greaterMap[stack_val][1] = val
            # Append the current value to the stack for future comparison.
            stack.append((idx, val))

        # Iterate through each number in the subset and add the next greater value in the set to the result.
        res = []
        for num in nums1:
            res.append(greaterMap[num][1])

        # Return the result.
        return res

"""
Time Complexity: O(n + m)
Space Complexity: O(n)
"""