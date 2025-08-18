"""
Author: Samuel Jaden García Muñoz
Date: 16/08/2025
Note:-
This version improves on the storage complexity, but is more time costly to code and less readable.
Normal version is probably good enough, but good to know this implementation as well.
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
        
        # Create a temporary node and assign it to the head of the linked list.
        node = head
        # Iterate through the list until you find a None value.
        while node:
            # Create a new node, our copy, and give it the value and next attributes of the current node.
            newNode = Node(node.val, node.next)
            # Then, amend the current node's next attribute to point to our new copy.
            node.next = newNode
            # Lastly, skip forward to the next node in the original linked list.
            node = newNode.next
            
        # Repeat the process above, while this time updating the random attribute of our copied nodes.
        node = head
        while node:
            # If the current node's random pointer does not point to Null...
            if node.random:
                # Update the random value of the copy of our current node (node.next.random)...
                # to the copy of the random node (node.random.next).
                node.next.random = node.random.next
            # Skip forward to the next original node (node.next.next).
            node = node.next.next

        # Iterate through one last time, and delete the original values from the list.
        node = head
        newHead = head.next
        while node:
            # Copy node
            newNode = node.next
            # Set the value of the original node to the copy node's next value.
            node.next = newNode.next
            # Set the copy node's next value to the next copied node (skipping the original),
            # or set it to null if none remain
            newNode.next = newNode.next.next if newNode.next else None
            # Continue to the next node (which is now the node after the copy node).
            node = node.next

        # Return the head of the new head
        return newHead

"""
Time Complexity: O(n)
Space Complexity: O(1), because we've reused the existing linked list.
"""