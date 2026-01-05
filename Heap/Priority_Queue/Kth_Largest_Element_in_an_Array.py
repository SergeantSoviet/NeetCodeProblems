class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq._heapify_max(nums)
        maxHeap = nums

        count = 1
        while count < k:
            heapq._heappop_max(maxHeap)
            count += 1
        
        return maxHeap[0]