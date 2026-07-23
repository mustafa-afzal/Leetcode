# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = l1
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l1 = prev
        prev = None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l2 = prev
        strL1 = ""
        while l1:
            strL1 += str(l1.val)
            l1 = l1.next
        strL2 = ""
        while l2:
            strL2 += str(l2.val)
            l2 = l2.next
        res = str(int(strL1) + int(strL2))
        res = res[::-1]
        dummy = ListNode(0)
        curr = dummy
        for s in res:
            curr.next = ListNode(int(s))
            curr = curr.next
        return dummy.next
