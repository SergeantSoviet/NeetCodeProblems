class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list = []
        left = 1
        right = len(nums) - 1
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = i+2
            while left < right and left < len(nums) - 1:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    if [nums[i], nums[left], nums[right]] not in list:
                        list.append([nums[i], nums[left], nums[right]])
                    right += 1
                else:
                    right += 1
                
                if right == len(nums):
                    left += 1
                    right = left + 1  

        return list