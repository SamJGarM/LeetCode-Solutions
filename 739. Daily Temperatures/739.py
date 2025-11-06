"""
Author: Samuel Jaden García Muñoz
Date: 05/11/2025
Revised: 06/11/2025
Note:-

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # List for storing the results of index distances to increase in temperature.
        res = [0] * len(temperatures)
        # Stack for storing temperature values, and their index, until a greater value is found.
        stack = []

        # Iterate through every entry in temperatures
        for idx, temp in enumerate(temperatures):
            # So long as there is an item in the stack, compare to see if a new highest temperature has been found.
            while stack and temp > stack[-1][0]:
                # If so, remove it 0from the stack and update its corresponding res entry.
                item = stack.pop()
                res[item[1]] = idx - item[1]
            # Lastly, add the newest entry into the stack.
            stack.append([temp, idx])

        return res

"""
Time Complexity: O(2n) => O(n)
Space Complexity: O(2n) => O(n)
"""