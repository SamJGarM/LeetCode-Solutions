"""
Author: Samuel Jaden García Muñoz
Date: 22/10/2025
Revised: 03/11/2025
Note:-
Expansion on exercise 100.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS to check if trees from node and subNode as roots are identical.
        def dfs(node, subNode):
            # If at least one of the roots is empty...
            if node == None or subNode == None:
                # Return them if they are different.
                if node != subNode:
                    return False
                # Otherwise return true, as it means both are empty, and thusly equal.
                return True

            # If the roots are of different value, the trees are not identical.
            if node.val != subNode.val:
                return False

            # Repeat the process for the left and right nodes.
            return dfs(node.left, subNode.left) and dfs(node.right, subNode.right)
        
        # If the subRoot (and therefore the subtree) is empty, return True.
        if subRoot == None:
            return True

        # Otherwise, if the root is empty, we know the subRoot cannot contain a subtree that is within the main tree.
        if root == None:
            return False

        # In that case, check if the trees are the same from the root node.
        if dfs(root, subRoot):
            return True

        # If not, iterate recursively through the left and right children of the root node, and return True if a match for the subtree is found.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


"""
Time Complexity: O(m*n)
Space Complexity: O(h (of main tree))
"""