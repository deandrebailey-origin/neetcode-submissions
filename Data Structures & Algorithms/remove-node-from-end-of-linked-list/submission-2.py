# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy = ListNode(0,head)
        cur = dummy
        k = 0

        while cur:
            k = k + 1
            cur = cur.next

        a = k - n -1
        cur = dummy

        while a > 0:
            cur = cur.next
            a -= 1
        

        cur.next = cur.next.next

        return dummy.next
