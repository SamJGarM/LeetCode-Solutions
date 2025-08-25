"""
Author: Samuel Jaden García Muñoz
Date: 25/08/2025
Note:-

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Iterate recursively through each potential stair.
        def dfs(steps_left):
            # If steps left <= 1, we can reach the end within 1 move, so no cost.
            if steps_left <= 1:
                return 0

            # If this path has been traversed before, pull the stored result.
            if steps_left in memo:
                return memo[steps_left]
            
            # Otherwise, store the minimum route from this step in the dictionary.
            memo[steps_left] = min(cost[steps_left-1] + dfs(steps_left - 1), cost[steps_left - 2] + dfs(steps_left - 2))

            # Return the result.
            return memo[steps_left]

        # Map for storing results.
        memo = {}
        
        # Return the result for len(cost) stairs.
        return dfs(len(cost))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""