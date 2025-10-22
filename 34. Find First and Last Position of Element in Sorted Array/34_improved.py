"""
Author: Samuel Jaden García Muñoz
Date: 20/08/2025
Revised: 10/22/2025
Note:-
Improved version that now reaches O(log n) time complexity as requested by the exercise.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Function for conducting the search.
        # Direction == 0 -> Left, Direction == 1 -> Right
        def search(direction):
            # Tracks the furthest extent in a given direction of the target being found.
            edge = -1

            # Left and right pointers for a binary search.
            left, right = 0, len(nums) - 1

            while left <= right:
                # Get the middle position.
                middle = (left + right) // 2

                # If the target is found...
                if nums[middle] == target:
                    # A new edge has been found.
                    edge = middle
                    # If checking the right, increase the left pointer
                    if direction:
                        left = middle + 1
                    # If checking the left, decrease the right pointer.
                    else:
                        right = middle - 1
                    

                # Otherwise operate as a binary search would normally.
                elif nums[middle] > target:
                    right = middle - 1

                else:
                    left = middle + 1

            # Return the furthest location of the target (or -1)
            return edge
        
        # Return the outcomes for left and right search.
        return [search(0), search(1)]

"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""