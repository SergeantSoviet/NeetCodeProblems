class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Dict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Dict:
                return [Dict[diff], i]
            else:
                Dict[n] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = 1
        output = []
        while i < len(nums):
            j = i +1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                j += 1
            i += 1
        return output[0:2]