# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head
        while f and f.next:
            if s.next and f.next.next:
                s = s.next
                f = f.next.next
            else:
                break
        curr = s.next
        s.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = head
        while curr and prev:
            nxt = curr.next
            prevNext = prev.next
            curr.next = prev
            prev.next = nxt
            curr = nxt
            prev = prevNext



