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