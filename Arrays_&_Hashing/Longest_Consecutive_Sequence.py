class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        longest = 0

        for n in nums:
            if (n-1) not in nums:
                length = 0
                while (n + length) in nums:
                    length += 1
                longest = max(longest, length)
        return longest