"""
Author: Samuel Jaden García Muñoz
Date: 16/08/2025
Note:-
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If an empty linked list is provided, return None.
        if not head:
            return None
        
        # Create a hashmap for storing the node connections.
        # The current node will serve as a key, and the value will be the cloned node.
        hashmap = {}

        # Create a temporary node and assign it to the head of the linked list.
        node = head
        # Iterate through the list until you find a None value.
        while node:
            # Create the dict entry in the hashmap and continue down the list.
            hashmap[node] = Node(node.val)
            node = node.next
            
        # Repeat the process above, this time setting the next and random values,
        # as all nodes now have a copy entry in the dict.
        node = head
        while node:
            # We use hashmap.get to avoid any potential key errors
            # for when node.random/node.next is null.
            hashmap[node].next = hashmap.get(node.next)
            hashmap[node].random = hashmap.get(node.random)
            node = node.next

        # Return the head of the copy list.
        return hashmap[head]

# Time Complexity: O(n)
# Storage Complexity: O(n)