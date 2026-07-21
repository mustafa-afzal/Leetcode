# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, nxt = head, head
        steps = 0
        while nxt:
            steps += 1
            nxt = nxt.next
        dist = steps - n
        if dist == 0:
            return head.next
        while curr and dist - 1:
            curr = curr.next
            dist -= 1
        curr.next = curr.next.next 
        return head