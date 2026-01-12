class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res, sol = [],[]

        def backTrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # then we move left
            backTrack(i+1)

            #then we mve right
            sol.append(nums[i])
            backTrack(i+1)
            sol.pop()

        backTrack(0)
        return res