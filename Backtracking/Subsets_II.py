class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        sol = []
        n = len(nums)
        nums.sort()

        def backtrack(i):
            if i == n:
                if sol.sort not in res:
                    res.add(tuple(sol[:]))
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return list(res)
            