# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        lists = [l for l in lists if l]

        while lists:
            potential = float('inf')
            min_idx = 0

            for i in range(len(lists)):
                if lists[i].val < potential:
                    potential = lists[i].val
                    min_idx = i

            tail.next = lists[min_idx]
            tail = tail.next

            lists[min_idx] = lists[min_idx].next

            if lists[min_idx] is None:
                lists.pop(min_idx)

        return dummy.next
