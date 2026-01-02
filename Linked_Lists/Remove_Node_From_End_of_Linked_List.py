# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenP = head
        count = 0
        while lenP:
            lenP = lenP.next
            count += 1
        
        pos = (count + 1) - n

        curr = head
        if pos == 1:
            head = curr.next
            return head
        prev = None
        for i in range(1, pos):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return head