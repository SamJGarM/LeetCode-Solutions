"""
Author: Samuel Jaden García Muñoz
Date: 19/08/2025
Note:-
Good question for testing out different algorithms, so I'll do multiple solutions for it.   
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Depth-first Search
        def dfs(node):
            # If at an empty destination, return 0
            if not node:
                return 0
            # Return the maximum of the left and right branches, plus 1
            return max(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)
    
"""
Time Complexity: O(n)
Space Complexity: O(h) 
"""