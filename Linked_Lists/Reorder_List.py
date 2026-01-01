# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            nextNode = curr.next

            curr.next = prev
            prev = curr
            curr = nextNode
        
        while prev:
            tmp1 = head.next
            tmp2 = prev.next

            head.next = prev
            prev.next = tmp1

            head = tmp1
            prev = tmp2
            
        
