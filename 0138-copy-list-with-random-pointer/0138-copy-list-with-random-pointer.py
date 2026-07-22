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
        curr1 = head
        map = {}
        while curr1:
            map[curr1] = Node(curr1.val)
            curr1 = curr1.next
        curr1 = head
        while curr1:
            map[curr1].next = map[curr1.next] if curr1.next else None
            map[curr1].random = map[curr1.random] if curr1.random else None
            curr1 = curr1.next
        return map[head] if head else None
