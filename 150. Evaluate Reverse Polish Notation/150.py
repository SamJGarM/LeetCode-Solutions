"""
Author: Samuel Jaden García Muñoz
Date: 20/08/2025
Revised: 05/11/2025
Note:-

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack for storing the numbers for operation.
        stack = []
        
        for token in tokens:
            # Encapsulating if statement to avoid rewriting the stack.pop operations.
            if token in ["*", "/", "+", "-"]:
                # Get the second value (from the top of the stack), and the first value
                # (value prior) and conduct the operation accordingly.
                second = stack.pop()
                first = stack.pop()
                # If multiplication...
                if token == "*":
                    stack.append(first * second)
                # If division...
                elif token == "/":
                    # Using (int) to round towards 0
                    stack.append(int(first / second))
                # If addition...
                elif token == "+":
                    stack.append(first + second)
                # If subtraction...
                elif token == "-":
                    stack.append(first - second)
            # If not an operation, add the value to the stack.
            else:
                stack.append(int(token))
        # Return the result on the stack.
        return stack[0]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""