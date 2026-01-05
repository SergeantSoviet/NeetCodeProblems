class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        maxHeap = stones
        while len(maxHeap) > 1:
            x = heapq._heappop_max(maxHeap)
            y = heapq._heappop_max(maxHeap)

            if x == y:
                continue
            elif x > y:
                newVal = x - y
                heapq._heappush_max(maxHeap, newVal)
            else:
                newVal = y-x
                heapq._heappush_max(maxHeap, newVal)

        if maxHeap:
            return maxHeap[0]
        else:
            return 0