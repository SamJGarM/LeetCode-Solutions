# 323. Number of Connected Components in an Undirected Graph
#
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.

# Constraints:
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Depth First Search
        def dfs(node):
            # If the node has already been visited, it already forms part of a component group that has been tracked.
            if node in visited:
                return

            # Mark the current node as visited.
            visited.add(node)
            # Iterate through each neighbor in the adjacency map (neighbors dict).
            for neighbor in neighbors[node]:
                # Run DFS from the neighbor node.
                dfs(neighbor)

        # Set for storing visited nodes.
        visited = set()

        # Adjacency map for neighbors of every vertex.
        ## We create a list for each vertex to track all edges to/from this
        neighbors = {i:[] for i in range(n)}
        # Iterate through every edge pair in the edges list
        for (node1, node2) in edges:
            # Since the graph is undirected, append to the lists within the dictionary for both ends of the edge
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        # Result Variable
        res = 0

        # Iterate through each node.
        for node in range(n):
            # If a node hasn't been visited, we can assume it doesn't form part of any group that has been visited yet.
            if node not in visited:
                # Run DFS from this node and increase the result variable (amount of groups)
                dfs(node)
                res += 1

        # Return the resulting amount of groups
        return res