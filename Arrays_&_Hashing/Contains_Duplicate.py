class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for n in nums:
            dict[n] = 1
        
        if len(dict.values()) != len(nums):
            return True
        return False

