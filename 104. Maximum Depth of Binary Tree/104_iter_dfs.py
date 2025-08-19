"""
Author: Samuel Jaden García Muñoz
Date: 19/08/2025
Note:-
Iterative alternative for DFS.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If no root provided.
        if not root:
            return 0

        # Stack for keeping node, depth pairs.
        stack = [(root, 1)]
        # Variable for keeping track of the best depth found.
        max_depth = 0

        # Iterate throuh every pair in the stack.
        while stack:
            node, depth = stack.pop()

            # Append the left and right children if available.
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
            
            # And calculate the current max depth.
            max_depth = max(max_depth, depth)
            
        return max_depth
    
"""
Time Complexity: O(n)
Space Complexity: O(h) 
"""