class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Dict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Dict:
                return [Dict[diff], i]
            else:
                Dict[n] = i