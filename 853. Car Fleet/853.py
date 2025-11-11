"""
Author: Samuel Jaden García Muñoz
Date: 10/11/2025
Revised: 11/11/2025
Note:-

"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Group the two lists together and sort them by inverse numerical order of position.
        cars = sorted([[pos, spd] for pos, spd in zip(position, speed)])[::-1]
        # Create a stack for storing fleet time-to-target values.
        stack = []

        # Iterate through each car (position/speed pair)
        for pos, spd in cars:
            # Calculate the time to the target.
            timeToTarget = (target - pos) / spd
            # If the top of the stack takes longer to get to the target than the current car, then we know
            # that this car will join that fleet.
            if stack and stack[-1] >= timeToTarget:
                continue
            # Otherwise, we know that this vehicle is now the head of a new fleet.
            stack.append(timeToTarget)
            
        # Return the length of the stack, as this contains the head of each fleet.
        return len(stack)


"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""