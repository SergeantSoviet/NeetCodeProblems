class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxLeft = []
        maxRight = []
        minLR = []

        for i in range(length):
            if i == 0:
                maxLeft.append(height[i])
            elif height[i - 1] > maxLeft[i-1]:
                maxLeft.append(height[i - 1])
            else:
                maxLeft.append(maxLeft[i-1])

        for i in range(1, length+1):
            if i == 1:
                maxRight.append(0)
            elif height[-i + 1] > maxRight[i - 2]:
                maxRight.append(height[-i + 1])
            else:
                maxRight.append(maxRight[i-2])

        for i in range(length):
            minLR.append(min(maxLeft[i], maxRight[-1 - i]))

        trapped = 0
        for i in range(length):
            area = minLR[i]- height[i]
            if area > 0:
                trapped += area

        return trapped