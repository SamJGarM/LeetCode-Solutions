"""
Author: Samuel Jaden García Muñoz
Date: 22/08/2025
Revised: 29/09/2025
Note:-
Should try a BFS version as well.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary for mapping nodes to their corresponding clone.
        cloneMap = {}

        # Conduct a depth-first search from a given node.
        def dfs(node):
            # If the node is already in the clone map, we can return the cloned node.
            if node in cloneMap:
                return cloneMap[node]

            # Otherwise, create a copy of the current node, and store it in the map.
            copy = Node(node.val)
            cloneMap[node] = copy

            # Iterate through each neighbor in the current node.
            for neighbor in node.neighbors:
                # Add the clone of the neighbor to the neighbors list of the current node.
                copy.neighbors.append(dfs(neighbor))
            
            # Return the clone.
            return copy
            
        # If node isn't null, return the "head" of the clone graph, otherwise return null.
        return dfs(node) if node else None

"""
Time Complexity: O(V + E)
Space Complexity: O(V)
"""