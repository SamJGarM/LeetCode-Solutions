"""
Author: Samuel Jaden García Muñoz
Date: 25/08/2025
Note:-

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Append empty cost (symbolic of the final step)
        cost.append(0)

        # Iterate from the top of the steps (with 2 steps of gap for option 1 and option 2)
        for i in range(len(cost) - 3, -1, -1):
            # Update the cost of each step to the lowest cost to reach said step.
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

        # Return the minimum value of option 1 (1 step) or option 2 (2 steps)
        return min(cost[0], cost[1])

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""