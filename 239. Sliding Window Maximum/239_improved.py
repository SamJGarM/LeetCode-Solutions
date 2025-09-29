"""
Author: Samuel Jaden García Muñoz
Date: 29/09/2025
Revised: 
Note:-
Slight improvement, removing the need for left/right pointers.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        _deque = deque()

        for i in range(len(nums)):
            while _deque and nums[_deque[-1]] < nums[i]:
                _deque.pop()
            _deque.append(i)

            if i - k >= _deque[0]:
                _deque.popleft()

            if i >= k - 1:
                res.append(nums[_deque[0]])

        return res

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""