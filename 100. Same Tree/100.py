"""
Author: Samuel Jaden García Muñoz
Date: 22/10/2025
Revised: 
Note:-

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_node, q_node):
            # If at least one of the roots is empty...
            if p_node == None or q_node == None:
                # Return them if they are different.
                if p_node != q_node:
                    return False
                # Otherwise return true, as it means both are empty, and thusly equal.
                return True

            # If the roots are of different value, the trees are not identical.
            if p_node.val != q_node.val:
                return False

            # Repeat the process for the left and right nodes.
            return dfs(p_node.left, q_node.left) and dfs(p_node.right, q_node.right)

        return dfs(p, q)

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""