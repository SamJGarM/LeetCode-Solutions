"""
Author: Samuel Jaden García Muñoz
Date: 26/10/2025
Revised: 01/11/2025
Note:-

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Double-ended queue so we can popleft while appending to the right.
        dq = deque([root])

        while dq:
            # Node value, for storing the latest popped value.
            node = dq.popleft()

            # If we have a child node to the right, add it to the deque.
            if node.right:
                dq.append(node.right)

            # If we have a child node to the left, ...
            if node.left:
                dq.append(node.left)

        # Return the last popped node's value (node.val)
        return node.val

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""