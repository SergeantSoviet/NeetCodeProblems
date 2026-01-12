class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        res = []

        def backTrack(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= n or total > target:
                return

            curr.append(nums[i])
            backTrack(i, curr, total + nums[i])

            curr.pop()
            backTrack(i+1, curr, total)

        backTrack(0, [], 0)
        return res
