# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1values = []
        l2values = []
        
        while l1:
            l1values.append(l1.val)
            l1 = l1.next
        
        while l2:
            l2values.append(l2.val)
            l2 = l2.next
        
        num = int("".join(map(str, reversed(l1values)))) + int("".join(map(str, reversed(l2values))))
        
        if num == 0:
            return ListNode(0)

        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        dummy = ListNode(0)
        curr = dummy
        for d in digits:
            curr.next = ListNode(d)
            curr = curr.next
        return dummy.next