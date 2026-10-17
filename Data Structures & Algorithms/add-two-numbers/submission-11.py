# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        start = ListNode(0)
        res = start
        self.rec(l1, l2, res, 0)
        return start.next

    def rec(self, list1: Optional[ListNode], list2: Optional[ListNode], res: Optional[ListNode], prev: int) -> None:
        if not list1 and not list2:
            if prev == 1:
                res.next = ListNode(1)
                return
            else:
                return

        curr = 0
        answer = prev
        if list1:
            answer += list1.val
        if list2:
            answer += list2.val

        if answer >= 10:
                answer = answer - 10
                curr = 1

        if list1 and not list2:
            res.next = ListNode(answer)
            return self.rec(list1.next, list2, res.next, curr)
            
        elif list2 and not list1:
            res.next = ListNode(answer)
            return self.rec(list1, list2.next, res.next, curr)

        else:
            res.next = ListNode(answer)
            return self.rec(list1.next, list2.next, res.next, curr)
                
            




        
