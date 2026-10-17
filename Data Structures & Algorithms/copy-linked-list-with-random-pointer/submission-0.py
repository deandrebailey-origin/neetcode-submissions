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
        h = {None: None}
        cur = head
        while cur:
            h[cur] = Node(cur.val)    # pass 1: copies only
            cur = cur.next

        cur = head
        while cur:
            h[cur].next = h[cur.next]       # pass 2: wire next
            h[cur].random = h[cur.random]   # pass 2: wire random
            cur = cur.next

        return h[head]