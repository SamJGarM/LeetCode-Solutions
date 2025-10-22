"""
Author: Samuel Jaden García Muñoz
Date: 22/08/2025
Revised: 22/10/2025
Note:-
Very cute problem with only one line needed for the solution.
(Though I could do it iteratively by populating the set num by num
if ever asked to elaborate in an interview setting)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Turn the array provided into a set, and compare it's length to the length of the array.
        # Any difference in lengths will mean that a duplicate was present.
        return len(set(nums)) != len(nums)

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""