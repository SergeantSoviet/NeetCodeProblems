class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        res = []

        def backTrack(i, curr, total):
            if target == total:
                res.append(curr[:])
                return
            if i >= n or total > target:
                return
            
            curr.append(candidates[i])
            backTrack(i+1, curr, total+candidates[i])
            curr.pop()

            while i+1 < n and candidates[i] == candidates[i+1]:
                i+=1
            backTrack(i+1, curr, total)
            
        backTrack(0, [], 0)
        return res