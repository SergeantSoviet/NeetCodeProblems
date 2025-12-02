class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        count = [[] for i in range(len(nums) + 1)]

        for n in sorted(nums):
            dict[n] = dict.get(n, 0) + 1

        for key, value in dict.items():
            count[value].append(key)

        output = []
        for i in range(len(count) - 1, 0, -1):
            for key in count[i]:
                output.append(key)
                if len(output) == k:
                    return output
                
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        storage = []
        dict = {}
        
        for i in range(len(nums)):
            dict[nums[i]] = 1 + dict.get(nums[i], 0)
        
        dict_sorted = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
        for key, v in dict_sorted.items():
            output.append(key)
        
        return output[0:k]