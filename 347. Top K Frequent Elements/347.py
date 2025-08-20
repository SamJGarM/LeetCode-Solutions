"""
Author: Samuel Jaden García Muñoz
Date: 20/08/2025
Note:-
Bucket sort solution.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap for tracking the count of each number
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        # Frequency array of buckets for sorting by occurrence.
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            freq[value].append(key)

        # Iterate backwards from the frequency array...
        res = []
        for i in range(len(freq)-1, -1, -1):
            # Appending items from non-empty buckets until k items are appended to the result.
            for j in freq[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""