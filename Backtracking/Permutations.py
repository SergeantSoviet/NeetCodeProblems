class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res, sol = [], []
        used = [False] * len(nums)

        def backTrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                sol.append(nums[i])
                backTrack()
                sol.pop()
                used[i] = False

        backTrack()
        return res