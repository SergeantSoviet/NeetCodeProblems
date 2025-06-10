class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            Sum = numbers[l] + numbers[r]

            if Sum > target:
                r -= 1
            elif Sum < target:
                l += 1
            else:
                return [l+1, r+1]

