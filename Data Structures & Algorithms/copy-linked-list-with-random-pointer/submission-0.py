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
        
        the_map = {}

        curr = head
        
        while curr:

            copy = Node(curr.val)
            the_map[curr] = copy
            curr = curr.next

        curr = head
        
        the_map[None] = None

        while curr:
            
            copy = the_map[curr]
            copy.next = the_map[curr.next]
            copy.random = the_map[curr.random]
            curr = curr.next
        
        return the_map[head]
