"""
Author: Samuel Jaden García Muñoz
Date: 18/08/2025
Note:-

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Result variable for appending the maximum of each k-sized group.
        res = []
        
        # Double-ended queue for storing the indexes of numbers from nums.
        _deque = deque()

        # Left and right pointers for moving the sliding window through the nums list.
        left, right = 0, 0

        # Iterate through the list.
        for i in range(len(nums)):
            # While the deque isn't empty and the current num is greater than the last item in the deque
            # pop the last item from the deque.
            while _deque and nums[i] > nums[_deque[-1]]:
                _deque.pop()
            # Append the index of the current item into the deque.
            _deque.append(i)

            # If the left-end of the window surpasses the current maximum of the deque, pop it.
            if left > _deque[0]:
                _deque.popleft()
            
            # If window size has been met.
            if right - left + 1 >= k:
                # Append the current maximum value in the deque (at position 0) to the result list
                # and increase the left pointer.
                res.append(nums[_deque[0]])
                left += 1
            # Increase the right pointer.
            right += 1

        # Return the result list.
        return res
    
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""