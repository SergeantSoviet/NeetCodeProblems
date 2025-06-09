class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dict = {}
        dictlist = []
        output = []

        for i in range(0, len(nums)):
            dictlist = nums[:i] + nums[i+1:]
            dict[i] = dict.get(i, []) + dictlist

        for k, v in dict.items():
            count = 1
            for n in v:
                count *= n
            output.append(count)

        return output