class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (right + left) //2
            if target in matrix[mid]:
                return True
            if target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
        return False