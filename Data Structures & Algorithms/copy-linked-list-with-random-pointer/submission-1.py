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
        mp = {None:None}

        start = Node(0)
        newList = start

        curr = head
        while curr:
            newList.next = Node(curr.val)
            mp[curr] = newList.next
            curr = curr.next
            newList = newList.next

        while head:
            mp[head].random = mp[head.random]
            head = head.next

        return start.next
