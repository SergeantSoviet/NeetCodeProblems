class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right
        while left <= right:
            mid = (left+right)//2
            count = 0
            for i in range(len(piles)):
                    count += math.ceil(piles[i] / mid)
            if h >= count:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer