"""
Author: Samuel Jaden García Muñoz
Date: 31/08/2025
Note:-

"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Helper function to conduct insertion sort on each bucket.
        def insertionSort(bucket):
            # Iterate through every item
            for i in range(1, len(bucket)):
                # Set both pointers to the value of the current iteration.
                j = i
                # So long as the second pointer (j) is greater than 0, and the item at the position
                # previous to the pointer j is lesser, swap j with the previous item.
                while j > 0 and bucket[j-1] > bucket[j]:
                    bucket[j-1], bucket[j] = bucket[j], bucket[j-1]
                    j -= 1
            # Return the sorted bucket.
            return bucket

        # Get the size, minimum value, and maximum value from the array.
        n, minVal, maxVal = len(nums), min(nums), max(nums)

        # If the array's len is 1 or smaller (only contains an item or is empty)
        # or contains all duplicate entries, return the input array.
        if n <= 1 or minVal == maxVal:
            return nums

        # Create buckets for as many possible different numbers (length of array).
        buckets = [[] for _ in range(n + 1)]
        
        # Iterate through each numbe in the array, and insert it into the appropriate bucket.
        for num in nums:
            # Get the appropriate index by multiplying the size of the array by the division of the
            # difference of the current number and the minimum value in the array, by the difference
            # of the maximum value and the minimum value, and rounding it.
            index = int(n * (num - minVal) / (maxVal - minVal))
            buckets[index].append(num)

        # Iterate through each bucket, and sort the components inside using a different sorting algorithm.
        # (In this case, I used insertion sort)
        res = []
        for bucket in buckets:
            insertionSort(bucket)
            res.extend(bucket)
        
        # Return the sorted array.
        return res
            

"""
Time Complexity: O(n + k (buckets))
Space Complexity: O(n + k (buckets)) 
"""