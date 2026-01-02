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
        oldNtoNewN = { None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldNtoNewN[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldNtoNewN[curr]
            copy.next = oldNtoNewN[curr.next]
            copy.random = oldNtoNewN[curr.random]
            curr = curr.next

        return oldNtoNewN[head]