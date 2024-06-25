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
        lookup = {None:None}

        og = head
        while og:
            dup = Node(og.val)
            lookup[og] = dup
            og = og.next

        og = head
        while og:
            dup = lookup[og]
            dup.next = lookup[og.next]
            dup.random = lookup[og.random]
            og = og.next
        
        return lookup[head]
    