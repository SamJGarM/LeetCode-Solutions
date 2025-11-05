"""
Author: Samuel Jaden García Muñoz
Date: 19/08/2025
Revised: 05/11/2025
Note:-

"""

class MinStack:

    def __init__(self):
        # List for maintaining all values currently in the stack.
        self.stack = []
        # List that keeps track of the minimum value at any given position of the stack.
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If there is a previous value, append the minimum of the current value and the previous.
        # Otherwise, append the value as the initial in the list.
        self.minimum.append(val) if not self.minimum else self.minimum.append(min(self.minimum[-1], val))

    def pop(self) -> None:
        # Simple pop operations, though if requested to be done without functions, a simple slice [-1] could be used instead.
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Time Complexity: O(1)
Space Complexity: O(n)
"""