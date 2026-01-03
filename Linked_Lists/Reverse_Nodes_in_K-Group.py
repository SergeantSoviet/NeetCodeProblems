# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupP = dummy

        while True:
            kNode = self.getK(groupP, k)
            if not kNode:
                break
            groupN = kNode.next

            prev = kNode.next
            curr = groupP.next

            while curr != groupN:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            tmp = groupP.next
            groupP.next = kNode
            groupP = tmp
        
        return dummy.next

    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1 
        return curr